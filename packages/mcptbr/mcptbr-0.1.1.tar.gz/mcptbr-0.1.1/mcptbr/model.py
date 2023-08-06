from mcpi.minecraft import *


def saudacao(nome):
    return f"Olá, {nome}!"


def posicao(x,y,z):
    mc = Minecraft.create()

    mc.player.setPos(x,y,z)