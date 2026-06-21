from Mapa import gerar_mapa, imprimir_mapa_com_nevoa

conquistas = set() # Criei um set(conjunto) para quardar as conquistas do jogador, sem duplicata em caso de completar a etapa da história do jogo mais de uma vez.

def conquistas_desbloqueadas(conquista_jogador):
    global conquistas # Dizemos ao python que queremos mexer na variável coquistas, que está fora da função, o seja ela é uma variável global.

    if conquista_jogador not in conquistas:
        conquistas.add(conquista_jogador)
        print(f"\n🏆 CONQUISTA DESBLOQUEADA: [{conquista_jogador}]")

def exibir_conquistas(suas_conquistas):
    print("Suas Conquistas Coletadas:")
    for conquista in suas_conquistas:
        print(f"- {conquista}")

def init_game(nome_user, idade_user):
    print("-"*10, "RUN TO YOUR LIFE", "-"*10)
    print("Carregando status do jogador... ")
    print(f"Nome do jogador: {nome_user}")
    print(f"Idade do jogador: {idade_user}")

    print("Play","\nQuit")
    option = input().capitalize()

    if option == "Quit":
        return # Finaliza a função aqui.
    
    if option == "Play":
        print("iniciando história...")
        print("Você é um garoto de 8 anos chamado joshua, você mora com seus pais em um lugar afastado da cidade em uma casa simples.")
        print("Mas em um dia, enquanto você estava no seu quarto, você escuta um barulho um tanto estranho, e você resolve ver o que aconteceu.")
        print("Indo em direção ao lugar de onde veio aquele som, com passos silenciosos, você vê algo terrivel...")
        print("Um monstro havia entrado na sua casa enquanto todos estavam dormindo e estava devorando os seus pais, ou o que sobrou deles.")
        print("Nesse momento, aquele monstro te vê no canto da porta observando tudo e começa a te seguir.")
        print("A pergunta é, o que você irá fazer para fugir do monstro? Esse é o momento de CORRER PELA SUA VIDA!")
        print("Encontre a casa na floresta, a pessoa que mora nela pode te ajudar!")
        mapa = gerar_mapa()

        jogador_linha = 1
        jogador_coluna = 1
        # Posições iniciais dos personagens.
        monstro_linha = 9
        monstro_coluna = 9

        armadilha_monstro_linha = 16
        armadilha_monstro_coluna = 19

        # Colocando os personagens no mapa.
        mapa[jogador_linha][jogador_coluna] = "👦"
        mapa[monstro_linha][monstro_coluna] = "👹"
        mapa[armadilha_monstro_linha][armadilha_monstro_coluna] = "🕳️"

        while True:
            imprimir_mapa_com_nevoa(mapa, jogador_linha, jogador_coluna)

            movimento_personagem = input("\nPara onde ir? (W: Cima, A: Esquerda, S: Baixo, D: Direita): ").upper()

            linha_antiga = jogador_linha
            coluna_antiga = jogador_coluna

            match movimento_personagem:
                case "W":
                    jogador_linha -= 2
                case "A":
                    jogador_coluna -= 2
                case "S":
                    jogador_linha += 2
                case "D":
                    jogador_coluna += 2
                case "EXIT":
                    print("Você desistiu de correr pela sua vida.")
                    break
                case _:
                    print("Comando inválido! Para movimentar o personagem, utilize as teclas W, A, S, D")
                    continue
            # Apagamos o garoto da posição antiga e colocamos uma 🌲 no lugar (🌲= grama)
            mapa[linha_antiga][coluna_antiga] = "🌲"

            mapa[jogador_linha][jogador_coluna] = "👦"

            monstro_linha_antiga = monstro_linha
            monstro_coluna_antiga = monstro_coluna

            if monstro_linha > jogador_linha:
                monstro_linha -= 1
            elif monstro_linha < jogador_linha:
                monstro_linha += 1

            if monstro_coluna > jogador_coluna:
                monstro_coluna -= 1
            elif monstro_coluna < jogador_coluna:
                monstro_coluna += 1
            
            
            mapa[monstro_linha_antiga][monstro_coluna_antiga] = "🌲"
            mapa[monstro_linha][monstro_coluna] = "👹"


            if jogador_linha == monstro_linha and jogador_coluna == monstro_coluna:
                imprimir_mapa(mapa)
                print("\n👹 O MONSTRO TE PEGOU! GAME OVER!")
                break

            if jogador_linha == 47 and jogador_coluna == 47: # A posição do mapa onde está localizada a casa que o personagem deve encontrar.
                conquista1 = "Porto Seguro: Você encontrou a casa da senhora que irá te ajudar a derrotar o montro!"
                print("Você encontrou a casa e entra nela para se esconder do monstro.")
                print("O monstro bate algumas vezes na porta, mas desiste e vai embora.")
                print("Nesse momento, você conhece uma senhora que mora naquela casa, ela fala sobre o monstro para você e te dá uma informação muito inportante.")
                print("Como matar o monstro! Você escuta atentemente as instruções para fazer isso. A senhora te entrega as instruções necessárias para matar o monstro.")
                print("Você sai da casa da mulher para tentar encontra-lo, e consegue, o monstro novamente começa a te seguir pela floreta.")
                print("Mas, o que são essas instruções que podem matar o montro? A resposta é, uma armadilha. Parece fraco, mas pode prender fácilmente o monstro e acabar com essa perseguição.")
                print("Você precisa atrai-lo para essa armadilha, mas como você fará isso? ")
                conquistas_desbloqueadas(conquista1)
                continue

            if monstro_linha == 16 and monstro_coluna == 19: # Onde está localizada a armadilha para derrotar o monstro.
                conquista2 = "Caçador de Monstros: Você conseguiu derrotar o monstro que estava te perseguindo pela floreta, usando as intruções que a velha senhora te deu."
                print("Ufa! Parece de que você derrotou o monstro. Por enquanto!")
                print("Na verdade, a armadilha para matar o monstro era um buraco. Um buraco beeeeeeemm fundo.")
                print("Se ele caiu nesse buraco, ele provavelmente nunca mais vai sair de lá.")
                print("Você ao saber que o monstro está enfim derrotado, você volta para a sua casa para pegar as suas coisas.")
                print("Chegando lá, você encontra os restos dos seus pais no quarto deles, você sente tristeza, mas sabe que isso não vai traze-los de volta.")
                print("Então, você pega as suas coisas e parte para uma exploração nessa imensa floresta, para encontrar um outro lugar para morar.")
                print("Por esse momento, as coisas seguem tranquilas, mas não se engane. O monstro caiu no buraco, mas não significa que ele realmente morreu.")
                print("Em breve, tenha a certeza que aquele monstro vai voltar a segui-lo.")
                print("E com esse pensamento, você segue a vida explorando o mundo a fora, mas com a tristeza de que a sua familia nunca mais irá voltar a ser como antes...")
                print("FIM DE JOGO! POR EQUANTO")
                conquistas_desbloqueadas(conquista2)
                exibir_conquistas(conquistas)
                break

        print("\n" * 2) # Limpa o terminal visualmente.

if __name__== "__main__":

    print("-"*10, "Seja bem-vindo jogador!", "-"*10)
    print("Para iniciar a sua jornada, insira os seus dados abaixo: ")
    nome = input("nome: ").capitalize() # transforma a primeira letra do nome para maiúscula.
    try:
        idade = int(input("idade: "))
    except ValueError:
        print("ERRO! Insira apenas números nesse campo.")
        idade = 18
        # Garante que a variável exista, mesmo com o erro!
    
    print("Salvando dados do jogador...")
    print("Dados salvos.")

    init_game(nome, idade)