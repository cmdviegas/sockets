# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Cliente UDP modificado para enviar texto minusculo ao servidor e aguardar resposta convertida em maiuscula

# Como executar: 
# >_ python3 clientUDP.py
# ou
# >_ python3 clientUDP.py IP_DO_SERVIDOR

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
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Permite reusar a porta caso fique "presa" por algum processo que nao foi encerrado corretamente
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:
    # Solicita ao usuario uma frase
    message = input('Digite o texto em letras minusculas: ')
    # Envia a mensagem para o servidor (IP, porta)
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    # Aguarda resposta do servidor (max. 2048 bytes)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # Mostra a resposta recebida
    print(f"O servidor ('{serverName}', {serverPort}) respondeu com: {modifiedMessage.decode('utf-8')}")

except KeyboardInterrupt:
    print("\nCliente encerrado pelo usuario (Ctrl+C).")
except Exception as e:
    print(f"Erro durante a comunicacao UDP: {e}")
finally:
    # Fecha o socket de forma limpa
    clientSocket.close()

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
