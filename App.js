import { View, Text, FlatList, TouchableOpacity, Image, StyleSheet } from "react-native";

// Dados estáticos
const receitas = [
  {
    id: "1",
    titulo: "Bolo de Chocolate",
    imagem: "https://cdn.casaeculinaria.com/wp-content/uploads/2022/10/04101905/Bolo-de-chocolate-2.webp",
    ingredientes: ["2 ovos", "1 xícara de açúcar", "1 xícara de farinha", "1/2 xícara de chocolate em pó"],
    preparo: "Misture tudo, coloque em forma untada e leve ao forno por 40 minutos a 180ºC."
  },
  {
    id: "2",
    titulo: "Macarrão à Bolonhesa",
    imagem: "https://inst.destromacro.com.br/wp-content/uploads/2022/04/espaguete-com-molho-a-bolonhesa-798x532-1.jpeg",
    ingredientes: ["200g de macarrão", "100g de carne moída", "1 lata de molho de tomate"],
    preparo: "Cozinhe o macarrão, frite a carne moída, junte o molho e sirva com queijo ralado."
  }
];

// Tela de lista de receitas
export default function App() {
  const renderItem = ({ item }) => (
    <TouchableOpacity style={styles.card}>
      <Image source={{ uri: item.imagem }} style={styles.imagem} />
      <Text style={styles.titulo}>{item.titulo}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>📖 Minhas Receitas</Text>
      <FlatList
        data={receitas}
        keyExtractor={(item) => item.id}
        renderItem={renderItem}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: "#fff" },
  header: { fontSize: 24, fontWeight: "bold", marginBottom: 20, textAlign: "center", marginTop: 20},
  card: { marginBottom: 20, backgroundColor: "#f9f9f9", borderRadius: 10, padding: 10, elevation: 3 },
  imagem: { width: "100%", height: 150, borderRadius: 10 },
  titulo: { fontSize: 18, fontWeight: "bold", marginTop: 10, textAlign: "center" }
});
