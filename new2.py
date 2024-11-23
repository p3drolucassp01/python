banco.execute(query)

query = '''CREATE TABLE Orcamento (
    orcamento_id INTEGER PRIMARY KEY,
    valor_total DECIMAL(10,2),
    data_emissao DATE,
    cliente_id INTEGER,
    servico_id INTEGER,
    FOREIGN KEY(cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY(servico_id) REFERENCES Servico(servico_id));'''

banco.execute(query)

query = '''CREATE TABLE Peca  
 (
    peca_id INTEGER PRIMARY KEY,
    descricao VARCHAR(100),
    fabricante VARCHAR(50),
    quantidade_estoque INTEGER);'''
    
banco.execute(query)

query = '''CREATE TABLE Tecnico (
    tecnico_id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    especialidade VARCHAR(50));'''

banco.execute(query)

banco = '''CREATE TABLE ItemOrcamento (
    item_orcamento_id INTEGER PRIMARY KEY,
    descricao VARCHAR(100),
    quantidade INTEGER,
    valor_unitario DECIMAL(10,2),
    orcamento_id INTEGER,
    peca_id INTEGER,
    FOREIGN KEY(orcamento_id) REFERENCES Orcamento(orcamento_id),
    FOREIGN KEY(peca_id) REFERENCES Peca(peca_id));'''