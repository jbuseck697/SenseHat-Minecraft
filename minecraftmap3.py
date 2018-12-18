from mcpi.minecraft import Minecraft

mc = Minecraft.create()


stone = 1
x, y, z = mc.player.getPos()

mc.player.setPos(14, 1, -10)

#clear map
mc.setBlocks(0, 0, 0, x+1000, 1000, z+1000, 0)
mc.setBlocks(0, 0, 0, x+1000, 1000, z-1000, 0)
mc.setBlocks(0, 0, 0, x-1000, 1000, z-1000, 0)
mc.setBlocks(0, 0, 0, x-1000, 1000, z+1000, 0)

#make everything grass
mc.setBlocks(0, 0, 0, x+1000, y-2, z+1000, 2)
mc.setBlocks(0, 0, 0, x+1000, y-2, z-1000, 2)
mc.setBlocks(0, 0, 0, x-1000, y-2, z-1000, 2)
mc.setBlocks(0, 0, 0, x-1000, y-2, z+1000, 2)

#base
mc.setBlocks(5, 0, 5, 22, 1000, 17, 41)

#OpenInside
mc.setBlocks(6, 1, 6, 21, 1000, 16, 0)

#Entrance
mc.setBlocks(13, 1, 5, 14, 2, 5, 0)

#maze
mc.setBlocks(21, 0, 14, 21, 1000, 14, 42)
mc.setBlocks(20, 0, 7, 20, 1000, 12, 42)
mc.setBlocks(18, 0, 6, 18, 1000, 11, 42)
mc.setBlocks(18, 0, 14, 16, 1000, 14, 42)
mc.setBlocks(16, 0, 11, 16, 1000, 13, 42)
mc.setBlocks(16, 0, 7, 14, 1000, 13, 42)
mc.setBlock(14, 0,   8, 42)
mc.setBlocks(16, 0, 9, 11, 1000, 9, 42)
mc.setBlocks(11, 0, 8, 42)
mc.setBlocks(12, 0, 7, 11, 1000, 7, 42)
mc.setBlocks(7, 0, 7, 7, 1000, 7, 42)
mc.setBlocks(11, 0, 11, 11, 1000, 8, 42)
mc.setBlocks(17, 0, 11, 16, 1000, 13, 42)
mc.setBlocks(15, 0, 13, 12, 1000, 13, 42)
mc.setBlocks(12, 0, 14, 12, 1000, 15, 42)
mc.setBlocks(10, 0, 14, 9, 1000, 15, 42)
mc.setBlocks(20, 0, 14, 19, 1000, 14, 42)
mc.setBlocks(17, 0, 12, 11, 1000, 12, 0)
mc.setBlocks(15, 0, 7, 15, 1000, 11, 0)
mc.setBlock(14, 1, 1000, 0)
mc.setBlock(14, 0, 10, 41) 
mc.setBlocks(17, 0, 12, 5, 0, 12, 41)
mc.setBlocks(15, 0, 7, 15, 0, 11, 41)
mc.setBlocks(13, 0, 11, 13, 1000, 11, 42)
mc.setBlocks(9, 0, 7, 7, 1000, 13, 42)
mc.setBlocks(8, 0, 8, 8, 1000, 13, 0)
mc.setBlocks(8, 0, 8, 8, 0, 13, 41)
mc.setBlocks(12, 0, 15, 12, 1000, 15, 0)
mc.setBlocks(12, 0, 15, 12, 0, 15, 41)
mc.setBlocks(13, 0, 16, 13, 1000, 16, 42)
mc.setBlocks(14, 0, 15, 14, 1000, 15, 42)
mc.setBlocks(15, 0, 16, 15, 1000, 16, 42)
mc.setBlocks(14, 1, 17, 14, 2, 17, 0)

#diamonds
mc.setBlock(21, 0, 10, 57)
mc.setBlock(17, 0, 10, 57)
mc.setBlock(12, 0, 8, 57)
mc.setBlock(8, 0, 8, 57)
mc.setBlock(14, 0, 16, 57)
mc.setBlocks(21, 0, 15, 21, 0, 16, 57)

#Intro
mc.postToChat("Hello explorer! Can you find all 7 diamond blocks?")