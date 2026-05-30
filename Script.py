# Estrutura de dados

# Memoria Ran - Ela era definir um ID para cada posição de memória, e o valor armazenado nessa posição. Por exemplo, a posição de memória 0 poderia armazenar o valor 5, a posição de memória 1 poderia armazenar o valor 10, e assim por diante.

memoria_ran = [0] * 100 # Inicializa a memória RAM com 256 posições, todas com o valor 0

# Carregando um programa de teste na memória
memoria_ran[0] = "clear"
memoria_ran[1] = "load"
memoria_ran[2] = "add"
memoria_ran[3] = "halt"

# Registradores - Uma memória rápida, onde ficaram guardada as coisas que estão sendo processadas no momento. Por exemplo, um registrador poderia armazenar o resultado de uma operação de adição, ou o endereço de memória onde um valor está armazenado. (So precisam salvar numeros inteiros) (so existem 4 registradores, R0, R1, R2 e R3)

R0 = 0 # Registrador 0
R1 = 0 # Registrador 1
R2 = 0 # Registrador 2
R3 = 0 # Registrador 3

# Programa Counter (PC) - Um contador que indica a posição atual do programa que está sendo executado. Ele é incrementado a cada instrução executada, e pode ser alterado por comandos de salto (como o comando JMP) para pular para uma posição específica do programa.

PC = 0 # Inicializa o Programa Counter (PC) com o valor 0

# ULA - Unidade Lógica e Aritmética, responsável por realizar operações matemáticas e lógicas. Ela pode realizar operações como adição, subtração, multiplicação, divisão, AND, OR, NOT, entre outras. A ULA recebe os operandos (valores a serem processados) dos registradores e retorna o resultado da operação para um registrador ou para a memória.

# Comandos

import os # || Importa o módulo os para usar a função de limpar a tela

# Comando - ADD (adicionar)
def ADD():
    print("Comando ADD executado")

# Comando - SUB (subtrair)
def SUB():
    print("Comando SUB executado")

# Comando - JMP (pular)
def JMP():
    print("Comando JMP executado")

    valor = int(input("Digite o endereço para pular: "))
    
    if valor < 0 or valor >= len(memoria_ran):
        print("Endereço inválido. O endereço deve estar entre 0 e", len(memoria_ran) - 1)
    else:
        global PC
        PC = valor
        print("Programa Counter (PC) atualizado para:", PC)
        return PC
            
# Comando - LOAD (carregar)
def LOAD():
    print("Comando LOAD executado")

    valor = int(input("Digite o valor na memória para carregar: "))

    global memoria_ran

    if valor < 0 or valor >= len(memoria_ran):
        print("Endereço inválido. O endereço deve estar entre 0 e", len(memoria_ran) - 1)
    else:
        valor_carregado = memoria_ran[valor]
        print("Valor carregado da memória:", valor_carregado)

        repetir = True

        while repetir:
            registrador = input("Em qual registrador deseja armazenar o valor carregado? (0 - R0, 1 - R1, 2 - R2 ou 3 - R3, Cancelar): ")
            if registrador == "0":
                global R0
                R0 = valor_carregado
                print("Valor armazenado no registrador R0:", R0)
                repetir = False
            elif registrador == "1":
                global R1
                R1 = valor_carregado
                print("Valor armazenado no registrador R1:", R1)
                repetir = False
            elif registrador == "2":
                global R2
                R2 = valor_carregado
                print("Valor armazenado no registrador R2:", R2)
                repetir = False
            elif registrador == "3":
                global R3
                R3 = valor_carregado
                print("Valor armazenado no registrador R3:", R3)
                repetir = False
            elif registrador == "cancelar":
                print("Operação de LOAD cancelada.")
                repetir = False
            else:
                print("Registrador inválido. O registrador deve ser 0, 1, 2, 3 ou cancelar.")

# Comando - HALT (parar)
def HALT():
    print("Comando HALT executado")
    # Colocar comando para finalizar codigo
    exit()

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Comando - Help (Mostrar os codigos de cada comando)
def Help():
    print("Comandos disponíveis:")
    print("add - Adicionar")
    print("sub - Subtrair")
    print("jmp - Pular")
    print("load - Carregar")
    print("halt - Parar")
    print("clear - Limpar a tela")
    print("help - Mostrar ajuda")

# Inicicialização

Clear() # Limpa a tela antes de iniciar o simulador

print("Iniciando o simulador de computador...")

print("Bem-vindo ao simulador de computador!")

print("Digite 'help' para ver os comandos disponíveis.")

while True: # Loop infinito para continuar pedindo comandos até que o usuário decida parar

    comando = input("Digite um comando: ") # Ta peidendop um comando do usuário

    if comando == "add": # se o comando for "add", chama a função ADD()
        ADD()
    elif comando == "sub": # se o comando for "sub", chama a função SUB()
        SUB()
    elif comando == "jmp": # Assim por diante
        JMP()
    elif comando == "load":
        LOAD()
    elif comando == "halt":
        HALT()
        break
    elif comando == "help":
        Help()
    elif comando == "clear":
        Clear()
    else:
        print("Comando desconhecido. Digite 'Help' para ver os comandos disponíveis.") # Se o comando não for reconhecido, mostra uma mensagem de erro e pede para digitar 'Help' para ver os comandos disponíveis.

