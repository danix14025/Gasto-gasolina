def gasolina_carro():
    """
    Calcula o consumo aproximado de gasolina baseado na velocidade, 
    frequência de uso diário e período de tempo.
    """
    velocidade = float(input("Qual velocidade você normalmente anda (km/h)?: "))
    vezes = float(input("Quantas vezes no dia você anda no carro?: "))
    tempo = float(input("Por quantos dias você quer calcular o consumo?: "))

    gasolina_gasta = velocidade * vezes * tempo  # Essa fórmula pode ser ajustada conforme necessário

    print(f"\nVocê irá gastar aproximadamente {gasolina_gasta:.2f} litros de gasolina em {tempo} dias.")

def menu():
    """
    Exibe um menu para o usuário escolher se quer calcular o consumo de gasolina.
    """
    while True:
        print("\n===== MENU =====")
        print("1. Calcular gasto de gasolina")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            gasolina_carro()
        elif escolha == "2":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
menu()