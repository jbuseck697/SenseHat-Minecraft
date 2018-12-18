from sense_hat import SenseHat

from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()

#blocks
grass = 2
    
diamond = 57
    
gold = 41
    
iron = 42

#colors
cyan = (0, 255, 255)

yellow = (255, 255, 0)

white = (255, 255, 255)

black = (0, 0, 0)
#block clors
colors = {
    grass: black,
    diamond: cyan,
    gold: yellow,
    iron: white,
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
    