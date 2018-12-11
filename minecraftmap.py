from sense_hat import SenseHat

from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()

mc.postToChat("Hello Minecraft!")
sense.clear(0, 255, 0)
