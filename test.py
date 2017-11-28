from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.setTilePos(0, 50, 100)
position = mc.player.getTilePos()
mc.setBlock(position.x,position.y,position.z,10)

