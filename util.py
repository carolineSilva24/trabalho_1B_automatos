# coding: utf-8

# não consigo azer com que o resultado fique no formato A 0 B, está ficando A 0 ['B']
def saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao):
    result = "\nAutomato: \n\nestados "
    inicial_saida = "inicial " + inicial
    aceita = "aceita "
    
    # Adiciona estados à saída
    result += " ".join(lista_estados)
    result += "\n" + inicial_saida
    
    # Adiciona estados de aceitação à saída
    aceita += " ".join(lista_aceita)
    result += "\n" + aceita
    
    # Adiciona transições à saída
    transicoes = []
    for elemento in lista_transicao:
        transicoes.append(f"{elemento[0]} {elemento[2]} {elemento[1]}")
    result += "\n" + "\n".join(transicoes)
    
    return result

def afn_checker(lista_transicao, lista_estados):
    count = 0
    for elemento in lista_transicao:
        if "h" == elemento[2]:
            return True
    for estado in lista_estados:
        for elemento in lista_transicao:
            if estado == elemento[0] and elemento[2] != "h":
                count += 1
        if count < 2 or count > 2:
            return True
        else:
            count = 0  
    return False