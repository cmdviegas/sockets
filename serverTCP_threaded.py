# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Servidor TCP multithread para receber conexoes simultaneas de clientes

# Como executar: 
# >_ python3 serverTCP_threaded.py

# --- INICIO DA LOGICA DE CODIGO ---

# Importacao das bibliotecas
from socket import *    # socket
import threading        # threading

# Funcao para tratar conexoes dos clientes em threads separadas
# Cada cliente sera atendido por uma thread diferente e executara esta funcao
def handle_connection(client_socket, client_address):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Cliente {client_address} enviou: {data}")
    except Exception as e:
        print(f"Erro ao tratar cliente {client_address}: {e}")
    finally:
        client_socket.close()

# Definicao das variaveis
serverName = '0.0.0.0'  # IP do servidor (0.0.0.0 = escuta em todas as interfaces)
serverPort = 61000      # porta do servidor (numero maior que 1024)
# Criacao do socket TCP (SOCK_STREAM = TCP / SOCK_DGRAM = UDP)
serverSocket = socket(AF_INET, SOCK_STREAM)
# Permite reusar a porta caso fique "presa" por algum processo que nao foi encerrado corretamente
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Associacao (bind) do socket com o IP e a porta
serverSocket.bind((serverName, serverPort))
# Coloca o socket em modo de escuta (fila de conexoes pendentes = 5)
serverSocket.listen(5)

try:
    print(f"Servidor TCP multithread esperando conexoes na porta {serverPort} ...")
    # Loop principal do servidor (so encerra com Ctrl+C)
    while True:
        # Aguarda novas conexoes de clientes
        connectionSocket, addr = serverSocket.accept()
        print(f"Nova conexao recebida de {addr}")
        # Cria uma thread para atender o cliente
        thread = threading.Thread(target=handle_connection, args=(connectionSocket, addr)) # Define a funcao e os argumentos
        thread.start() # Inicia a thread
except KeyboardInterrupt:
    print("\nEncerrando servidor (Ctrl+C pressionado)...")
finally:
    # Fecha o socket do servidor de forma limpa
    serverSocket.close()

# --- FIM DA LOGICA DE CODIGO ---