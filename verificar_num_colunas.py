def verificar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

   
    num_colunas = len(linhas[0].split(';'))

    for i, linha in enumerate(linhas):
        if len(linha.split(';')) != num_colunas:
            print(f"Linha {i+1} tem um número inesperado de colunas.")

verificar_arquivo(r'SEU_ARQUIVO.txt')
print("Concluído")
