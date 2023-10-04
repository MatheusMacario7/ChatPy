import socket
import threading

# Configurações do servidor
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080 

# Cria um socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Dicionário para armazenar as conexões dos clientes e seus nomes
clients = {}

def remove_client(client_socket):
    if client_socket in clients:
        client_name = clients[client_socket]
        print(f"Cliente {client_name} saiu do chat.")
        del clients[client_socket]


def handle_client(client_socket, client_name):
    while True:
        try:
            # Recebe a mensagem do cliente
            data = client_socket.recv(1024)
            if not data:
                break

                
            if data.decode("utf-8") == '/quit':
                remove_client(client_socket)

               
           # Verifica se o cliente deseja iniciar uma conversa privada
            if data.decode("utf-8").startswith("/private"):
                parts = data.decode("utf-8")[8:].split(":", 1)
                if len(parts) == 2:
                    recipient_name = parts[0]
                    message = parts[1]
                    send_private_message(client_name, recipient_name, message)
                else:
                    client_socket.send("Uso correto: /private<destinatário>:<mensagem>".encode("utf-8"))
            else:
                # Transmite a mensagem para todos os outros clientes na sala
                send_group_message(client_name, data.decode("utf-8"))  # Decodifica os dados recebidos

        except Exception as e:
            print(f"Erro: {e}")
            break


def send_group_message(sender_name, message):
    # Transmite a mensagem para todos os clientes na sala
    for client_socket, client_name in clients.items():
        if client_name != sender_name:
            
            client_socket.send(f"{sender_name}: {message}".encode("utf-8")) if message != " /quit " else  client_socket.send(f"{sender_name} saiu do chat".encode("utf-8"))
        #else:
            #print(f"{sender_name} saiu do chat.")

def send_private_message(sender_name, recipient_name, message):
    # Envia uma mensagem privada para o destinatário
    recipient_socket = None
    for client_socket, client_name in clients.items():
        if client_name.lower().strip() == recipient_name.lower().strip():
            recipient_socket = client_socket
            break

    if recipient_socket:
        recipient_socket.send(f"[Mensagem Privada de {sender_name}]: {message}".encode("utf-8"))
    else:
        sender_socket = [socket for socket, name in clients.items() if name == sender_name][0]
        sender_socket.send(f"Destinatário '{recipient_name}' não encontrado.".encode("utf-8"))

def main():
    server.listen(5)
    print(f"Servidor escutando em {HOST} : {PORT}")
    print("AGUARDANDO CONEXÃO...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Cliente conectado: {client_address}")

        # Solicita ao cliente que informe seu nome
        client_name = client_socket.recv(1024).decode("utf-8")
        print(f"Cliente {client_name} conectado.")

        # Adiciona o cliente ao dicionário de clientes
        clients[client_socket] = client_name

        # Inicia uma thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_name))
        client_handler.start()

if __name__ == "__main__":
    main()