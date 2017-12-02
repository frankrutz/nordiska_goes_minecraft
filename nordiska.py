from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def makeRoof(x,z,y):
    for h in range(0,12):
        mc.setBlocks(x+h,z+h  ,y+h    ,x+22-h  ,z+h,y+42-h   ,17)
        if h < 11:
            mc.setBlocks(x+h+1,z+h,y+h+1  ,x+22-1-h,z+h,y+42-h-1 , 0)
  
def makeStairs(x,z,y,numstairs,width): 
    for s in range(0, numstairs):
        for w in range(0,width):
             mc.setBlock(x+w,z+s,y+s,1)#stone y-koordinate
    
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


mc.setBlocks(81,6,21  ,83,6,29   ,0) #air for groundfloor stairs
makeStairs(81,0,23 ,7,3) #ground floor stairs

makeRoof(79,13,19)

mc.setBlocks(85,12,34 ,87,12,38   ,0) #air for secondfloor stairs
makeStairs(85,7,33 ,6,3) #stairs to second floor








mc.player.setTilePos(90, 1, 15)

#make coordinate system
for x in range(0, 10):
     mc.setBlock(x,1,0,2)#gras x-coordinate

for z in range(0, 10):
    mc.setBlock(0,z,0,24)#sandstone z-coordinate

for y in range(0, 10):
     mc.setBlock(0,1,y,1)#stone y-koordinate
