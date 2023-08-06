from mcpi.minecraft import *
mc = Minecraft.create()

def saudacao(nome):
    return f"Olá, {nome}!"



def colocarBloco(x,y,z,id_bloco,estado):
    mc.setBlock(x,y,z,id_bloco,estado) 


def colocarBlocos(x0,y0,z0,x1,y1,z1,id_bloco,estado):
    mc.setBlocks(x0,y0,z0,x1,y1,z1,id_bloco,estado)

def pegarBloco(x,y,z):
    mc.getBlock(x,y,z)


def mandarMensagem(mensagem):
    mc.postToChat(mensagem)


def pegarPosicaoJogador():
    mc.player.getPos()


def novaPosicaoJogador(x,y,z):
    """
    novaPosicaoJogador(x,y,z)

    Coloca o jogador em uma nova posição no mundo do Minecraft.
    """
    mc.player.setPos(x,y,z)


def pegarBlocosTocados():
    mc.events.pollBlockHits()
