--- INSTALACAO graphviz ---
1 - instalar a ultima versão do graphviz link ->https://graphviz.org/download/
2 - adicionar o caminho C:\Program Files\Graphviz\bin as variáveis de ambiente (PATH)
3 - executar o comando no terminal ->  python -m pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz

--- USANDO pycfg ---
1 - Extrair o arquivo pycfg.tar
2 - Executar o seguinte comando no terminal -> python path_to/pycfg.py path_to/whiletest.py -d

