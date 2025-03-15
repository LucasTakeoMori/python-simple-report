# Projeto de Geração de Relatórios em Python

## Descrição

Este é um projeto simples em Python que coleta dados fornecidos pelo usuário e gera um relatório em formato de texto. O objetivo é facilitar a criação de relatórios personalizados de maneira rápida e eficiente.

## Funcionalidades

- **Coleta de Dados**: Permite ao usuário inserir múltiplos dados até que ele decida finalizar.
- **Geração de Relatório**: Cria um relatório formatado em um arquivo de texto (`relatorio.txt`), listando todos os dados fornecidos pelo usuário.
- **Interface Simples**: Interação por linha de comando para fácil uso.

## Pré-requisitos

- Python 3.x

## Como Usar

Siga os passos abaixo para executar o projeto:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. **Execute o script principal**:
    ```bash
    python main.py
    ```

3. **Insira os dados**: Siga as instruções na tela para inserir os dados. Digite `sair` para finalizar a entrada de dados.

4. **Verifique o relatório**: Após finalizar a entrada de dados, o relatório será gerado no arquivo `relatorio.txt` no diretório do projeto.

## Exemplo de Uso

```bash
$ python main.py
Digite os dados para o relatório. Digite 'sair' para finalizar.
Informe o dado: Produto A - 100 unidades
Informe o dado: Produto B - 200 unidades
Informe o dado: sair
Relatório gerado com sucesso: relatorio.txt
```

## Estrutura do Projeto

```plaintext
├── README.md
├── main.py
└── relatorio.txt  # Gerado após a execução do script
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Autor

- **Lucas Takeo Mori** - [LucasTakeoMori](https://github.com/LucasTakeoMori)