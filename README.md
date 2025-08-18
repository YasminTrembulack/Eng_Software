1. Ambientes virtuais
Para evitar conflito de pacotes, é recomendado usar ambientes virtuais:
`python -m venv venv`

Ative o ambiente virtual:
`.\venv\Scripts\activate`

Para desativar digite:
`deactivate`


2. Instalando pacotes individualmente

No Prompt de Comando ou PowerShell, você usa o comando:
`pip install nome_do_pacote`


3. Instalando pacotes a partir do requirements.txt

O requirements.txt é um arquivo que lista todos os pacotes que seu projeto precisa. Ele é muito usado para compartilhar dependências.
Se você recebeu ou já tem um requirements.txt, basta executar:
`pip install -r requirements.txt`
