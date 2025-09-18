## Componentes, Props e Estilização



### Título



Construindo a Interface: Componentes Reutilizáveis e Estilo com `props`



### Objetivos



  * Aprofundar o entendimento sobre **componentes** em React Native.

  * Aprender a utilizar e passar **props** para tornar componentes reutilizáveis.

  * Dominar a estilização com **`StyleSheet`** e propriedades de estilo comuns.

  * Introduzir o conceito de **Flexbox** para layout em React Native.

  * **BÔNUS:** Discussão sobre a modularização do código e a filosofia "componente-primeiro".



### Revisão Rápida



  * Como iniciamos um novo projeto Expo?

  * Qual a função do `View` e `Text` em um componente React Native?



### Conteúdo Teórico



  * **Componentes em Detalhe:**

      * Blocos de construção independentes e reutilizáveis da UI.

      * Função dos componentes: encapsular lógica e UI.

      * Componentes de função (Functional Components) vs. Componentes de classe (Class Components) - foco em Funções com Hooks.

  * **`Props` (Propriedades):**

      * Como dados são passados de um componente "pai" para um componente "filho".

      * Tornam os componentes genéricos e reutilizáveis.

      * São somente leitura (read-only): componentes filhos não devem modificar suas props diretamente.

      * Desestruturação de `props`.

  * **Estilização com `StyleSheet`:**

      * A forma recomendada de estilizar em React Native.

      * Permite criar estilos de forma eficiente e otimizada (como objetos JavaScript).

      * `StyleSheet.create()` para agrupar estilos e melhorar a legibilidade.

      * Estilização inline (menos recomendado para estilos complexos ou reutilizáveis).

  * **Fundamentos de Flexbox:**

      * O sistema de layout padrão no React Native (e web).

      * `flexDirection`: Define o eixo principal (row/column).

      * `justifyContent`: Alinha itens no eixo principal.

      * `alignItems`: Alinha itens no eixo cruzado.

      * `flex`: Controla como um item preenche o espaço disponível.

      * Adaptação para diferentes tamanhos de tela.



### Prática Laboratorial



-----



#### Slide: Passo 1: Organizar Pastas e Componentes



  * **Ação:** Vamos criar uma pasta `components/` para organizar nossos componentes reutilizáveis.



  * **Estrutura de Pastas:**



    ```

    guia-turistico-app/

    ├── App.js

    ├── components/         # <-- Nova pasta

    │   └── PontoTuristicoCard.js # <-- Novo arquivo

    ├── assets/

    └── package.json

    ```



  * **Explicação:**



      * Organizar o código em pastas lógicas ajuda a manter o projeto **escalável e fácil de navegar**.

      * `components/`: Contém componentes de UI que podem ser usados em várias telas.



-----



#### Passo 2: Criar o Primeiro Componente Reutilizável (`PontoTuristicoCard.js`)



  * **Ação:** Vamos criar um componente simples para exibir informações de um ponto turístico.



  * **Conteúdo de `components/PontoTuristicoCard.js`:**



    ```javascript

    // components/PontoTuristicoCard.js

    import React from 'react';

    import { View, Text, StyleSheet } from 'react-native'; // <--- Importe View, Text, StyleSheet



    // <--- O componente recebe 'props'

    const PontoTuristicoCard = (props) => {

      return (

        <View style={styles.card}>

          <Text style={styles.titulo}>{props.nome}</Text> {/* <--- Acessando props.nome */}

          <Text style={styles.descricao}>{props.descricao}</Text> {/* <--- Acessando props.descricao */}

        </View>

      );

    };



    const styles = StyleSheet.create({

      card: {

        backgroundColor: '#fff',

        padding: 15,

        marginVertical: 10,

        marginHorizontal: 20,

        borderRadius: 8,

        shadowColor: '#000',

        shadowOffset: { width: 0, height: 2 },

        shadowOpacity: 0.1,

        shadowRadius: 3.84,

        elevation: 5, // Sombra para Android

      },

      titulo: {

        fontSize: 20,

        fontWeight: 'bold',

        marginBottom: 5,

        color: '#333',

      },

      descricao: {

        fontSize: 14,

        color: '#666',

      },

    });



    export default PontoTuristicoCard; // <--- Exporte o componente

    ```



  * **Entendimento:**



      * O componente `PontoTuristicoCard` é uma **função React** que recebe um objeto `props` como argumento.

      * Usamos `props.nome` e `props.descricao` para acessar os dados passados a ele.

      * Definimos estilos específicos para o card usando `StyleSheet.create()`.



-----



