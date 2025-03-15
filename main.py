import os
from datetime import datetime

def coletar_dados():
    dados = []
    print("Digite os dados para o relatório. Digite 'sair' para finalizar.")
    while True:
        dado = input("Informe o dado (formato: Item - Quantidade): ")
        if dado.lower() == 'sair':
            break
        if ' - ' not in dado:
            print("Formato inválido. Use o formato: Item - Quantidade")
            continue
        dados.append(dado)
    return dados

def gerar_relatorio(dados, formato='txt'):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists('relatorios'):
        os.makedirs('relatorios')
    
    if formato == 'txt':
        with open('relatorios/relatorio.txt', 'w') as arquivo:
            arquivo.write("Relatório Gerado\n")
            arquivo.write(f"Data e Hora: {data_hora}\n")
            arquivo.write("=================\n")
            for i, dado in enumerate(dados, start=1):
                arquivo.write(f"{i}. {dado}\n")
            arquivo.write("=================\n")
            arquivo.write(f"Total de Itens: {len(dados)}\n")
        print("Relatório gerado com sucesso: relatorios/relatorio.txt")
    if formato == 'csv':
        with open('relatorios/relatorio.csv', 'w') as arquivo:
            arquivo.write("Item,Quantidade\n")
            for dado in dados:
                item, quantidade = dado.split(' - ')
                arquivo.write(f"{item},{quantidade}\n")
        print("Relatório gerado com sucesso: relatorios/relatorio.csv")
    else:
        print("Formato de relatório desconhecido. Use 'txt' ou 'csv'.")

def main():
    dados = coletar_dados()
    formato = input("Escolha o formato do relatório (txt/csv): ").strip().lower()
    gerar_relatorio(dados, formato)

if __name__ == "__main__":
    main()