# coding: utf-8

import sys
import getopt
from conversao import conversao
from util import saidaAuto, afn_checker

maquina = {}

def usage():
    print('''

    Para usar nossa ferramenta: python3 main.py ou python3 main.py -h --Para ter uma help
    ex: $ python3 main.py
    
    Argumentos:

    -c  --conversao de AFN para AFD
    -v  --verifica palavras em arquivo

    Exemplos:
    $ python3 main.py -c arquivo.txt
    $ python3 main.py -v arquivo.txt palavras.txt 
    ''')
    sys.exit(2)

def retornoErros():
    print ('''Confira a linha de comando, esta faltando argumentos.
Exemplos de execucao:

    $ python3 main.py -c arquivo.txt
    $ python3 main.py -v arquivo.txt palavras.txt 
    ''')
    return

def geraMaquina1(file):
    arquivo = open(file, 'r')
    list = []
    maquina["transicao"] = list
    while True:
        l = arquivo.readline()
        if l == '':
            break
        elif l.startswith("estados "):
            aux = l.replace("estados ", "")
            split = aux.split(" ") # tirei a ,
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina["estados"] = split
        elif l.startswith("inicial "):
            aux = l.replace("inicial ", "")
            maquina["inicial"] = aux.split("\n")[0]
        elif l.startswith("final "):
            aux = l.replace("final ", "")
            split = aux.split(" ")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina["final"] = split
        else:
            split = (l.split("\n")[0]).split(" ")
            maquina["transicao"].append([split[0], split[2], split[1]]) # mudei aq para reorganizar

def ler_automato(arquivo_automato):
    with open(arquivo_automato, 'r') as file:
        linhas = file.readlines()

    # Ler estados
    estados = linhas[0].strip().split()
    
    # Ler estados iniciais
    estados_iniciais = linhas[1].strip().split()
    
    # Ler estados finais
    estados_finais = linhas[2].strip().split()

    # Ler transições
    transicoes = {}
    for linha in linhas[3:]:
        estado_inicial, simbolo, estado_final = linha.strip().split()
        if (estado_inicial, simbolo) not in transicoes:
            transicoes[(estado_inicial, simbolo)] = []
        transicoes[(estado_inicial, simbolo)].append(estado_final)

    return estados, estados_iniciais, estados_finais, transicoes


def ler_palavras(arquivo_palavras):
    with open(arquivo_palavras, 'r') as file:
        palavras = [linha.strip() for linha in file.readlines()]
    return palavras


def verificar_palavra(automato, palavra):
    estados, estados_iniciais, estados_finais, transicoes = automato

    # Função recursiva para verificar a palavra no AFND
    def aceita_estado(estado_atual, restante_palavra):
        if not restante_palavra:
            # Se a palavra foi completamente consumida, verificar se o estado atual é final
            return estado_atual in estados_finais
        
        # Pegar o próximo símbolo da palavra
        simbolo_atual = restante_palavra[0]
        restante_palavra = restante_palavra[1:]

        # Verificar transições possíveis
        if (estado_atual, simbolo_atual) in transicoes:
            for proximo_estado in transicoes[(estado_atual, simbolo_atual)]:
                if aceita_estado(proximo_estado, restante_palavra):
                    return True
        return False

    # Verificar se a palavra é aceita a partir de qualquer estado inicial
    for estado_inicial in estados_iniciais:
        if aceita_estado(estado_inicial, palavra):
            return True

    return False

#main
def main():
    if not len(sys.argv[1:]):
        usage()
    
    ###### Trata a entrada para saber se esta de acordo com a especificação ######
    comandLine = sys.argv[1:]
    if len(comandLine) > 3 or len(comandLine) < 2:
        retornoErros()
 
    ###### Captura o arquivo que sera lido ######
    try:
        file = comandLine[1]
    except:
        return
    ###### Captura a linha de comando e faz a verificao para agir com tal   ######
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:v:", [
                                   "conversao=", "verifica="])
    except getopt.GetoptError as err:
        retornoErros()

    for opcao, _ in opts:
        
        if opcao in ("-c", "--conversao"):
            geraMaquina1(file)
            check = afn_checker(maquina["transicao"],maquina["estados"])
            print ("É uma AFN? " + str(check))
            if (check):
                new_maquina = conversao(maquina)
                print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["final"], new_maquina["transicao"]))
            else:
                print("\nO automato '" + file + "' já é uma AFD, portanto, não precisa de conversão :D.\n")
       
        elif opcao in ("-v", "--verifica"):
            # Obtenção dos arquivos de automato e palavras a partir dos argumentos passados
            arquivo_automato = comandLine[1]  # O primeiro argumento depois de -v é o arquivo do automato
            arquivo_palavras = comandLine[2]  # O segundo argumento depois de -v é o arquivo das palavras

            if arquivo_automato is None or arquivo_palavras is None:
               retornoErros()

            automato = ler_automato(arquivo_automato)
            palavras = ler_palavras(arquivo_palavras)

            # Para cada palavra, verificar se é aceita ou não
            for palavra in palavras:
               if verificar_palavra(automato, palavra):
                 print(f"{palavra}: aceita")
               else:
                 print(f"{palavra}: não aceita")

        else:
            assert False,"Opção não tratada"
if __name__ == "__main__":
 main()