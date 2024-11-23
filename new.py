import sqlite3


conn = sqlite3.connect('locadora_de_veiculos.db')


query = '''CREATE TABLE IF NOT EXISTS cliente (
    IDcliente INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    CPF TEXT,
    Endereco TEXT,
    Telefone TEXT,
    E_mail TEXT,
    Cliente_TIPO INT
);'''
conn.execute(query)

query = '''CREATE TABLE IF NOT EXISTS relacionamento (
   fk_Cliente_IDcliente INTEGER,
   fk_Locacao_IDdalocacao INTEGER,
   fk_Locacao_IDcliente INTEGER,
   fk_Locacao_IDveiculo INTEGER
);'''
conn.execute(query)

query = '''CREATE TABLE IF NOT EXISTS locacao (
    IDdalocacao INTEGER,
    IDcliente INTEGER,
    IDveiculo INTEGER,
    Datadalocacao TEXT,
    Datadadevolucao TEXT,
    Valortotal REAL,
    Status TEXT,
    Hora TEXT,
    PRIMARY KEY (IDdalocacao, IDcliente, IDveiculo)
);'''
conn.execute(query)

query = '''CREATE TABLE IF NOT EXISTS veiculos (
    IDveiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    Modelo TEXT,
    Marca TEXT,
    AnodeFabricacao INTEGER,
    Cor TEXT,
    Tipo TEXT,
    Precodelocacaododia REAL,
    Disponibilidade TEXT,
    Placa TEXT,
    fk_Locacao_IDdalocacao INTEGER,
    fk_Locacao_IDcliente INTEGER,
    fk_Locacao_IDveiculo INTEGER
);'''
conn.execute(query)


clientes = [
    ('João Silva', '12345678900', 'Rua A, 123', '11987654321', 'joao@gmail.com', 1),
    ('Maria Oliveira', '98765432100', 'Rua B, 456', '21987654321', 'maria@gmail.com', 2),
    ('Pedro Santos', '19283746500', 'Rua C, 789', '31987654321', 'pedro@gmail.com', 1),
    ('Ana Costa', '56473829100', 'Rua D, 012', '41987654321', 'ana@gmail.com', 2),
    ('Lucas Lima', '84736291000', 'Rua E, 345', '51987654321', 'lucas@gmail.com', 1)
]

locacoes = [
    (1, 1, 1, '2024-07-01', '2024-07-10', 500.00, 'Ativa', '10:00'),
    (2, 2, 2, '2024-07-02', '2024-07-09', 450.00, 'Concluída', '11:00'),
    (3, 3, 3, '2024-07-03', '2024-07-08', 400.00, 'Ativa', '12:00'),
    (4, 4, 4, '2024-07-04', '2024-07-07', 350.00, 'Concluída', '13:00'),
    (5, 5, 5, '2024-07-05', '2024-07-06', 300.00, 'Ativa', '14:00')
]

veiculos = [
    ('Gol', 'Volkswagen', 2020, 'Branco', 'Hatch', 50.00, 'Disponível', 'ABC1234', 1, 1, 1),
    ('Onix', 'Chevrolet', 2021, 'Preto', 'Sedan', 60.00, 'Indisponível', 'DEF5678', 2, 2, 2),
    ('HB20', 'Hyundai', 2019, 'Prata', 'Hatch', 55.00, 'Disponível', 'GHI9012', 3, 3, 3),
    ('Argo', 'Fiat', 2022, 'Vermelho', 'Hatch', 65.00, 'Indisponível', 'JKL3456', 4, 4, 4),
    ('Ka', 'Ford', 2018, 'Azul', 'Hatch', 45.00, 'Disponível', 'MNO7890', 5, 5, 5)
]


conn.executemany('''
    INSERT INTO cliente (Nome, CPF, Endereco, Telefone, E_mail, Cliente_TIPO)
    VALUES (?, ?, ?, ?, ?, ?);
''', clientes)


conn.executemany('''
    INSERT INTO locacao (IDdalocacao, IDcliente, IDveiculo, Datadalocacao, Datadadevolucao, Valortotal, Status, Hora)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
''', locacoes)


conn.executemany('''
    INSERT INTO veiculos (Modelo, Marca, AnodeFabricacao, Cor, Tipo, Precodelocacaododia, Disponibilidade, Placa, fk_Locacao_IDdalocacao, fk_Locacao_IDcliente, fk_Locacao_IDveiculo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
''', veiculos)


conn.commit()


conn.close()
