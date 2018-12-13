from sense_hat import SenseHat

from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()

#blocks
grass = 2

water = 9

sand = 12

#colors
green = (0, 255, 0)

blue = (0, 0, 255)

yellow = (255, 255, 0)

#block clors
colors = {
    grass: green,
    water: blue,
    sand: yellow,
}


while True:
    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)
    
    if block in colors:
        color = colors[block]
        sense.clear(color)
    else:
        print("Dont't know block ID %s" % block)
    sleep(0.1)
    