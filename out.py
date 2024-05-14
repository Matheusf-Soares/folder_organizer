import os

def recuperar_pastas():
    arquivos = os.listdir()
    pastas = list(filter(lambda arquivo: os.path.isdir(arquivo), arquivos))
    return pastas

def recuperar_arquivos(pasta):
    path = os.path.join(os.getcwd(), pasta)
    arquivos = os.listdir(path)
    arquivos = list(filter(lambda arquivo: os.path.isfile(os.path.join(path, arquivo)), arquivos))
    return arquivos

def retirar_arquivo(pasta, arquivo):
    path = os.getcwd()
    path_pasta = os.path.join(path, pasta, arquivo)
    new_path = os.path.join(path, arquivo)
    os.rename(path_pasta, new_path)

def retirar_arquivos(pasta, arquivos):
    for arquivo in arquivos:
        retirar_arquivo(pasta, arquivo)

def retirar_arquivos_das_pastas(pastas):
    for pasta in pastas:
        arquivos = recuperar_arquivos(pasta)
        retirar_arquivos(pasta, arquivos)

def deletar_pastas(pastas):
    for pasta in pastas:
        os.rmdir(pasta)

def main():
    pastas = recuperar_pastas()
    retirar_arquivos_das_pastas(pastas)
    deletar_pastas(pastas)

main()
