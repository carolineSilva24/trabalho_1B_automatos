# coding: utf-8

def simulador(estado_atual, lista_de_transicoes, palavra, estado_de_aceitacao):
    if((estado_atual in estado_de_aceitacao) and ((len(palavra) == 0))):
        print (estado_atual + "            h")
        return estado_atual + "            h" + "\n\npalavra aceita"
    elif(len(palavra) > 0):
        result = "\npalavra não aceita"
        for elemento in lista_de_transicoes:
            if (elemento[0] == estado_atual and (elemento[1] == palavra[0] or elemento[1] == "h")):
                print(estado_atual + "            " + palavra)
                aux = ""
                if (elemento[2] == "h"):
                    aux = (estado_atual + "            " + palavra + "\n") + simulador(elemento[2], lista_de_transicoes, palavra, estado_de_aceitacao)
                else:
                    if(len(palavra) <= 1):
                        aux = (estado_atual + "            " + palavra + "\n") + simulador(elemento[1], lista_de_transicoes, "", estado_de_aceitacao)
                    else:
                        aux = (estado_atual + "            " + palavra + "\n") + simulador(elemento[1], lista_de_transicoes, palavra[1:], estado_de_aceitacao)
                if (aux.split("\n")[-1] == "palavra aceita"):
                    result = aux
                    break
        if result == "\npalavra não aceita":
            result = (estado_atual + "            " + palavra + "\n") + result
        return result
    elif(len(palavra) == 0):
        print(estado_atual + "            h")
        return "\npalavra não aceita"