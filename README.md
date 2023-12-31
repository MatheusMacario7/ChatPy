# Projeto de Redes de Computadores - Desenvolvimento de um Chat em Python

Este é um chat simples desenvolvido em Python que permite a comunicação entre clientes e um servidor. Ele oferece funcionalidades básicas de chat em grupo e mensagens privadas. Este projeto foi criado como parte da disciplina de Redes de Computadores da Universidade Federal de Alagoas (UFAL) e teve como participantes os seguintes estudantes:

**- Gabriel Vitorino de Andrade**

**- Maria Eduarda Cardoso Aciole**

**- Matheus Macário dos Santos**

**- Rafael Ramos Pimentel Santana**

**- Rômulo José Araújo Rodrigues Siqueira**

Aqui estão as principais funcionalidades do servidor e do cliente, juntamente com instruções sobre como utilizar o chat:

## Funcionalidades Principais

### Servidor (server.py)

O servidor é responsável por gerenciar as conexões dos clientes e facilitar a comunicação entre eles. Aqui estão as principais funcionalidades do servidor:

1. **Conexão e Gerenciamento de Clientes:**
   - O servidor cria um socket TCP e aguarda conexões de clientes na porta especificada (8080 por padrão).
   - Cada cliente é associado a um nome que eles fornecem ao se conectar.

2. **Mensagens em Grupo:**
   - Os clientes podem enviar mensagens para todos os outros clientes conectados.
   - Para enviar uma mensagem, basta digitar o texto e pressionar Enter.

3. **Mensagens Privadas:**
   - Os clientes podem iniciar conversas privadas com outros clientes usando o comando `/private<destinatário>:<mensagem>`.
   - Exemplo: `/privateJoão:Oi João, como você está?`

4. **Sair do Chat:**
   - Os clientes podem sair do chat digitando `/quit`. Isso encerra a conexão com o servidor e remove o cliente da lista de participantes.

### Cliente (client.py)

O cliente é responsável por se conectar ao servidor e permitir que os usuários enviem e recebam mensagens. Aqui estão as principais funcionalidades do cliente:

1. **Conexão ao Servidor:**
   - O cliente solicita ao usuário o endereço IP do servidor ao qual deseja se conectar.
   - O cliente também solicita ao usuário que forneça um nome para identificação no chat.

2. **Recebimento de Mensagens:**
   - O cliente cria uma thread para receber mensagens do servidor em segundo plano.
   - Ele exibe as mensagens recebidas na tela, permitindo que o usuário as leia.

3. **Envio de Mensagens:**
   - O usuário pode digitar mensagens e enviá-las para o servidor.
   - As mensagens são transmitidas para todos os clientes conectados ou para um destinatário específico, se for uma mensagem privada.

4. **Sair do Chat:**
   - O usuário pode sair do chat digitando `/quit`. Isso fecha a conexão com o servidor e encerra o programa do cliente.

## Como Utilizar o Chat

1. **Iniciar o Servidor:**
   - Execute o arquivo `server.py` para iniciar o servidor.
   - O servidor irá aguardar conexões de clientes na porta 8080.

2. **Conectar Clientes:**
   - Execute o arquivo `client.py` em cada máquina/cliente.
   - Fornecer o endereço IP do servidor quando solicitado.
   - Escolher um nome de usuário para identificação no chat.

3. **Enviar Mensagens:**
   - Os clientes podem digitar mensagens e pressionar Enter para enviá-las.
   - Use `/private<destinatário>:<mensagem>` para enviar mensagens privadas.
   - Use `/quit` para sair do chat.

4. **Receber Mensagens:**
   - As mensagens dos outros clientes serão exibidas na tela do cliente atual.

5. **Sair do Chat:**
   - Para sair, digite `/quit` no cliente.
   - O servidor também exibe quando um cliente sai do chat.

**OBS:**
Certifique-se de que o servidor esteja em execução antes de iniciar os clientes. Você pode usar esse chat para se comunicar com outros clientes conectados ao mesmo servidor.


