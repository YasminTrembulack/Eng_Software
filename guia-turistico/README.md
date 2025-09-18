## Aula 1: Introdução ao Desenvolvimento Mobile

### Título

Primeiros Passos: Desvendando o Mundo Mobile com React Native

### Objetivos

  * Compreender o cenário atual do **desenvolvimento de aplicativos móveis**.
  * Entender o que é **React Native** e por que ele é uma escolha popular.
  * Conhecer o **ambiente de desenvolvimento** necessário (Node.js, Expo CLI).
  * Criar seu **primeiro projeto** React Native com Expo.
  * **BÔNUS:** Discussão sobre a importância da comunidade e documentação.

### Conteúdo Teórico

  * **O Crescimento do Mobile:**
      * Estatísticas de uso de smartphones.
      * A onipresença dos aplicativos no dia a dia.
      * Oportunidades de carreira no desenvolvimento mobile.
  * **Desenvolvimento Nativo vs. Híbrido/Multiplataforma:**
      * **Nativo:** Swift/Kotlin (performance máxima, específico para uma plataforma).
      * **Híbrido (WebViews):** Ionic, Cordova (desenvolvimento rápido, mas com limitações de performance/UI).
      * **Multiplataforma (Compilado para Nativo):** React Native, Flutter (código único, performance quase nativa).
  * **O que é React Native?**
      * Um framework JavaScript para construir apps móveis nativos.
      * Baseado na biblioteca React (para web).
      * Reutilização de código entre iOS e Android.
      * Hot Reloading e Fast Refresh para desenvolvimento ágil.
  * **Por que React Native?**
      * Produtividade (um código para duas plataformas).
      * Grande comunidade e ecossistema.
      * Componentes nativos para UI e performance.
      * Curva de aprendizado mais suave para devs web React.
  * **Introdução ao Expo:**
      * Uma ferramenta e plataforma que simplifica o desenvolvimento React Native.
      * Abstrai a complexidade do ambiente nativo.
      * `Expo Go` para testes rápidos em dispositivos reais.
      * `EAS Build` para gerar builds nativos.
  * **Componentes Básicos do React Native:**
      * `View`: O contêiner básico, como uma `div` no HTML.
      * `Text`: Para exibir texto.
      * `StyleSheet`: Para estilizar componentes (CSS-like).
      * `Image`: Para exibir imagens.
      * `Button`: Para interações de clique.

### Prática Laboratorial

-----

