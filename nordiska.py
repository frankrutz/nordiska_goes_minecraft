from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()


mc.setBlocks(-150,0,-150,150,150,150,0)  #air
mc.setBlocks(-150,-1,-150, 150,0,150,2)  #gras - all.

mc.setBlocks(-150,-1,80,150,0,150,8)     #water
mc.setBlocks(0,-1,0,100,0,80,2)          #gras
mc.setBlocks(-150,-1,0,150,0,-20,1)      #stone=street

mc.setBlocks(80,0,20,100,12,60  ,24)     #NORDISKA first and second floor
mc.setBlocks(81,1,21,  99,11,59  , 0)     #air in NORDISKA
mc.setBlocks(84,1,20,   87,4,21 , 0)     #front door opening

mc.setBlock(90,4,20 ,0)     #toilet window boys
mc.setBlock(93,4,20 ,0)     #toilet window girls

mc.setBlocks(81,6,21, 99,6,59   ,1) #first floor
mc.setBlocks(81,6,21, 83,6,29   ,0) #air for stairs

#stairs ground floor
h=0
for y in range(23, 30):
     mc.setBlock(81,h,y,1)#stone y-koordinate
     mc.setBlock(82,h,y,1)#stone y-koordinate
     mc.setBlock(83,h,y,1)#stone y-koordinate     
     h=h+1


mc.player.setTilePos(90, 1, 0)

#make coordinate system
for x in range(0, 10):
     mc.setBlock(x,1,0,2)#gras x-coordinate

for z in range(0, 10):
    mc.setBlock(0,z,0,24)#sandstone z-coordinate

for y in range(0, 10):
     mc.setBlock(0,1,y,1)#stone y-koordinate

