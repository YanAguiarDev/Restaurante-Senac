from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, status):
        self.nome = nome.title()
        self.categoria = categoria.title()
        self.status = status 
        self.cardapio = []
        self.avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status".ljust(20)}')
        for i in cls.restaurantes:
            print(f'{i.nome.ljust(20)} | {i.categoria.ljust(20)} | {str(i.media_avaliacao).ljust(20)} | {i.status.ljust(20)}')

    def arredondar(numero):
        return round(numero, 1)

    def receber_nota(self, cliente, nota):
        nota = float(nota)
        if nota > 5 or nota < 0:
            print('Nota inválida. A nota deve ser entre 0 e 5.')
            return None
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):

        if not self.avaliacao:
            return 0

        soma_das_notas = 0
        for i in self.avaliacao:
            soma_das_notas += float(i.nota)
        quantidade_de_notas = len(self.avaliacao)
        media = soma_das_notas / quantidade_de_notas
        media = Restaurante.arredondar(media)
        return media
    
    def adicionar_no_cardapio(self, item):


        if isinstance(item, ItemCardapio):
            self.cardapio.append(item)

    def mostrar_cardapio(self):
        listagem = 0

        print(f'Cardapio do restaurante {self.nome}:')
        print(f'{"Nome do Item:".ljust(18)} | {"Preço:".ljust(18)} | {"Descrição:".ljust(18)}')
        for i in self.cardapio:
            listagem += 1
            print(f'{listagem}. {i.nome.ljust(15)} | R${str(i.preco).ljust(16)} | {i.descricao.ljust(15)}')

    def adcionar_item_no_cardapio(Bebida, Prato):
        nome_restaurante = input("Digite o nome do restaurante que vai receber o Item: ")
        for i in Restaurante.restaurantes:
            if i.nome == nome_restaurante:
                tipo = input("1. Bebida  2. Comida: ")
                nome_item = input("Digite o nome do item: ")
                preco = input("Digite o preco do item: ")
                preco = float(preco)
                if tipo == "1":
                    tamanho = input("Digite o tamanho do item: ")

                    nome_item = Bebida(nome_item, preco, tamanho)

                elif tipo == "2":
                    descricao = input("Digite a descrição do item: ")

                    nome_item = Prato(nome_item, preco, descricao)
                else:
                    print("Deu ruim")
                    pass

            
                i.adicionar_no_cardapio(nome_item)
                print(f'O item {nome_item.nome} foi adicionado ao cardápio do restaurante {i.nome} com sucesso!')

""" FIM DA CLASSE """