#### Passo 1: Instalar Node.js e Expo CLI

  * **Ação:** Para começar, precisamos do Node.js (que inclui o npm) e da ferramenta de linha de comando do Expo.

  * **Comando:**

    1.  **Instale Node.js:** Baixe e instale a versão LTS de [nodejs.org](https://nodejs.org/).
    2.  **Instale Expo CLI:** Abra seu terminal ou prompt de comando e execute:

    <!-- end list -->

    ```bash
    npm install -g expo-cli
    ```
    **ps.1:** Em alguns casos, por uma questão de segurança, o Windows vai bloquear execução de scripts. Quando isso ocorrer, execute o Powershell do Windows em modo administrador e digite o seguinte comando:
    ```bash
    set-ExecutionPolicy unrestricted
    ```
    ![PowerShell](./ps2.png)

    **ps.2:** Uma alternativa para rodar o app em Android sem um dispositivo físico é executá-lo em um emulador. Neste caso, será preciso apenas executar o terminal do vscode e rodar o seguinte comando:
    ```bash
     C:\Users\User\AppData\Local\Android\Sdk\tools\emulator -list-avds
    ```
    Isso fará surgir a lista de emuladores previamente instalados na máquina. Em seguida, basta executar o emulador desejado, com o comando:
    ```bash
     C:\Users\User\AppData\Local\Android\Sdk\tools\emulator -avd <nome_do_emulador>
    ```

  * **Explicação:**

      * `Node.js`: É o ambiente de execução JavaScript que permite rodar o React Native fora do navegador. `npm` (Node Package Manager) vem junto com ele e é usado para instalar bibliotecas.
      * `expo-cli`: É a ferramenta de linha de comando do Expo que nos ajuda a criar, desenvolver e gerenciar projetos React Native.

    ```bash
    added 1282 packages in 55s
    185 packages are looking for funding
      run `npm fund` for details
    npm notice
    npm notice New major version of npm available! 10.2.4 -> 11.5.1
    npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.5.1
    npm notice Run npm install -g npm@11.5.1 to update!
    npm notice
    ```

-----

#### Passo 2: Criar Seu Primeiro Projeto Expo

  * **Ação:** Agora, vamos criar um novo projeto React Native usando o Expo CLI.

  * **Comando:** No terminal, navegue até a pasta onde deseja criar seu projeto e execute:

    ```bash
    expo init meu-primeiro-app-guia
    # ou npx create-expo-app meu-primeiro-app-guia
    ```

      * **Escolha a opção:** `blank (TypeScript)` ou `blank (JavaScript)` (para este curso, JavaScript é suficiente).
      * **Navegue para a pasta do projeto:**

    <!-- end list -->

    ```bash
    cd meu-primeiro-app-guia
    ```

  * **Explicação:**

      * `expo init`: Inicializa um novo projeto Expo.
      * `meu-primeiro-app-guia`: É o nome da pasta e do seu projeto.
      * `blank`: Cria um projeto mínimo, sem configurações adicionais.

-----

#### Passo 3: Rodar o Aplicativo pela Primeira Vez

  * **Ação:** É hora de ver seu aplicativo em ação\!

  * **Comando:** Dentro da pasta do seu projeto (`meu-primeiro-app-guia`), execute:

    ```bash
    npm start
    # ou expo start
    ```

  * **Explicação:**

      * Este comando inicia o **Metro Bundler**, que compila seu código JavaScript.
      * Um **QR Code** aparecerá no terminal.
      * **No seu celular:** Baixe o aplicativo **Expo Go** (disponível na Google Play Store e Apple App Store). Abra o Expo Go e escaneie o QR Code.
      * **No emulador/simulador:** Pressione `a` (para Android) ou `i` (para iOS) no terminal para abrir o app em um emulador/simulador (se você tiver um configurado).

-----

#### Passo 4: Entendendo a Estrutura Básica (`App.js`)

  * **Ação:** Vamos olhar o arquivo principal do seu projeto, `App.js`.

  * **Conteúdo Inicial de `App.js`:**

    ```javascript
    // App.js
    import { StatusBar } from 'expo-status-bar';
    import { StyleSheet, Text, View } from 'react-native';

    export default function App() {
      return (
        <View style={styles.container}>
          <Text>Open up App.js to start working on your app!</Text>
          <StatusBar style="auto" />
        </View>
      );
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
      },
    });
    ```

  * **Entendimento:**

      * `import { ... } from 'react-native';`: Importa componentes básicos do React Native.
      * `export default function App() { ... }`: Define o componente principal do seu aplicativo.
      * `View`: Um contêiner flexível para outros componentes.
      * `Text`: Componente para exibir texto.
      * `StyleSheet.create({ ... })`: Usado para criar estilos de forma otimizada e legível.
      * `StatusBar`: Componente do Expo para controlar a barra de status do celular.

-----

#### Passo 5: Fazendo Sua Primeira Alteração

  * **Ação:** Altere o texto no `App.js` e veja o Hot Reload em ação.

  * **Mudança no `App.js`:**

    ```javascript
    // App.js
    import { StatusBar } from 'expo-status-bar';
    import { StyleSheet, Text, View } from 'react-native';

    export default function App() {
      return (
        <View style={styles.container}>
          <Text>Olá, Mundo! Meu Primeiro App Guia Turístico!</Text> {/* <--- Texto Alterado */}
          <StatusBar style="auto" />
        </View>
      );
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
      },
    });
    ```

  * **Observação:** Salve o arquivo (`Ctrl+S` ou `Cmd+S`). Você verá a mudança instantaneamente no seu celular ou emulador, sem precisar recarregar o app manualmente. Isso é o **Hot Reload** ou **Fast Refresh**\!

-----

### Desafio da Aula

  * Crie seu primeiro projeto Expo com o nome `guia-turistico-app`.
  * Rode o aplicativo no seu celular (usando Expo Go) ou emulador.
  * Altere o texto inicial do `App.js` para uma mensagem personalizada de boas-vindas ao seu "Guia Turístico".
  * Explore a estrutura de pastas básica que o Expo cria.
  * **Extra:** Tente adicionar um segundo componente `Text` com seu nome.
  * Faça **commits no Git** com as alterações iniciais do projeto.

### Próximos Passos

  * Na próxima aula, vamos aprofundar na criação de componentes, uso de `props` e estilização com `StyleSheet`.