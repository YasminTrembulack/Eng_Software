import { View, Text } from "react-native"; // <--- Importe View, Text
import styles from "./PontoTuristicoCard.styles";

// <--- O componente recebe 'props'

const PontoTuristicoCard = (props) => {
  return (
    <View style={styles.card}>
      <Text style={styles.titulo}>{props.nome}</Text>
      <Text style={styles.descricao}>{props.descricao}</Text>
    </View>
  );
};



export default PontoTuristicoCard; // <--- Exporte o componente
