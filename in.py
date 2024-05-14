import os

def recuperar_arquivos():
    arquivos = os.listdir()
    arquivos = list(filter(lambda arquivo: os.path.isfile(arquivo),arquivos))
    return arquivos

def recuperar_extensoes(arquivos):
    extensoes = [arquivo.split('.')[1] for arquivo in arquivos if '.' in arquivo and '.py' not in arquivo]
    extensoes = list(set(extensoes))
    return extensoes

def criar_pastas(extensoes):
    for extensao in extensoes:
        os.mkdir(extensao)

def mover_arquivo(arquivo, extensao):
    path = os.getcwd()
    path_arquivo = os.path.join(path, arquivo)
    new_path = os.path.join(path, extensao, arquivo)
    os.rename(path_arquivo, new_path)

def mover_arquivos(arquivos, extensoes):
    for arquivo in arquivos:
        for extensao in extensoes:
            if extensao == arquivo.split('.')[1]:
                mover_arquivo(arquivo, extensao)
                break

def main():
    arquivos = recuperar_arquivos()
    extensoes = recuperar_extensoes(arquivos)
    criar_pastas(extensoes)
    mover_arquivos(arquivos, extensoes)

main()