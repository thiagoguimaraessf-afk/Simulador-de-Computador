# Estrutura de dados

# Memoria Ran - Ela era definir um ID para cada posição de memória, e o valor armazenado nessa posição. Por exemplo, a posição de memória 0 poderia armazenar o valor 5, a posição de memória 1 poderia armazenar o valor 10, e assim por diante.


# Registradores - Uma menoria rapida, onde ficaram guardada as corisas que estão sendo processadas no momento. Por exemplo, um registrador poderia armazenar o resultado de uma operação de adição, ou o endereço de memória onde um valor está armazenado. (So precisam salvar numeros inteiros) (so existem 4 registradores, R0, R1, R2 e R3)

# Programa Counter (PC) - Um contador que indica a posição atual do programa que está sendo executado. Ele é incrementado a cada instrução executada, e pode ser alterado por comandos de salto (como o comando JMP) para pular para uma posição específica do programa.

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
    
# Comando - LOAD (carregar)
def LOAD():
    print("Comando LOAD executado")

# Comando - HALT (parar)
def HALT():
    print("Comando HALT executado")
    # Colocar comando para finalizar codigo

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tela limpa.")

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

print("Bem-vindo ao simulador de computador!")

print("Digite 'Help' para ver os comandos disponíveis.")

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

