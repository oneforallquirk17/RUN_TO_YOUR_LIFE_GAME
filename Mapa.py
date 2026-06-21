import random

def imprimir_mapa_com_nevoa(mapa, jogador_l, jogador_c):
    raio_visao = 2
    print("\n" * 3)

    for l in range(len(mapa)):
        linha_renderizada = ""
        for c in range(len(mapa[l])):
            distancia_linha = abs(l - jogador_l)
            distancia_coluna = abs(c - jogador_c)

            if distancia_linha <= raio_visao and distancia_coluna <= raio_visao:
                linha_renderizada += mapa[l][c]
            else:
                linha_renderizada += "░░"

        print(linha_renderizada)

def gerar_mapa():
    # 1. Cria a matriz 30x30 preenchida com grama ('🌲') de forma automática
    mapa = [["🌲" for _ in range(50)] for _ in range(50)]
    
    # 2. Constrói as paredes (#) nas bordas do mapa (Muros do Mundo)
    for i in range(50):
        mapa[0][i] = "#"       # Muro de cima
        mapa[49][i] = "#"      # Muro de baixo
        mapa[i][0] = "#"       # Muro da esquerda
        mapa[i][49] = "#"      # Muro da direita
        
    # 3. Posiciona os elementos fixos da história nas coordenadas (Linha, Coluna)
    mapa[2][2] = "🏠"          # 🏠 = Casa onde o personagem começa (o garotinho)
    mapa[47][47] = "🏚️"        # 🏚️ = Casa onde o personagem deve encontrar.
            
    return mapa

def imprimir_mapa(mapa):
    # Função para printar o mapa no terminal sem os colchetes e as vírgulas da lista
    for linha in mapa:
        print(" ".join(linha))

# --- TESTANDO O SEU MAPA ---
meu_mapa = gerar_mapa()
imprimir_mapa(meu_mapa)