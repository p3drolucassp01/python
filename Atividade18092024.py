class Vendedor():
    def _init_(self, nome):
        self.nome = nome
        self.vendas = 0
    
    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "bateu a meta")
        else:
            print(self.nome, "não bateu a meta")

Vendedor1 = Vendedor('Paulo')
Vendedor1.vendeu(5000)
Vendedor2 = Vendedor('Pedro')
Vendedor2.vendeu(3000)

print(Vendedor1.nome)
print(Vendedor2.nome)

meta = 4000
Vendedor1.bateu_meta(meta)
Vendedor2.bateu_meta(meta)


class produto:
    def _init_(self,nome,preco,quantidade):
        self.nome =nome
        self.preco =preco
        self.quantidade =quantidade

    def mostra_info(self):
        print(f"nome:{self.nome}")
        print(f"preco:R${self.preco}")
        print(f"quantidade:{self.quantidade}") 
        
p1 = produto("agua",2.50,60)
p1.mostra_info()        
p2 = produto("cafe",10.00,1)
p2.mostra_info()
p3 = produto("chocolate", 50,23)
p3.mostra_info()


class veiculo:
    def _init_(self,nome,placa,cor,fabricante,ano):
        self.nome =nome
        self.placa =placa
        self.cor =cor
        self.fabricante=fabricante
        self.ano=ano

    def mostra_info(self):
        print(f"nome:{self.nome}")
        print(f"placa: {self.placa}")
        print(f"cor:{self.cor}") 
        print(f"fabricante: {self.fabricante}")
        print(f"ano: {self.ano}")

cliente =veiculo("fusca","abc3869","vermelho","honda", 1960)
cliente.mostra_info()