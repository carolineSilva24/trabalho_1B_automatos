# coding: utf-8

import sys
import getopt
from conversao import conversao
from util import saidaAuto, afn_checker
from simulador import simulador

maquina = {}

def usage():
    print('''

    Para usar nossa ferramenta: python3 main.py ou python3 main.py -h --Para ter uma help
    ex: $ python3 main.py
    
    Argumentos:

    -s  --simulador
    -c  --conversao de AFN para AFD
    -v  --verifica palavras em arquivo

    Exemplos:
    $ python3 main.py -s arquivo.txt 10010
    $ python3 main.py -c arquivo.txt
    $ python3 main.py -v arquivo.txt palavras.txt 
    ''')
    sys.exit()

def retornoErros():
    print ('''Confira a linha de comando, esta faltando argumentos.
Exemplos de execucao:

    $ python3 main.py -s arquivo.txt palavra
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
        elif l.startswith("aceita "):
            aux = l.replace("aceita ", "")
            split = aux.split(" ")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina["aceita"] = split
        else:
            split = (l.split("\n")[0]).split(" ")
            maquina["transicao"].append([split[0], split[2], split[1]]) # mudei aq para reorganizar


def verificar_palavras_arquivo(arquivo_palavras):
    if "estados" not in maquina or "inicial" not in maquina or "aceita" not in maquina or "transicao" not in maquina:
        print("Automato não carregado corretamente.")
        return

    with open(arquivo_palavras, 'r', encoding='utf-8') as f:
        palavras = f.readlines()

    print("\nPalavra           Status")
    print("-------------------------")
    for palavra in palavras:
        palavra = palavra.strip()
        if palavra == "":
            continue
        aceita = simulador(maquina["inicial"], maquina["transicao"], palavra, maquina["aceita"])
        if "palavra aceita" in aceita:
            print(f"{palavra:<20} aceita")
        else:
            print(f"{palavra:<20} não aceita")

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
        opts, args = getopt.getopt(sys.argv[1:], "s:c:v:", [
                                   "simulador=", "conversao=", "verifica="])
    except getopt.GetoptError as err:
        retornoErros()

    for o, a in opts:
        if o in ("-s", "--simulador"):
            geraMaquina1(file)
            try:
                palavra = comandLine[2]
            except:
                retornoErros()
                return
            print("Todos os caminhos tentados:\n\nEstado       Palavra")
            result_simula = simulador(maquina["inicial"], maquina["transicao"], palavra, maquina["aceita"])
            if (result_simula.split("\n")[-1] == "palavra aceita"):
                    print("\n\nCaminho até um estado aceito:\nEstado       Palavra")
                    print(result_simula)
            else:
                    print(result_simula)
        elif o in ("-c", "--conversao"):
            geraMaquina1(file)
            check = afn_checker(maquina["transicao"],maquina["estados"])
            print ("É uma AFN? " + str(check))
            if (check):
                new_maquina = conversao(maquina)
                print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
            else:
                print("\nO automato '" + file + "' já é uma AFD, portanto, não precisa de conversão :D.\n")
        elif o in ("-v", "--verifica"):
            arquivo_afd = a
            arquivo_palavras = sys.argv[sys.argv.index("-v") + 1]
            geraMaquina1(arquivo_afd)
            verificar_palavras_arquivo(arquivo_palavras)
        else:
            assert False,"Unhandled Option"
if __name__ == "__main__":
 main()