# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Cliente TCP modificado para enviar texto minusculo ao servidor e aguardar resposta convertida em maiuscula

# Como executar: 
# >_ python3 clientTCP.py
# ou
# >_ python3 clientTCP.py IP_DO_SERVIDOR

# Disclamer/aviso:
# Este codigo foi desenvolvido unicamente para fins didaticos.
# O uso deste codigo e estritamente educacional e experimental, nao devendo ser empregado em ambientes com fins comerciais.

# --- INICIO DA LOGICA DE CODIGO ---

# Importacao das bibliotecas
from socket import *    # socket
import sys              # sys (para argumentos na linha de comando)

# Definicao das variaveis
serverName = 'localhost'    # IP do servidor (localhost = este computador)
serverPort = 61000          # porta do servidor (numero maior que 1024)
# Se um IP for passado como argumento, ele substitui o valor padrao
if len(sys.argv) > 1:
    serverName = sys.argv[1]
# Criacao do socket TCP (SOCK_STREAM = TCP / SOCK_DGRAM = UDP)
clientSocket = socket(AF_INET, SOCK_STREAM)  
# Permite reusar a porta caso fique "presa" por algum processo que nao foi encerrado corretamente
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:
    # Conecta ao servidor
    clientSocket.connect((serverName, serverPort))
    # Solicita ao usuario que digite uma frase em minusculas
    sentence = input('Digite o texto em letras minusculas: ')
    # Envia a frase para o servidor
    clientSocket.send(sentence.encode('utf-8'))
    # Recebe a resposta do servidor
    modifiedSentence = clientSocket.recv(1024).decode('utf-8')
    # Mostra a resposta do servidor
    print(f"O servidor ('{serverName}', {serverPort}) respondeu com: {modifiedSentence}")
except KeyboardInterrupt:
    print("\nCliente encerrado pelo usuario (Ctrl+C).")
except ConnectionRefusedError:
    print(f"Nao foi possivel conectar ao servidor em {serverName}:{serverPort}.")
except Exception as e:
    print(f"Erro durante a comunicacao: {e}")
finally:
    clientSocket.close()

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