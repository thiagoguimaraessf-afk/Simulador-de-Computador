# Tabela



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
while True:
    comando = input("Digite um comando: ")
    
    if comando == "add":
        ADD()
    elif comando == "sub":
        SUB()
    elif comando == "jmp":
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
        print("Comando desconhecido. Digite 'Help' para ver os comandos disponíveis.")

