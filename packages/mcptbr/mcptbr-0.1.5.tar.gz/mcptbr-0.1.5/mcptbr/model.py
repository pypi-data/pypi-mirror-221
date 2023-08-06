from mcpi.minecraft import *

try:
    mc = Minecraft.create()

except:
    print("Erro: Servidor de minecraft não está aberto.")


def colocarBloco(x,y,z,id_bloco,estado):
    """
    colocarBloco(x,y,z,id_bloco,estado)

    Coloca um bloco que desejar pelo mapa.
    """
    try:
        mc.setBlock(x,y,z,id_bloco,estado) 
    except:
        print("Erro: Preenchar todos os campos da função. /n colocarBloco(x,y,z,id_bloco,estado)")

def colocarBlocos(x0,y0,z0,x1,y1,z1,id_bloco,estado):
    """
    colocarBlocos(x0,y0,z0,x1,y1,z1,id_bloco,estado)

    Coloca mais de um bloco em qualquer lugar pelo mapa.
    """
    try: 
        mc.setBlocks(x0,y0,z0,x1,y1,z1,id_bloco,estado)
    except:
        print("Erro: Preenchar todos os campos da função. /n colocarBlocos(x0,y0,z0,x1,y1,z1,id_bloco,estado)")

def pegarBloco(x,y,z):
    """
    pegarBloco(x,y,z)

    Pega o ID de um bloco pelo mapa.
    """

    try:
        return mc.getBlock(x,y,z)
    except:
        print("Erro: Preenchar todos os campos da função. /n pegarBloco(x,y,z)")

def mandarMensagem(mensagem):
    """
    mandarMensagem(mensagem)

    Envia uma mensagem no chat do Minecraft.
    """

    try:
        mc.postToChat(mensagem)
    except:
        print("Erro: Preenchar todos os campos da função. /n mandarMensagem(mensagem)")


def pegarPosicaoJogador():
    """
    pegarPosicaoJogador()

    Coloque o bloco que desejar pelo mapa.
    """
    try:
        return mc.player.getPos()
    except:
        print("Erro: pegarPosicaoJogador()")



def novaPosicaoJogador(x,y,z):
    """
    novaPosicaoJogador(x,y,z)

    Coloca o jogador em uma nova posição no mundo do Minecraft.
    """
    try:
        mc.player.setPos(x,y,z)
    except:
        print("Erro: Preenchar todos os campos da função. /n novaPosicaoJogador(x,y,z)")



def pegarBlocosTocados():
    """
    pegarBlocosTocados()

    pega a coordenada e o ID do bloco tocado por uma espada. 
    Observação: Só funciona com espadas.
    """

    try:
        return mc.events.pollBlockHits()
    except:
        print("Erro: pegarBlocosTocados()")