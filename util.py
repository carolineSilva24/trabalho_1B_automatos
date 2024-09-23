# coding: utf-8
# from graphviz import Digraph

def saidaAuto(lista_estados, inicial, lista_final, lista_transicao):
    result = "\nAutomato: \n\nestados "
    inicial_saida = "inicial " + inicial
    final = "final "
    
    # Adiciona estados à saída
    result += " ".join(lista_estados)
    result += "\n" + inicial_saida
    
    # Adiciona estados de finalção à saída
    final += " ".join(lista_final)
    result += "\n" + final
    
    # Adiciona transições à saída
    transicoes = []
    for elemento in lista_transicao:
        transicoes.append(f"{elemento[0]} {elemento[2]} {''.join(elemento[1])}")
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

# Função para desenhar o autômato (AFND ou AFD)
# def desenhar_automato(maquina, nome_arquivo):
#     dot = Digraph(comment="Autômato")

#     estados = maquina["estados"]
#     estado_inicial = maquina["inicial"]
#     estados_finais = maquina["final"]
#     transicoes = maquina["transicao"]

#     # Adiciona estados
#     for estado in estados:
#         if estado == estado_inicial:
#             dot.node(estado, shape="doublecircle", color="green")  # Estado inicial
#         elif estado in estados_finais:
#             dot.node(estado, shape="doublecircle", color="red")  # Estado final
#         else:
#             dot.node(estado, shape="circle")

#     # Adiciona transições
#     for transicao in transicoes:
#         estado_origem = "".join(transicao[0])
#         estado_destino = "".join(transicao[1])
#         simbolo = transicao[2]

#         dot.edge(estado_origem, estado_destino, label=simbolo)

#     # Salva o arquivo do Graphviz
#     dot.render(nome_arquivo, format="png")  # Salva como imagem PNG

#     print(f"Arquivo {nome_arquivo}.png gerado com sucesso.")
