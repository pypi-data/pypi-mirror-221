from mcpi import *


def saudacao(nome):
    return f"Olá, {nome}!"


def posicao(x,y,z):
    mc = mcpi.minecraft.create()

    mc.player.setPos(x,y,z)