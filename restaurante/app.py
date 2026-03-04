from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import os

def limpar_tela():
    input("Pressione Enter para continuar...")
    os.system('cls')








def Menu():
    print("Bem-vindo ao Restaurante!")
    print("1. Adicionar restaurante")
    print("2. Adicionar item no cardápio")
    print("3. Adicionar avaliação")
    print("4. Mostrar restaurantes")
    print("5. Mostrar cardápio")
    print("6. Mudar status do restaurante")
    print("7. Sair")

    resposta = input("Escolha uma opção: ")
    if resposta == "1":
        nome = input("Digite o nome do restaurante: ")
        categoria = input("Digite a categoria do restaurante: ")
        nome = Restaurante(nome, categoria, "desativado")
        print(f'O restaurante {nome} foi criado com sucesso!')
        print(nome.nome)

        limpar_tela()
    

    elif resposta == "2":
        Restaurante.adcionar_item_no_cardapio(Bebida, Prato)

        limpar_tela()

    elif resposta == "3":
        restaurante_nota = input("Digite o nome do restaurante a ser avaliado: ")
        for i in Restaurante.restaurantes:
            if i.nome == restaurante_nota:
                cliente = input("Digite o nome do cliente a dar a nota: ")
                nota = input("Digite a nota que foi dada: ")
                nota = float(nota)
                i.receber_nota(cliente, nota)

                print(f'Restaurante {i.nome} recebeu a nota {nota}.')

        limpar_tela()
        
       

    elif resposta == "4":
        Restaurante.listar_restaurantes()

        limpar_tela()

    elif resposta == "5":
        nome_restaurante = input("Digite o nome do restaurante para mostrar o cardápio: ")
        for i in Restaurante.restaurantes:
            if i.nome == nome_restaurante:
                i.mostrar_cardapio()

        limpar_tela()

    elif resposta == "6":
        nome_restaurante = input("Digite o nome do restaurante para mudar o status: ")
        for i in Restaurante.restaurantes:
            if i.nome == nome_restaurante:
                if i.status == "desativado":
                    i.status = "ativado"
                    print(f'O status do restaurante {i.nome} foi mudado para {i.status} com sucesso!')
                elif i.status == "ativado":
                    i.status = "desativado"
                    print(f'O status do restaurante {i.nome} foi mudado para {i.status} com sucesso!')
                else:
                    print("Deu ruim")
                    pass

        limpar_tela()


  




  
    elif resposta == "7":
        print("Obrigado por usar o Restaurante!")
        exit()


    else:
        print("Opção inválida. Tente novamente.")

        limpar_tela()


    Menu()


Menu()