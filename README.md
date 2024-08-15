# verificar_num_colunas
 Verificar numero de colunas

# 📁 Verificador de Consistência de Arquivo CSV

Bem-vindo ao repositório **Verificador de Consistência de Arquivo CSV**! Este simples, mas poderoso, script em Python foi criado para ajudar a identificar problemas de inconsistência em arquivos delimitados por ponto e vírgula (`;`). Se você já se deparou com erros devido a colunas faltantes ou adicionais em seus arquivos, este script é a solução!

## 🔍 Funcionalidades

- **Verificação Automática de Colunas**: O script verifica se todas as linhas do arquivo possuem o mesmo número de colunas.
- **Detecção de Erros**: Identifica e exibe quais linhas estão fora do padrão, facilitando a correção dos dados.
- **Fácil de Usar**: Basta apontar o script para o arquivo desejado, e ele fará o resto.

## 🛠️ Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos:

- **Python 3.x**
- **Arquivo de Texto**: Um arquivo delimitado por ponto e vírgula (`;`), como um CSV.

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/ericfp87/verificar_num_colunas.git
    ```

2. **Prepare seu arquivo**:
   - Certifique-se de que o arquivo a ser verificado está no formato correto e usa `;` como delimitador.

3. **Execute o script**:
    - Edite o caminho do arquivo no script ou simplesmente substitua `'SEU_ARQUIVO.txt'` pelo caminho do seu arquivo.
    - Execute o script:
    ```bash
    python verificar_arquivo.py
    ```

4. **Verifique os resultados**:
   - O script imprimirá no terminal as linhas que não possuem o número esperado de colunas, permitindo que você as identifique rapidamente.

## 📦 Estrutura do Projeto

```plaintext
├── verificar_arquivo.py    # Script principal para verificação de consistência
├── SEU_ARQUIVO.txt         # Exemplo de arquivo de texto para teste
└── README.md               # Documentação do projeto
```

## 🌟 Dicas e Sugestões

- **Formatos Diferentes**: Embora o script seja projetado para arquivos delimitados por ponto e vírgula, ele pode ser facilmente adaptado para outros delimitadores. Basta modificar o parâmetro de divisão (`split`) na linha de código correspondente.
- **Grandes Arquivos**: Para arquivos muito grandes, considere adicionar uma barra de progresso ou otimizar a leitura das linhas para melhorar o desempenho.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *Issues*.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.