import discord
from discord.ext import commands
from discord.ui import Button, View
from datetime import datetime, timedelta


class Calendar(commands.Cog):
    """Cog to handle reservation calendar and booking logic"""

    def __init__(self, bot):
        self.bot = bot
        # Store reservations in memory (later replace with a DB)
        # Format: { "DD/MM/YYYY": { "08:00": user_id, ... } }
        self.reservations = {}

    # ---------------- Command to open calendar ----------------
    @commands.command(name='calendario')
    async def calendar(self, ctx):
        """Shows the next 7 days for the user to pick a date"""
        today = datetime.today()
        embed = discord.Embed(title="📅 Reservation Calendar",
                              description="Choose a day to make a reservation",
                              color=discord.Color.blue())

        buttons = View()

        for i in range(7):
            day = today + timedelta(days=i)
            date_str = day.strftime("%d/%m/%Y")

            button = Button(label=date_str, style=discord.ButtonStyle.green)

            async def callback(interaction, date=date_str):
                await self.show_times(interaction, date)

            button.callback = callback
            buttons.add_item(button)

        await ctx.send(embed=embed, view=buttons)

    # ---------------- Show times for a selected day ----------------
    async def show_times(self, interaction, date):
        embed = discord.Embed(title=f"⏰ Choose starting time on {date}",
                              description="Then choose the ending time",
                              color=discord.Color.green())

        buttons = View()

        for hour in range(8, 21):
            time_slot = f"{hour:02d}:00"

            # Already reserved -> red button disabled
            if date in self.reservations and time_slot in self.reservations[
                    date]:
                button = Button(label=time_slot,
                                style=discord.ButtonStyle.red,
                                disabled=True)
            else:
                button = Button(label=time_slot,
                                style=discord.ButtonStyle.blurple)

                async def callback(interaction, h=time_slot, d=date):
                    await self.choose_end(interaction, d, h)

                button.callback = callback

            buttons.add_item(button)

        await interaction.response.send_message(embed=embed,
                                                view=buttons,
                                                ephemeral=True)

    # ---------------- Choose ending time ----------------
    async def choose_end(self, interaction, date, start_time):
        embed = discord.Embed(
            title=f"📌 Reserve on {date}",
            description=f"Start: {start_time}\nNow choose the ending time:",
            color=discord.Color.purple())

        buttons = View()
        start_hour = int(start_time.split(":")[0])

        for hour in range(start_hour + 1, 22):
            end_time = f"{hour:02d}:00"
            conflict = any(f"{h:02d}:00" in self.reservations.get(date, {})
                           for h in range(start_hour, hour))

            if conflict:
                button = Button(label=end_time,
                                style=discord.ButtonStyle.red,
                                disabled=True)
            else:
                button = Button(label=end_time,
                                style=discord.ButtonStyle.green)

                async def callback(interaction,
                                   d=date,
                                   i=start_time,
                                   f=end_time):
                    await self.reserve_slot(interaction, d, i, f)

                button.callback = callback

            buttons.add_item(button)

        await interaction.response.send_message(embed=embed,
                                                view=buttons,
                                                ephemeral=True)

    # ---------------- Reserve the slot ----------------
    async def reserve_slot(self, interaction, date, start_time, end_time):
        start_hour = int(start_time.split(":")[0])
        end_hour = int(end_time.split(":")[0])

        if date not in self.reservations:
            self.reservations[date] = {}

        conflicts = [
            f"{h:02d}:00" for h in range(start_hour, end_hour)
            if f"{h:02d}:00" in self.reservations[date]
        ]
        if conflicts:
            await interaction.response.send_message(
                f"❌ There are already reservations at {', '.join(conflicts)} on {date}.",
                ephemeral=True)
            return

        # Save reservations by user ID
        for h in range(start_hour, end_hour):
            self.reservations[date][f"{h:02d}:00"] = interaction.user.id

        # Send DM confirmation
        try:
            await interaction.user.send(
                f"✅ Your reservation on **{date}** from **{start_time}** to **{end_time}** has been confirmed!"
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                f"⚠️ {interaction.user.mention}, I couldn’t send you a DM. Please enable DMs to receive confirmations.",
                ephemeral=True)
            return

        print(
            f"✅ Reservation confirmed for {interaction.user.name} ({interaction.user.id}) on {date} from {start_time} to {end_time}"
        )
        print(f"Global name: {interaction.user.global_name}")

        await interaction.response.send_message(
            "✅ Reservation confirmed! (check your DM 👀)", ephemeral=True)


# ---------------- Setup function to load the Cog ----------------
async def setup(bot):
    await bot.add_cog(Calendar(bot))
