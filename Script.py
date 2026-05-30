# Estrutura de dados

memoria_ran = [0] * 100 # Inicializa a memória RAM com 100 posições, todas com o valor 0

# Carregando um programa de teste na memória de forma limpa
memoria_ran[0] = ("load", 50, 0)  # Carrega o valor da posição 50 no R0
memoria_ran[1] = ("load", 50, 1)  # Carrega o valor da posição 50 no R1
memoria_ran[2] = ("ula", "add", 0, 1) # Soma R0 e R1 e joga no R2
memoria_ran[3] = "halt"

# Guardando o número 1 na posição 50 isolada de dados
memoria_ran[50] = 1
    
R0 = 0 # Registrador 0
R1 = 0 # Registrador 1
R2 = 0 # Registrador 2
R3 = 0 # Registrador 3
    
PC = 0 # Inicializa o Programa Counter (PC) com o valor 0

def ULA(operacao, operando1, operando2):
    if operacao == "add":
        return operando1 + operando2
    elif operacao == "sub":
        return operando1 - operando2
    # Aqui você pode adicionar mais operações, como multiplicação, divisão, AND, OR, etc.
    else:
        print("Operação desconhecida na ULA.")
        return None

# Comandos

import os # || Importa o módulo os para usar a função de limpar a tela

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
            
# Comando - LOAD (carregar) atualizado
def LOAD(endereco_memoria, num_registrador):
    print(f"Comando LOAD executado: Carregando posição {endereco_memoria} no registrador R{num_registrador}")

    global memoria_ran, R0, R1, R2, R3

    if endereco_memoria < 0 or endereco_memoria >= len(memoria_ran):
        print("Erro: Endereço de memória inválido.")
        return

    valor_carregado = memoria_ran[endereco_memoria]

    # Agora comparamos com números inteiros, sem aspas!
    if num_registrador == 0:
        R0 = valor_carregado
    elif num_registrador == 1:
        R1 = valor_carregado
    elif num_registrador == 2:
        R2 = valor_carregado
    elif num_registrador == 3:
        R3 = valor_carregado
    else:
        print("Erro: Registrador inválido.")
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
    print("jmp - Pular")
    print("load - Carregar")
    print("halt - Parar")
    print("clear - Limpar a tela")
    print("help - Mostrar ajuda")

# Inicicialização na maão do usuário || Desativado
"""
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
"""

# Inicialização no automático
print("Iniciando o simulador de computador...")
print("Bem-vindo ao simulador de computador!")

while PC < len(memoria_ran):
    
    instrucao_atual = memoria_ran[PC]
    
    # Se a instrução for vazia (0), apenas pula
    if instrucao_atual == 0:
        PC = PC + 1
        continue

    # --- FASE DE DECODIFICAÇÃO ---
    # Se for uma tupla, o comando é o primeiro item
    if isinstance(instrucao_atual, tuple):
        comando = instrucao_atual[0]
    else:
        comando = instrucao_atual
    
    print(f"\n[CPU] PC: {PC} | Executando: {comando}")

    # --- FASE DE EXECUÇÃO ---
    if comando == "clear":
        Clear()
        
    elif comando == "load":
        # instrucao_atual é ("load", 1, 0) -> instrucao_atual[1] é o endereço, [2] é o registrador
        LOAD(instrucao_atual[1], instrucao_atual[2])
        
    elif comando == "jmp":
        JMP()
        
    elif comando == "ula":
        # instrucao_atual é ("ula", "add", 0, 1)
        operacao = instrucao_atual[1]
        reg_A = instrucao_atual[2]
        reg_B = instrucao_atual[3]
        
        # Pega o valor real de dentro dos registradores para mandar para a ULA
        val1 = R0 if reg_A == 0 else R1 if reg_A == 1 else R2 if reg_A == 2 else R3
        val2 = R0 if reg_B == 0 else R1 if reg_B == 1 else R2 if reg_B == 2 else R3
        
        # Executa a conta e salva sempre no R2 (como você planejou no seu comentário)
        R2 = ULA(operacao, val1, val2)
        print(f"Resultado da ULA ({operacao} R{reg_A} + R{reg_B}): R2 agora vale {R2}")
        
    elif comando == "halt":
        HALT()
        
    # Avança o PC
    if comando != "jmp":
        PC = PC + 1