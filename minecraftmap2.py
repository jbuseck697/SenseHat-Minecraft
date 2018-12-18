from sense_hat import SenseHat
from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()



known_blocks = {}

def get_blocks():
    global known_blocks

    x, y, z = mc.player.getTilePos()
    y -= 1

    blocks = []
    for dz in range(z-3, z+5):
        for dx in range(x-3, x+5):
            b = (dx, y, dz)
            if b in known_blocks:
                block = known_blocks[b]
            else:
                block = mc.getBlock(dx, y, dz)
                known_blocks[b] = block
            blocks.append(block)

    return blocks

def lookup_color(block):
    if block in colors:
        return colors[block]
    else:
        return white

def map_blocks_to_colors(blocks):
    return [lookup_color(block) for block in blocks]

# blocks
grass = 2
    
diamond = 57
    
gold = 41
    
iron = 42

air = 0
# colors
cyan = (0, 255, 255)

yellow = (255, 255, 0)

white = (255, 255, 255)

black = (0, 0, 0)

# block: color
colors = {
     grass: black,
    diamond: cyan,
    gold: yellow,
    iron: white,
    air: black,
}

player_pos = 27

while True:
    blocks = get_blocks()
    pixels = map_blocks_to_colors(blocks)
    pixels[player_pos] = black  # denote player as black pixel
    sense.set_pixels(pixels)
    