import argparse

def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]... [FILE]...",
        description="Programa para corrigir provas de vestibulares"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 0.1"
    )
    parser.add_argument('-s', '--save', action='store_true', help="salva o resultado em um arquivo txt")
    parser.add_argument('-r', '--respostas', action='store_true', help="incluir as questões e alternativas escolhidas")
    parser.add_argument("files", nargs=2)
    parser.add_argument("filename", nargs='?')
    return parser

def salvar_resultados(resultados, respostas, filename="resultados.txt"):
    txt_resultados = mostrar_resultados(resultados, respostas)
    file = open(filename, 'wb')
    file.write(txt_resultados.encode('utf8'))
    file.close()

def mostrar_resultados(resultados, respostas = False):
    txt_resultados = f"Total de questões: {resultados['total']}\n"
    txt_resultados += f"Acertos: {resultados['acertos']}\n"
    txt_resultados += f"Erros: {resultados['erros']}\n"
    txt_resultados += f"Sem resposta: {resultados['sem_resposta']}\n"
    if respostas:
        if resultados["certas"]:
            txt_resultados += "\nQuestões Certas:\n"
            txt_resultados += "\n".join(f"{quest[0]:>2}: {quest[1].upper()}" for quest in resultados["certas"])
        if resultados["erradas"]:
            txt_resultados += "\n\nQuestões Erradas:\n"
            txt_resultados += "\n".join(f"{quest[0]:>2}: {quest[1].upper()} --> {quest[2].upper()}" for quest in resultados["erradas"])
        if resultados["sem_responder"]:
            txt_resultados += "\n\nQuestões não repondidas:\n"
            txt_resultados += "\n".join(f"{quest[0]:>2}: {quest[1].upper()}" for quest in resultados["sem_responder"])
    return txt_resultados

def ler_arquivo(filename):
    arquivo = []
    try:
        file = open(filename, 'r')
        arquivo = file.read().splitlines();
    except:
        print("Arquivo não encontrado")
    return arquivo

def corrigir(gabarito, prova):
    dados = dict()
    dados["total"] = len(gabarito)
    dados["acertos"] = 0
    dados["erros"] = 0
    dados["sem_resposta"] = 0
    dados["certas"] = []
    dados["erradas"] = []
    dados["sem_responder"] = []
    for q in range(len(gabarito)):
        if gabarito[q].upper() == prova[q].upper() and prova[q].upper() != '0':
            dados["acertos"] += 1
            dados["certas"].append((q+1, prova[q]))
        else:
            if prova[q] == ",":
                dados["sem_resposta"] += 1
                dados["sem_responder"].append((q+1, prova[q]))
            dados["erros"] += 1
            dados["erradas"].append((q+1, prova[q], gabarito[q]))
    return dados

def main():
    parser = init_argparse()
    args = parser.parse_args()
    print(args)
    if args.files:
        fn_gabarito, fn_prova = args.files
        gabarito = ler_arquivo(fn_gabarito)
        prova = ler_arquivo(fn_prova)
        resultados = corrigir(gabarito, prova)
        print(mostrar_resultados(resultados, args.respostas))
        if args.save:
            print("Salvando respostas")
            if args.filename:
                salvar_resultados(resultados, args.respostas, args.filename)
            else:
                salvar_resultados(resultados, args.respostas)
    else:
        raise SystemExit(parser.format_help())


if __name__ == '__main__':
    main()
