document.querySelector('.open-modal').addEventListener('click', () => {
  document.getElementById('modal').style.display = 'flex';
});

document.querySelector('.close-modal').addEventListener('click', () => {
  document.getElementById('modal').style.display = 'none';
});

document.getElementById('modal').addEventListener('click', (e) => {
  if (e.target.id === 'modal') {
    document.getElementById('modal').style.display = 'none';
  }
});
