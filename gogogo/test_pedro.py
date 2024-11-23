from py2cfg import CFGBuilder

# Lista de arquivos .py e nomes de saída para os PDFs
arquivos = ['arquivo01.py', 'arquivo02.py']
nomes_pdf = ['output1', 'output2']

# Loop sobre os arquivos e nomes de saída
for arquivo, nome_pdf in zip(arquivos, nomes_pdf):
    # Lê o conteúdo do arquivo .py
    with open(arquivo, 'r', encoding='utf-8') as f:
        src = f.read()

    # Constrói a CFG a partir do conteúdo do arquivo
    cfg = CFGBuilder().build_from_src('test', src)

    # Gera o gráfico de visualização em formato 'pdf'
    cfg.build_visual(nome_pdf, 'pdf')

print("Gráficos de CFG gerados com sucesso!")