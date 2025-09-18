import { StyleSheet } from "react-native";

export default StyleSheet.create({
  scrollViewContainer: {
    // Estilo para o ScrollView
    flex: 1,
    backgroundColor: "#f5f5f5",
  },

  container: {
    // Remova 'justifyContent: center' e 'alignItems: center'
    // para permitir que os cards se posicionem naturalmente.
    flex: 1,
    backgroundColor: "#f5f5f5", // Fundo claro para o app
    paddingTop: 50, // Espaço para a barra de status no topo
  },

  mainTitle: {
    // Novo estilo para o título principal
    fontSize: 28,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
    color: "#333",
  },
  // Outros estilos do card estão em PontoTuristicoCard.js
});
