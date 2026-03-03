from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.descricao = tamanho

    def __str__(self):
        return f'{self.nome} | {self.preco} | {self.descricao}'


