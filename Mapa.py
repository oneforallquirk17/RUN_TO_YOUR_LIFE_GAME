import random

def gerar_mapa():
    # 1. Cria a matriz 30x30 preenchida com grama ('🌲') de forma automática
    mapa = [["🌲" for _ in range(30)] for _ in range(30)]
    
    # 2. Constrói as paredes (#) nas bordas do mapa (Muros do Mundo)
    for i in range(30):
        mapa[0][i] = "#"       # Muro de cima
        mapa[29][i] = "#"      # Muro de baixo
        mapa[i][0] = "#"       # Muro da esquerda
        mapa[i][29] = "#"      # Muro da direita
        
    # 3. Posiciona os elementos fixos da história nas coordenadas (Linha, Coluna)
    mapa[2][2] = "🏠"          # 🏠 = Casa onde o personagem começa (o garotinho)
    mapa[27][27] = "🏚️"        # 🏚️ = Casa onde o personagem deve encontrar.
            
    return mapa

def imprimir_mapa(mapa):
    # Função para printar o mapa no terminal sem os colchetes e as vírgulas da lista
    for linha in mapa:
        print(" ".join(linha))

# --- TESTANDO O SEU MAPA ---
meu_mapa = gerar_mapa()
imprimir_mapa(meu_mapa)