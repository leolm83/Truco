import random
class Baralho:
    def __init__(self):
        self.baralho_base=[]
        self.cartas=[]
        self.gerar_baralho()
    def obter_uma(self):
        resultado=""
        aleatorio=random.randint(0, len(self.cartas)-1)
        resultado=self.cartas[aleatorio]
        #é necessario cria um metodo para que isso nao interfira no jogo pois é necessario remover o
        #self.cartas.pop(aleatorio)
        return resultado
    def obter_tres(self):
        resultado=[]
        for x in range(3):
            resultado.append(self.obter_uma())
        return resultado
    def gerar_baralho(self):
        naipes=["♧","♡","♤","♢"]
        valores=["4","5","6","7","Q","J","K","A","2","3"]
        for valor in valores:
            for naipe in naipes:
                self.cartas.append({valor:naipe})
                self.baralho_base.append({valor:naipe})
        print(self.cartas)
class Jogador:
    def __init__(self):
        self.cartas=[]
    def obter_cartas(self,card):
        for item in card:
            self.cartas.append(item)
    def jogar_carta(self):
        indice=-1
        while(not(indice>-1 and indice<len(self.cartas)) ):
            try:
                print(self.cartas)
                self.ver_cartas()
                indice=int(input("Digite o indice que voce deseja : "))
                valor=self.cartas[indice]
            except:
                continue
        self.cartas.pop(indice)
        return valor
    def ver_cartas(self):
        print(f"Suas Cartas são : {self.cartas}")
#b= Baralho()        
#x=b.obter_tres()
#l=Jogador()
#l.obter_cartas(x)
#l.ver_cartas()


class Jogo:
    def __init__(self):
        self.rodadas=1
        self.baralho=Baralho()
        self.jogadores=[Jogador(),Jogador()]
        self.mesa={}
        self.resultados={}
    def iniciar(self):
        for jogador in self.jogadores:
            jogador.obter_cartas(self.baralho.obter_tres())
        while(self.rodadas<4):
            print(f"Rodada {self.rodadas}")
            jogadas=[]
            jogadas.append(self.jogadores[0].jogar_carta())
            jogadas.append(self.jogadores[1].jogar_carta())

            self.resultado_rodada(jogadas)
            self.mesa[self.rodadas]=jogadas
            #self.exibir()
            self.rodadas+=1
        self.finalizar()
    def exibir(self):
        print(self.mesa)
    def finalizar(self):
        print("Fim de jogo!")
    def resultado_rodada(self,jogadas):
        for jogada in jogadas:
            for chave,valor in jogada.items():
                print({chave:valor})
                print(self.baralho.cartas.index({chave:valor}))
                for item in self.baralho.cartas:
                    if item.get(chave)!=None:
                        print(f"PASSOU {item.get(chave)}")
                        ###EXISTE UM BUG POIS ESTOU REMOVENDO A CHAVE DA LISTA DE CARTAS ATRAVES DO baralho.POP()
j=Jogo()
j.iniciar()
j.exibir()
