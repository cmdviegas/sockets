# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Servidor TCP modificado para receber do cliente um texto minusculo e enviar resposta convertida em maiuscula

# Como executar: 
# >_ python3 serverTCP.py

# Disclamer/aviso:
# Este codigo foi desenvolvido unicamente para fins didaticos.
# O uso deste codigo e estritamente educacional e experimental, nao devendo ser empregado em ambientes com fins comerciais.

# --- INICIO DA LOGICA DE CODIGO ---

# Importacao das bibliotecas
from socket import *    # socket

# Definicao das variaveis
serverName = '0.0.0.0'  # IP do servidor
serverPort = 61000      # porta do servidor

# Criacao do socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Permite reusar a porta caso fique "presa"
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Associacao do socket com o IP e a porta
serverSocket.bind((serverName, serverPort))

# Coloca o socket em modo de espera por conexoes
serverSocket.listen(1)

try:
    print(f"Servidor TCP esperando conexoes na porta {serverPort} ...")

    # Loop principal do servidor
    while True:
        # Aceita uma conexao do cliente
        connectionSocket, addr = serverSocket.accept()
        print(f"Cliente conectado: {addr}")

        try:
            # Loop para manter o cliente conectado
            while True:
                # Recebe dados do cliente
                data = connectionSocket.recv(1024)

                # Se recv retornar vazio, o cliente fechou a conexao
                if not data:
                    print(f"Cliente {addr} desconectou.")
                    break

                # Decodifica a mensagem recebida
                sentence = data.decode('utf-8')

                # Mostra a mensagem recebida no servidor
                print(f"Cliente {addr} enviou: {sentence}")

                # Nao envia nada de volta para o cliente

        except Exception as e:
            print(f"Erro ao tratar cliente {addr}: {e}")

        finally:
            # Fecha conexao somente quando o cliente desconectar
            connectionSocket.close()
            print(f"Conexao com {addr} fechada.")

except KeyboardInterrupt:
    print("\nEncerrando servidor (Ctrl+C pressionado)...")

finally:
    # Fecha o socket do servidor de forma limpa
    serverSocket.close()
    print("Socket do servidor fechado.")

# --- FIM DA LOGICA DE CODIGO ---

# ================================================================
# METODOS USADOS EM SOCKETS TCP (CLIENTE E SERVIDOR)
# ================================================================

# TCP E ORIENTADO A CONEXAO, PORTANTO HA O CICLO: connect -> comunicacao -> close

# Servidor TCP
# ---------------------------
# socket()              -> cria o socket (AF_INET, SOCK_STREAM)
# setsockopt()          -> define opcoes (ex: SO_REUSEADDR)
# bind()                -> associa o socket ao IP e porta
# listen()              -> coloca o socket em modo passivo (aguardando conexoes)
# accept()              -> aceita uma conexao (bloqueia ate um cliente conectar)
# recv() / send()       -> recebe e envia dados pela conexao estabelecida
# close()               -> fecha o socket (do cliente ou do servidor)

# Cliente TCP
# ---------------------------
# socket()              -> cria o socket (AF_INET, SOCK_STREAM)
# connect()             -> conecta ao servidor (IP, porta)
# send() / recv()       -> envia e recebe dados
# close()               -> encerra o socket