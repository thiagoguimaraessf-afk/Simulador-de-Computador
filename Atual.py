# Registradores || Normalmente são 4

Registradores = [0, 0, 0, 0]

# Program Counter (PC) || iniciando com o valor, ele mostra a posição atual da memória que está sendo executada, ou seja, o comando que está sendo lido e executado

PC = 0 

# Memória RAM || onde os comandos e dados são armazenados, normalmente tem um tamanho fixo, como 100 posições

Memoria_ram = [0] * 100

# ULA (Unidade Lógica e Aritmética) 

def ULA(operacao, operando1, operando2):
    if operacao == "add":
        return operando1 + operando2
    elif operacao == "sub":
        return operando1 - operando2
    elif operacao == "mul":
        return operando1 * operando2
    else:
        print("Operação desconhecida na ULA.")
        return None

# Discionario de comandos

def Help():
    print(" ")
    print("Comandos disponíveis:")
    print("jmp - Pular para um endereço específico, (escreva: jmp <endereço>)")
    print("load - Carregar um valor da memória para um registrador")
    print("ula - Realizar uma operação aritmética entre dois registradores, (escreva: ula <operação> <operando1> <operando2>)")
    print("clear - Limpar a tela do console")
    print("halt - Finalizar a execução")

def Clear():
    import os # || Importa o módulo os para usar a função de limpar a tela
    
    os.system('cls' if os.name == 'nt' else 'clear') # || Limpa a tela do console dependendo do sistema operacional

def JMP(valor):
    print("Comando JMP executado")
    
    if valor < 0 or valor >= len(Memoria_ram):
        print("Endereço inválido. O endereço deve estar entre 0 e", len(Memoria_ram) - 1)
    else:
        global PC
        PC = valor
        print("Programa Counter (PC) atualizado para:", PC)
        return PC

def HALT():
    print("Comando HALT executado")
    # Colocar comando para finalizar codigo
    exit()

def LOAD(endereco_memoria, num_registrador): # Leva as informações para os registradores
    global Memoria_ram, Registradores
    if endereco_memoria < 0 or endereco_memoria >= len(Memoria_ram):
        print("Erro: Endereço de memória inválido.")
        return
    else:
        valor_carregado = Memoria_ram[endereco_memoria]
        if num_registrador < 0 or num_registrador >= len(Registradores):
            print("Erro: Registrador inválido.")
            return
        else:
            Registradores[num_registrador] = valor_carregado
            print(f"Valor {valor_carregado} carregado no registrador R{num_registrador}")
    


while True: # Modo de execução do computador, onde o usuário pode escolher entre ser admin ou não, e dependendo da escolha, o computador funciona de forma diferente

    adm = input("Entrar como admin? (s/n): ")

    if adm.lower() == 's': # Modo Manual
        Clear()
        print("Bem-vindo, admin!")

        while True: # Comandos manuais
            comando = input("Digite um comando (help para ver os comandos disponíveis): ")
        
            if comando == "help":
                Help()
            elif comando == "clear":
                Clear()
            elif comando.startswith("jmp"):
                try:
                    valor = int(comando.split()[1]) # || Extrai o valor do comando JMP
                    JMP(valor)
                except (IndexError, ValueError): # IndexError || caso so escreva jmp  - ValueError || Trata erros de sintaxe e conversão de tipo
                    print("Uso correto: jmp <endereço>")
            elif comando == "halt":
                HALT()
            elif comando.startswith("ula"):
                try:
                    partes = comando.split()
                    operacao = partes[1] # || Extrai a operação (add, sub, mul)
                    operando1 = int(partes[2]) # || Extrai o primeiro operando (registrador)
                    operando2 = int(partes[3]) # || Extrai o segundo operando (registrador)

                    resultado = ULA(operacao, operando1, operando2)
                    if resultado is not None:
                        print("Resultado da operação ULA:", resultado)
                except (IndexError, ValueError):
                    print("Uso correto: ula <operação> <operando1> <operando2>")
            elif comando.startswith("load"):
                try:
                    partes = comando.split()
                    endereco_memoria = int(partes[1]) # || Extrai o endereço de memória
                    num_registrador = int(partes[2]) # || Extrai o número do registrador

                    LOAD(endereco_memoria, num_registrador)

    elif adm.lower() == 'n': # Modo Automático
        Clear()
        while True: # Computador funciona de forma automatica
            print("Iniciando execução automática...")
            print("Carregando programa na memória RAM...")

            
            

    else: # Nada
        print("Opção inválida.") # Volta para saber se o usuário quer ser admin ou não