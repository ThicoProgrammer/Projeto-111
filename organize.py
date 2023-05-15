import os
import shutil

origem = 'C:/Users/Thiago/origem/'
destino = 'C:/Users/Thiago/destino/'

lista_arquivos = os.listdir(origem)
# print(lista_arquivos)

for arquivo in lista_arquivos:
    raiz, extensao = os.path.splitext(arquivo)

    if extensao == '':
        continue
    if extensao in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:

        arquivo_na_origem = origem + arquivo
        pasta_destino = destino + 'Minhas imagens/'
        arquivo_no_destino = destino + 'Minhas imagens/' + arquivo

        if os.path.exists(pasta_destino):

            print('Movendo ' + arquivo)
            shutil.move(arquivo_na_origem, arquivo_no_destino)

        else:

            os.mkdir(pasta_destino)
            print('Movendo ' + arquivo)
            shutil.move(arquivo_na_origem, arquivo_no_destino)