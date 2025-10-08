# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Servidor UDP modificado para receber do cliente um texto minusculo e enviar resposta convertida em maiuscula

# Como executar: 
# >_ python3 serverUDP.py

# Disclamer/aviso:
# Este codigo foi desenvolvido unicamente para fins didaticos.
# O uso deste codigo e estritamente educacional e experimental, nao devendo ser empregado em ambientes com fins comerciais.

# --- INICIO DA LOGICA DE CODIGO ---

# Importacao das bibliotecas
from socket import *    # socket

# Definicao das variaveis
serverName = ''          # IP do servidor (em branco = qualquer IP)
serverPort = 61000       # porta do servidor (numero maior que 1024)
# Criacao do socket TCP (SOCK_STREAM = TCP / SOCK_DGRAM = UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Permite reusar a porta caso fique "presa" por algum processo que nao foi encerrado corretamente
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Associacao (bind) do socket com o IP e a porta
serverSocket.bind((serverName, serverPort))

try:
    print(f"Servidor UDP esperando conexoes na porta {serverPort} ...")
    # Loop principal do servidor (so encerra com Ctrl+C)
    while True: 
        # Recebe mensagem e endereco do cliente
        message, clientAddress = serverSocket.recvfrom(2048)     
        # Processa a mensagem e converte para maiusculas
        modifiedMessage = message.decode('utf-8').upper()
        # Mostra o que foi recebido e o que sera enviado
        print(f"Cliente {clientAddress} enviou: {message} -> {modifiedMessage}")
        # Envia resposta ao cliente
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
except KeyboardInterrupt:
    print("\nEncerrando servidor (Ctrl+C pressionado)...")
finally:
    # Fecha o socket do servidor de forma limpa
    serverSocket.close()

# --- FIM DA LOGICA DE CODIGO ---

# ================================================================
# METODOS USADOS EM SOCKETS UDP (CLIENTE E SERVIDOR)
# ================================================================

# UDP NAO E ORIENTADO A CONEXAO, NAO HA O CICLO: connect -> comunicacao -> close

# Servidor UDP
# ---------------------------
# socket()              -> cria o socket (AF_INET, SOCK_DGRAM)
# bind()                -> associa o socket ao IP e porta
# recvfrom()            -> recebe dados e o endereco do cliente
# sendto()              -> envia resposta para o cliente
# close()               -> encerra o socket

# Cliente UDP
# ---------------------------
# socket()              -> cria o socket (AF_INET, SOCK_DGRAM)
# sendto()              -> envia dados para (IP, porta)
# recvfrom()            -> recebe resposta do servidor
# close()               -> encerra o socket
# ================================================================
