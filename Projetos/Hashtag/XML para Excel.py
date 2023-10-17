# Link do projeto - https://www.youtube.com/watch?v=KmrNYmv6GHU

# xmltodict - Biblioteca que faz a leitura do arquivo XML e transforma em um dicionário Python
# os - Bibioteca que permite manusear arquivos, ler arquivos que estão dentro de pastas
# print(lista_arquivos) - Mostra os nomes dos arquivos que temos na pasta "nfs": ['NFe1.xml', 'NFe2.xml', 'NFe3.xml']
# with open(nomedoarquivo, "r") - Abre o arquivo em modo leitura (r), se o arquivo não estiver na mesma pasta do código, precisa passar o caminho
# Obs: o "r" vai ler o arquivo no formato string e se rodarmos o código ele vai dar erro: TypeError: read() did not return a bytes object (type=str)
# Pra corrigiri isso usamos "rb"
#Usando o "json.dumps" conseguimos formatar o dicionário tornando a leitura dele mais agradável

import xmltodict
import os
import json
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    #print(f"- Obtendo as informações do arquivo {nome_arquivo} -")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dic_arquivo, indent=4))
        #try:                                           #Ao rodar o código só funcionou pra NFe1, então colocamos o "try". Primeiro ele vai tentar fazer esse bloco e, se não conseguir, vai pro "except"
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]['infNFe']
        else:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]['xNome']
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"
        #print(numero_nota, empresa_emissora, nome_cliente, endereco, peso, sep="\n")
        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        # except Exception as e:      #Aqui pedimos pra ele salvar o erro em "e" e nos mostrar onde está o problema
        #     print(e)
        #     print(json.dumps(dic_arquivo, indent=4))


lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
valores = []

for arquivo in lista_arquivos:  #Para cada arquivo dentro da pasta, vamos pegar as informações através da função pegar_infos
    pegar_infos(arquivo, valores)
    #break

tabela = pd.DataFrame(columns=colunas, data=valores)
print(tabela)

tabela.to_excel("NotasFiscais.xlsx", index=False)
