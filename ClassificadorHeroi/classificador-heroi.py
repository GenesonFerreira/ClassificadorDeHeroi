import random # Importação da biblioteca random, usada para gerar números aleatórios

herois = [] # Criação de uma lista vazia para armazenar os heróis (cada um será um dicionário com nome e XP)

def classificar_rank(xp): # classifica o XP de acordo com os parametros informados
    if xp < 1000: return "Ferro"
    elif xp <= 2000: return "Bronze"
    elif xp <= 3000: return "Prata"
    elif xp <= 4000: return "Ouro"
    elif xp <= 5000: return "Platina"
    elif xp <= 6000: return "Diamante"
    elif xp <= 7000: return "Ascendente"
    elif xp <= 10000: return "Imortal"
    else: return "Radiante"

def criar_heroi(): # Função para criar um novo herói:
    nome = input("Digite o nome do seu Herói: ") # Solicita o nome do herói ao usuário
    herois.append({"nome": nome, "xp": 0}) # Adiciona um novo herói com XP inicial 0 à lista
    print(f"Herói {nome} criado com sucesso!") ## Confirma a criação

def ganhar_xp(): # Função para adicionar XP aleatório a um herói:
    if not herois:
        print("Você precisa cadastrar um herói primeiro.") # Verifica se há heróis cadastrados na nossa lista vazia
        return # retorna o print caso nao tenha nenhum heroi cadastrado

    while True: # Permite repetir a operação até o usuário decidir sair
        print("\nEscolha um herói para ganhar XP:")
        for i, h in enumerate(herois):# Mostra todos os heróis com índice
            print(f"{i + 1} - {h['nome']} (XP: {h['xp']})")

        try:
            escolha = int(input("Número do herói: ")) - 1  # Lê o índice escolhido (corrigido para começar do 0)
            if 0 <= escolha < len(herois): # Valida o índice
                ganho = random.randint(100, 200)  # Gera um valor de XP aleatório entre 100 e 200
                herois[escolha]["xp"] += ganho # Adiciona o XP ao herói escolhido
                print(f"{herois[escolha]['nome']} ganhou {ganho} XP!")
            else:
                print("Herói inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

        if input("Adicionar XP novamente? (s para sim): ").lower() != "s": # Sai do loop se a resposta for diferente de "s"
            break

def mostrar_herois():# Função para mostrar os heróis cadastrados com XP e Rank:
    if not herois:
        print("Nenhum herói cadastrado.")# Mensagem se a lista estiver vazia
    else:
        print("\nLista de heróis:")
        for h in herois:# Para cada herói, mostra nome, XP e rank calculado
            print(f"Herói: {h['nome']} | XP: {h['xp']} | Rank: {classificar_rank(h['xp'])}")

def menu(): # Função principal de menu (interface do usuário):
    while True:# Loop do menu principal
        print("\n=== Classificador de Nível do Herói ===")
        print("1 - Criar Herói")
        print("2 - Ganhar XP")
        print("3 - Ver Heróis")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")# Lê a escolha do usuário

        if opcao == "1": criar_heroi()
        elif opcao == "2": ganhar_xp()
        elif opcao == "3": mostrar_herois()
        elif opcao == "4":
            print("Saindo do programa...")# Mensagem de saída
            break# Encerra o loop do menu
        else:
            print("Opção inválida.") # Tratamento de opção incorreta

menu()# Inicia o programa chamando o menu principal.
