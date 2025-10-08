# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# REDES DE COMPUTADORES (DCA3605)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# Descricao: 
# Servidor HTTP simples que atende requisicoes GET de clientes

# Como executar:
# >_ python3 serverHTTP.py

# Disclamer/aviso:
# Este codigo foi desenvolvido unicamente para fins didaticos.
# O uso deste codigo e estritamente educacional e experimental, nao devendo ser empregado em ambientes com fins comerciais.

# --- INICIO DA LOGICA DE CODIGO ---

# Importacao das bibliotecas
from socket import *    # socket

# Definicao das variaveis
serverName = '0.0.0.0'  # IP do servidor (0.0.0.0 = escuta em todas as interfaces)
serverPort = 8081       # porta do servidor
# Criacao do socket TCP 
serverSocket = socket(AF_INET, SOCK_STREAM)
# Permite reusar o endereco e a porta caso o processo anterior nao tenha encerrado corretamente
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Associacao (bind) do socket com o IP e a porta
serverSocket.bind((serverName, serverPort))
# Coloca o socket em modo de espera por conexoes (5 conexao de espera no maximo)
serverSocket.listen(5)

try:
    print(f"Servidor TCP esperando conexoes na porta {serverPort} ...")
    # Loop principal do servidor (so encerra com Ctrl+C)
    while True:
        try:
            # Aguarda por novas conexoes
            connectionSocket, addr = serverSocket.accept()
            # Recebe dados enviados pelo cliente
            request = connectionSocket.recv(1024)
            if not request:
                # Nenhum dado recebido (cliente desconectou abruptamente)
                connectionSocket.close()
                continue
            # Exibe a requisicao HTTP no console
            print(f"Requisicao de {addr}: \n{request.decode('utf-8')}\n")

            # Resposta HTTP enviada ao cliente apos uma requisicao GET
            http_response = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head><title>Servidor HTTP Simples</title></head>
<body>
<h2>Servidor HTTP em Python (UFRN - DCA3605)</h2>
<p>Conexao estabelecida com sucesso!</p>
</body>
</html>
"""
            # Envia a resposta ao cliente
            connectionSocket.sendall(http_response.encode('utf-8')) # Usa sendall para garantir que todos os dados sejam enviados
        except ConnectionResetError:
            print("Conexao encerrada abruptamente por um cliente.")
        except Exception as e:
            print(f"Erro ao atender requisicao: {e}")
        finally:
            # Fecha sempre a conexao com o cliente
            connectionSocket.close()
except OSError as e:
    print(f"Erro ao iniciar servidor na porta {serverPort}: {e}")
except KeyboardInterrupt:
    print("\nEncerrando servidor (Ctrl+C pressionado)...")
finally:
    # Fecha o socket do servidor de forma limpa
    connectionSocket.close()

# ================================================================
# EXPLICACAO SOBRE CODIGOS DE RESPOSTA HTTP
# ================================================================
# Toda resposta HTTP deve comecar com uma "linha de status",
# que indica o resultado do processamento da requisicao.
#
# Essa linha e enviada antes do conteudo (HTML, texto, imagem etc.)
# e segue o formato:
#
#   HTTP/versao  codigo  mensagem
#
# Exemplos mais comuns:
#   HTTP/1.1 200 OK          -> Resposta bem-sucedida; conteudo sera retornado.
#   HTTP/1.1 404 NOT FOUND   -> O recurso solicitado nao foi encontrado.
#   HTTP/1.1 400 BAD REQUEST -> A requisicao enviada pelo cliente e invalida.
#
# O cliente (como um navegador) utiliza esse codigo para entender
# se a resposta foi bem-sucedida, se houve erro ou se o conteudo
# solicitado nao existe.
# ================================================================
