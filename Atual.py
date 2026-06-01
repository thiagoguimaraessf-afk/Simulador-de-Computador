"""

Simulador de Computador

Produzido por: 

Thiago Guimarães

Apoio: 

Daniel Padrão
Guilherme Nunes
Luis Davi
Miguel Pereira

"""



# Registradores || Normalmente são 4

Registradores = [0, 0, 0, 0]

# Program Counter (PC) || iniciando com o valor, ele mostra a posição atual da memória que está sendo executada, ou seja, o comando que está sendo lido e executado

PC = 0 

# Memória RAM || onde os comandos e dados são armazenados, normalmente tem um tamanho fixo, como 100 posições

Memoria_ram = [0] * 100

# Carregando um programa de teste na memória de forma limpa

Memoria_ram[51] = 1 # Guardando o número 1 na posição 51 isolada de dados
Memoria_ram[52] = 2 # Guardando o número 2 na posição 52 isolada de dados

Memoria_ram[0] = ("load 51 0")  
Memoria_ram[1] = ("load 51 1") 
Memoria_ram[2] = ("status registradores")
Memoria_ram[3] = ("ula add 0 1 2") 
Memoria_ram[4] = "status pc"
Memoria_ram[5] = "status registradores"
Memoria_ram[6] = "halt"

Memoria_ram[10] = ("status registradores")
Memoria_ram[11] = ("load 51 0")
Memoria_ram[12] = ("load 52 1")
Memoria_ram[13] = ("ula sub 0 1 2")
Memoria_ram[14] = "status pc"
Memoria_ram[15] = "status registradores"
Memoria_ram[16] = "halt"

Memoria_ram[20] = ("jmp 0")
Memoria_ram[21] = ("status registradores")


Programas = {
    "Youtube": {
        "PC": 0,
        "Base": 0,
        "Limite": 9,
        "Registradores": [0, 0, 0, 0],
        "Estado": "Pronto"           # Pode ser: "Pronto", "Executando" ou "Halt"
    },

    "Discord": {
        "PC": 10,
        "Base": 10,
        "Limite": 19,
        "Registradores": [0, 0, 0, 0],
        "Estado": "Pronto"           # Pode ser: "Pronto", "Executando" ou "Halt"
    },

      "Spotfy": {
        "PC": 20,
        "Base": 20,
        "Limite": 29,
        "Registradores": [0, 0, 0, 0],
        "Estado": "Pronto"           # Pode ser: "Pronto", "Executando" ou "Halt"
    },
}

def Processo_Atual(): # || Função para identificar qual processo está sendo executado atualmente, verificando o estado dos programas na tabela
    global Programas
    for nome, info in Programas.items():
        if info['Estado'] == "Executando":
            return nome
    return None

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

def Help(): # || Função para mostrar os comandos disponíveis
    print("""
    || COMANDOS DISPONÍVEIS ||
    
    jmp - Pular para um endereço específico, (escreva: jmp <endereço>)
    load - Carregar um valor da memória para um registrador (escreva: load <endereço_memoria> <num_registrador>)
    ula - Realizar uma operação aritmética entre dois registradores, (escreva: ula <operação> <operando1> <operando2> <Registrador de resultado>)
    clear - Limpar a tela do console
    halt - Finalizar a execução
    status - Mostrar o status do PC ou dos registradores, (escreva: status <PC ou Registradores>)
          
    || OPERAÇÕES ULA DISPONÍVEIS ||
          
    add - Soma os dois operandos   
    sub - Subtrai o segundo operando do primeiro
    mul - Multiplica os dois operandos
    """)

def Clear(): # || Função para limpar a tela do console
    import os # || Importa o módulo os para usar a função de limpar a tela
    
    os.system('cls' if os.name == 'nt' else 'clear') # || Limpa a tela do console dependendo do sistema operacional