#### Passo 3: Utilizar o Componente com `props` no `App.js`



  * **Ação:** Agora vamos importar e usar o `PontoTuristicoCard` em nosso `App.js`, passando diferentes `props` para ele.



  * **Mudança no `App.js`:**



    ```javascript

    // App.js

    import { StatusBar } from 'expo-status-bar';

    import { StyleSheet, Text, View, ScrollView } from 'react-native'; // <--- Importe ScrollView

    import PontoTuristicoCard from './components/PontoTuristicoCard'; // <--- Importe o componente



    export default function App() {

      return (

        <ScrollView style={styles.scrollViewContainer}> {/* <--- Usando ScrollView */}

          <View style={styles.container}>

            <Text style={styles.mainTitle}>Conheça Curitiba!</Text> {/* <--- Título principal */}

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



    const styles = StyleSheet.create({

      scrollViewContainer: { // Estilo para o ScrollView

        flex: 1,

        backgroundColor: '#f5f5f5',

      },

      container: {

        // Remova 'justifyContent: center' e 'alignItems: center'

        // para permitir que os cards se posicionem naturalmente.

        flex: 1,

        backgroundColor: '#f5f5f5', // Fundo claro para o app

        paddingTop: 50, // Espaço para a barra de status no topo

      },

      mainTitle: { // Novo estilo para o título principal

        fontSize: 28,

        fontWeight: 'bold',

        textAlign: 'center',

        marginBottom: 20,

        color: '#333',

      }

      // Outros estilos do card estão em PontoTuristicoCard.js

    });

    ```



  * **Observação:**



      * Usamos o componente `<ScrollView>` para que o conteúdo possa ser rolado se exceder a altura da tela.

      * Cada instância de `PontoTuristicoCard` recebe **diferentes `props` (`nome` e `descricao`)**, demonstrando a reutilização.

      * Ajustamos o estilo do `container` para que os cards se posicionem de forma mais natural (removendo `justifyContent` e `alignItems` centrais).



-----



#### Passo 4: Entendendo o Flexbox para Layout



  * **Ação:** Flexbox é essencial para organizar componentes na tela. Vamos entender as propriedades básicas.



  * **Exemplo de Flexbox:**



      * No `App.js`, no `styles.container`, já temos `flex: 1`.

      * Vamos adicionar um exemplo em um novo `View` temporário:



    <!-- end list -->



    ```javascript

    // App.js - Dentro do return da função App, APÓS a ScrollView

    {/* Exemplo de Flexbox para demonstração */}

    <View style={styles.flexboxExample}>

      <View style={styles.box}><Text>1</Text></View>

      <View style={[styles.box, { backgroundColor: 'orange' }]}><Text>2</Text></View>

      <View style={styles.box}><Text>3</Text></View>

    </View>



    // No StyleSheet.create, adicione:

    const styles = StyleSheet.create({

      // ... estilos existentes ...

      flexboxExample: {

        flexDirection: 'row', // <--- Itens lado a lado (por padrão é 'column')

        justifyContent: 'space-around', // <--- Espaça itens uniformemente

        alignItems: 'center', // <--- Centraliza itens verticalmente

        backgroundColor: '#e0e0e0',

        padding: 10,

        margin: 20,

        borderRadius: 8,

      },

      box: {

        width: 50,

        height: 50,

        backgroundColor: 'lightblue',

        justifyContent: 'center',

        alignItems: 'center',

        margin: 5,

        borderRadius: 5,

      }

    });

    ```



  * **Conceitos Chave do Flexbox:**



      * `flexDirection`: (`row`, `column`, `row-reverse`, `column-reverse`) - Define a direção do eixo principal.

      * `justifyContent`: (`flex-start`, `center`, `flex-end`, `space-around`, `space-between`, `space-evenly`) - Alinha itens ao longo do eixo principal.

      * `alignItems`: (`flex-start`, `center`, `flex-end`, `stretch`, `baseline`) - Alinha itens ao longo do eixo cruzado.

      * `flex`: Quando aplicado a um item, ele define como esse item cresce para preencher o espaço disponível. `flex: 1` significa que o item tenta preencher todo o espaço restante.



-----



### Desafio da Aula



  * No seu aplicativo "Guia Turístico":

      * Crie uma pasta `components/` na raiz do seu projeto.

      * Mova o `App.js` para ser um componente mais limpo e crie um componente `PontoTuristicoCard.js` (como no exemplo) que exiba `nome` e `descricao` como `props`.

      * No seu `App.js`, importe e utilize pelo menos **três instâncias** do `PontoTuristicoCard`, cada uma com informações diferentes de pontos turísticos (invente nomes e descrições).

      * Adicione um `<ScrollView>` para garantir que os cards sejam rolados se a lista for longa.

      * Experimente alterar as propriedades de `flexDirection`, `justifyContent` e `alignItems` no `styles.container` do `App.js` para observar o impacto no layout.

  * Faça **commits no Git** com as alterações.



### Próximos Passos

  * Na próxima aula, vamos explorar a navegação entre telas, permitindo que o usuário interaja e se mova pelo aplicativo.