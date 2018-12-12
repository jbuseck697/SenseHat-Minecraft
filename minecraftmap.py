from sense_hat import SenseHat

from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()

while True:
    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)
    print(block)
    sleep(0.1)
    