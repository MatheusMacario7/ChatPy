import socket
import threading

# Configurações do cliente
HOST = input("Digite o endereço de IP fornecido pelo servidor: ")
PORT = 8080

# Lista para acompanhar os nomes dos clientes conectados
connected_clients = []

# Variável para verificar se o usuário está conectado
user_connected = True

def receive_messages(client_socket):
    global user_connected
    while user_connected:
        try:
            # Recebe mensagens do servidor e imprime na tela
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(message)
            # Verifica se a mensagem é para desconectar o cliente
            if message == "/quit":
                user_connected = False
                print("Você saiu do chat.")
                break

            
        except Exception as e:
            print(f"Erro: {e}")
            break

def main():
    global user_connected
    # Cria um socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta-se ao servidor
    client_socket.connect((HOST, PORT))

    # Solicita ao usuário que informe seu nome
    print()
    user_name = input("Digite seu nome-> ")
    print("======================================")
    print(f"Bem-vindo(a) ao chat {user_name}!")
    print("======================================")
    # Envia o nome do usuário ao servidor
    client_socket.send(user_name.encode("utf-8"))

    # Adicione o nome do usuário à lista de clientes conectados
    connected_clients.append(user_name)

    # Inicia uma thread para receber mensagens do servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while user_connected:
        try:
            # Envia mensagens para o servidor
            message = input()
            client_socket.send(message.encode("utf-8"))

            # Verifica se o usuário deseja sair
            if message == "/quit":
                user_connected = False
                print("Você saiu do chat.")
                break

        except Exception as e:
            print(f"Erro: {e}")
            break

    # Fecha a conexão do cliente
    client_socket.close()

if __name__ == "__main__":
    main()