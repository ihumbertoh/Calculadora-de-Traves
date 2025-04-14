from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

def exibir_cabecalho():
    print(Fore.CYAN + "╔═══════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.YELLOW + "         CALCULADORA DE TRAVES            " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "           Criado por IcaroH              " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════╝\n")

def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(Fore.WHITE + mensagem))
            if valor <= 0:
                print(Fore.RED + "Valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número válido.")

while True:
    exibir_cabecalho()

    valor_super = ler_valor("Digite o valor total em R$: ")
    odd_super = ler_valor("Digite a odd da superbet: ")
    odd_mais = ler_valor("Digite a odd do mais traves: ")

    total = (valor_super * odd_super) / odd_mais
    ganho_total = total * odd_mais
    lucro = ganho_total - (valor_super + total)

    print("\n" + Fore.GREEN + f"Deve apostar no mais traves: R$ {total:.2f}")
    print(Fore.WHITE + f"Retorno Total: R$ {ganho_total:.2f}")
    print(Fore.YELLOW + f"Lucro: R$ {lucro:.2f}\n")

    repetir = input(Fore.WHITE + "Deseja fazer outra simulação? (s/n): ").strip().lower()
    if repetir != 's':
        print(Fore.CYAN + "\nEncerrando o programa. Boa sorte nas apostas!")
        print(Fore.MAGENTA + "Criado por IcaroH 🧠⚽")
        break
