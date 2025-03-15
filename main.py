import os

def coletar_dados():
    dados = []
    print("Digite os dados para o relatório. Digite 'sair' para finalizar.")
    while True:
        dado = input("Informe o dado: ")
        if dado.lower() == 'sair':
            break
        dados.append(dado)
    return dados

def gerar_relatorio(dados):
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write("Relatório Gerado\n")
        arquivo.write("=================\n")
        for i, dado in enumerate(dados, start=1):
            arquivo.write(f"{i}. {dado}\n")
    print("Relatório gerado com sucesso: relatorio.txt")

def main():
    dados = coletar_dados()
    gerar_relatorio(dados)

if __name__ == "__main__":
    main()