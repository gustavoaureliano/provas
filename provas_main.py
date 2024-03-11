import provas as p

def ler_arquivo(filename):
    arquivo = []
    try:
        file = open(filename, 'r')
        arquivo = file.read().splitlines();
    except:
        print("Arquivo não encontrado")
    return arquivo

def main():
    while True:
        filename = input("Arquivo gabarito: ")
        arquivo = p.ler_arquivo(filename)
        if arquivo:
            gabarito = arquivo
            break
    while True:
        filename = input("Argquivo prova: ")
        arquivo = p.ler_arquivo(filename)
        if arquivo:
            prova = arquivo
            break
    print(gabarito)
    print(prova)
    resultados = p.corrigir(gabarito, prova)
    print(p.mostrar_resultados(resultados))



if __name__ == '__main__':
    main()