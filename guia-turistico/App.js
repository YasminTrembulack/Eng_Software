import { StatusBar } from "expo-status-bar";

import {Text, View, ScrollView } from "react-native"; // <--- Importe ScrollView

import PontoTuristicoCard from "./components/PontoTuristicoCard"; // <--- Importe o componente
import styles from "./App.styles";

export default function App() {
  return (
    <ScrollView style={styles.scrollViewContainer}>
      {/* <--- Usando ScrollView */}
      <View style={styles.container}>
        <Text style={styles.mainTitle}>Conheça Curitiba!</Text>{" "}
        {/* <--- Título principal */}
        <PontoTuristicoCard
          nome="Jardim Botânico"
          descricao="Um dos mais famosos cartões-postais da cidade."
        />
        <PontoTuristicoCard
          nome="Ópera de Arame"
          descricao="Teatro com estrutura tubular e teto transparente, em meio à natureza."
        />
        <PontoTuristicoCard
          nome="Parque Tanguá"
          descricao="Antiga pedreira transformada em parque com cascata e mirante."
        />
        <PontoTuristicoCard
          nome="Museu Oscar Niemeyer"
          descricao="Conhecido como Museu do Olho, com arte moderna e contemporânea."
        />
        <StatusBar style="auto" />
      </View>
    </ScrollView>
  );
}