def Jmp(valor): # || Comando para pular para um endereço específico, o valor é o endereço para onde o PC deve ser atualizado
    if valor < 0 or valor >= len(Memoria_ram):
        print("Endereço inválido. O endereço deve estar entre 0 e", len(Memoria_ram) - 1)
    else:
        global PC
        PC = valor
        print("Programa Counter (PC) atualizado para:", PC)
        return PC

def Halt(): # || Para tudo
    print("Finalizando Processo")
    # Colocar comando para finalizar codigo
    exit()

def Load(endereco_memoria, num_registrador): # || Leva as informações para os registradores
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

def Status(valor): # || Mostra o status do PC ou dos registradores dependendo do valor passado
    if valor.lower() == "pc":
        global PC
        print("Status do PC:", PC)

    elif valor.lower() == "registradores":
        global Registradores
        print("Status dos Registradores:")
        for i in range(len(Registradores)):
            print(f"R{i}: {Registradores[i]}")
    else:
        print("Uso correto: status <PC ou Registradores>")

# Computador

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
                    Jmp(valor)
                except (IndexError, ValueError): # IndexError || caso so escreva jmp  - ValueError || Trata erros de sintaxe e conversão de tipo
                    print("Uso correto: jmp <endereço>")
            elif comando == "halt":
                Halt()
            elif comando.startswith("ula"):
                try:
                    partes = comando.split()
                    operacao = partes[1] # || Extrai a operação (add, sub, mul)
                    operando1 = Registradores[int(partes[2])] # || Extrai o primeiro operando (registrador)
                    operando2 = Registradores[int(partes[3])] # || Extrai o segundo operando (registrador)
                    resultado_registrador = int(partes[4]) # || Extrai o número do registrador para armazenar o resultado

                    resultado = ULA(operacao, operando1, operando2)
                    if resultado is not None:
                        Registradores[resultado_registrador] = resultado
                        print("Resultado da operação ULA:", resultado)
                except (IndexError, ValueError):
                    print("Uso correto: ula <operação> <operando1> <operando2>")
            elif comando.startswith("load"):
                try:
                    partes = comando.split()
                    endereco_memoria = int(partes[1]) # || Extrai o endereço de memória
                    num_registrador = int(partes[2]) # || Extrai o número do registrador

                    Load(endereco_memoria, num_registrador)
                except (IndexError, ValueError):
                    print("Uso correto: load <endereço_memoria> <num_registrador>")
            elif comando.startswith("status"):
                try:
                    valor = comando.split()[1] # || Extrai o valor do comando status
                    if valor.lower() == "pc":
                        Status(valor)
                    elif valor.lower() == "registradores":
                        Status(valor)
                    else:
                        print("Uso correto: status <PC ou Registradores>")
                except (IndexError, ValueError):
                    print("Uso correto: status <PC ou Registradores>")

    elif adm.lower() == 'n': # Modo Automático

        Clear()
        print("""Iniciando execução automática...
Carregando programa na memória RAM 
              """)
        
        fila = list(Programas.keys()) # || Cria uma fila com os nomes dos programas para simular a ordem de chegada dos processos

        while True: # LOOP DO ESCALONADOR: Fica escolhendo os processos

            if len(fila) == 0: # Ver se a fila de processos está vazia, ou seja, se não tem mais processos para executar
                print(f"\n[SO] >>> Sucesso: Todos os processos foram finalizados pelo Escalonador! <<<")
                Halt()

            processo_escolhido = fila.pop(0) 

            comandos_rodados = 0 # || Contador de comandos rodados para limitar a quantidade de comandos por processo
            maximo_comandos = 2 # || Limite de comandos por processo para simular a troca de contexto

            print(f"\n[SO] >>> Trocando de contexto para: {processo_escolhido} <<<")
            Programas[processo_escolhido]["Estado"] = "Executando"
            PC = Programas[processo_escolhido]["PC"]
            Registradores = Programas[processo_escolhido]["Registradores"].copy()

            while True: # Computador funciona de forma automatica
                comando = Memoria_ram[PC] # || Lê o comando da memória RAM na posição do PC

                if isinstance(comando, int): # Se for inteiro não é nenhum comando
                    print(f"[SO] >>> Comando inválido na posição {PC}: {comando} <<<")
                    PC += 1
                    comandos_rodados += 1
                    continue # || Continua para a próxima posição da memória RAM

                if comando == "halt":
                    print(f"[SO] Processo {processo_escolhido} finalizado com sucesso!")
                    Programas[processo_escolhido]["Estado"] = "Halt"
                    
                    # TROCA DE CONTEXTO (SAVE): Salva o estado final na tabela antes de sair
                    Programas[processo_escolhido]["PC"] = PC
                    Programas[processo_escolhido]["Registradores"] = Registradores.copy()
                    
                    break # ESSE BREAK É O PULO DO GATO! Ele quebra o loop de comandos 
                          # e faz o código voltar para o topo do Escalonador procurar o próximo!

                elif comando == "clear":
                    Clear()
                    PC += 1 
                elif comando.startswith("ula"):
                    try:
                        partes = comando.split()
                        operacao = partes[1] # || Extrai a operação (add, sub, mul)
                        operando1 = Registradores[int(partes[2])] # || Extrai o primeiro operando (registrador)
                        operando2 = Registradores[int(partes[3])] # || Extrai o segundo
                        resultado_registrador = int(partes[4]) # || Extrai o número do registrador para armazenar o resultado

                        resultado = ULA(operacao, operando1, operando2)
                        if resultado is not None:
                            Registradores[resultado_registrador] = resultado
                            print("Resultado da operação ULA:", resultado)
                    except (IndexError, ValueError):
                        print("Uso correto: ula <operação> <operando1> <operando2>")
                    PC += 1 
                elif comando.startswith("jmp"):
                    try:
                        valor = int(comando.split()[1])
                        base_atual = Programas[processo_escolhido]["Base"]
                        limite_atual = Programas[processo_escolhido]["Limite"]
                        
                        if valor < base_atual or valor > limite_atual:
                            print(f"\n[ERRO DE MEMÓRIA] O processo {processo_escolhido} tentou invadir o endereço {valor}!")
                            print(f"Processo {processo_escolhido} abortado por violação de segurança.")
                            Programas[processo_escolhido]["Estado"] = "Halt"
                            break 
                        else:
                            Jmp(valor)
                    except (IndexError, ValueError):
                        print("Uso correto: jmp <endereço>")
                elif comando.startswith("load"):
                    try:
                        partes = comando.split()
                        endereco_memoria = int(partes[1]) # || Extrai o endereço de memória
                        num_registrador = int(partes[2]) # || Extrai o número do registrador

                        Load(endereco_memoria, num_registrador)
                    except (IndexError, ValueError):
                        print("Uso correto: load <endereço_memoria> <num_registrador>")
                    
                    PC += 1 
                elif comando.startswith("status"):
                    try:
                        valor = comando.split()[1] # || Extrai o valor do comando status
                        if valor.lower() == "pc":
                            Status(valor)
                        elif valor.lower() == "registradores":
                            Status(valor)
                        else:
                            print("Uso correto: status <PC ou Registradores>")
                    except (IndexError, ValueError):
                        print("Uso correto: status <PC ou Registradores>")
                    PC += 1

                comandos_rodados += 1

                if comandos_rodados >= maximo_comandos: 
                    print(f"[SO] Tempo de CPU esgotado para o processo {processo_escolhido}. Realizando troca de contexto...")
                    
                    # TROCA DE CONTEXTO (SAVE)
                    Programas[processo_escolhido]["Estado"] = "Pronto"
                    Programas[processo_escolhido]["PC"] = PC
                    Programas[processo_escolhido]["Registradores"] = Registradores.copy()
                    
                    # CORREÇÃO 2: O tempo acabou? Joga ele de volta para o FINAL da fila!
                    fila.append(processo_escolhido)
                    
                    break

    else: # Nada
        print("Opção inválida.") # Volta para saber se o usuário quer ser admin ou não