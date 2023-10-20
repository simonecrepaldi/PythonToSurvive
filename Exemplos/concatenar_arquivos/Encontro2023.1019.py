# Exercício 1: Concatenando Arquivos de Texto
# Crie dois arquivos de texto, "arquivo1.txt" e "arquivo2.txt", com algum conteúdo.
# Em seguida, crie um programa que os abre, lê seus conteúdos e concatena o conteúdo dos dois arquivos em um terceiro arquivo chamado "arquivo_concatenado.txt".

# def ler_arquivo(arquivo: object) -> object:
#     with open(arquivo, encoding="utf8") as file:
#         conteudo = file.read()
#         print(conteudo)
#         return conteudo
#
#
# def inicio():
#     texto1 = ler_arquivo("textos\arquivo1.txt")
#     texto2 = ler_arquivo("textos\arquivo2.txt")


    texto1 = open("textos\arquivo1.txt")
    texto2 = open("textos\arquivo2.txt")

    conteudo1 = texto1.readlines()
    print(conteudo1)