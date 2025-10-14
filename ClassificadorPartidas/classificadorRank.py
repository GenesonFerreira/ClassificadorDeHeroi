# Função que calcula o saldo de vitórias e determina o nível do jogador
def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    # Estrutura de decisão para determinar o nível
    if 0 <= saldo_vitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    elif saldo_vitorias >= 101:
        nivel = "Imortal"

    # Retorna uma tupla com o saldo e o nível
    return saldo_vitorias, nivel


# Programa principal
while True:
    print("===== Calculadora de Partidas Rankeadas =====")
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    saldo, nivel = calcular_rank(vitorias, derrotas)
    print(f"\nO Herói tem um saldo de {saldo} e está no nível de {nivel}.\n")

    # Pergunta se o usuário quer calcular novamente
    continuar = input("Deseja calcular novamente? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break