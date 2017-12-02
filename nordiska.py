from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#########################################################################################
def initWorld():
    #mc.setBlocks(-150,0,-150   ,150,150,150 ,0)  #air
    #mc.setBlocks(-150,-1,-150  ,150,0,150   ,2)  #gras - all.
    mc.setBlocks(-150,-1,80    ,150,0,150,8)     #water
    mc.setBlocks(-150,-1,0,150,0,-20,1)          #stone=street

#########################################################################################
def makeRoof(x,z,y):
    for h in range(0,12):
        mc.setBlocks(x+h,z+h  ,y+h    ,x+22-h  ,z+h,y+42-h   ,17)
        if h < 11:
            mc.setBlocks(x+h+1,z+h,y+h+1  ,x+22-1-h,z+h,y+42-h-1 , 0)
######################################################################################### 
def makeStairs(x,z,y,numstairs,width): 
    for s in range(0, numstairs):
        for w in range(0,width):
             mc.setBlock(x+w,z+s,y+s,17)#stone y-koordinate
#########################################################################################
def makeTree(x,z,y):
        mc.setBlocks(x,z,y       ,x+1,z+6,y+1,  17)
        mc.setBlocks(x-3,z+6,y-4 ,x+4,z+26,y+5, 18)
#########################################################################################
def printCoordinateSystem():
    for x in range(0, 10):
         mc.setBlock(x,1,0,2)#gras x-coordinate
    for z in range(0, 10):
        mc.setBlock(0,z,0,24)#sandstone z-coordinate
    for y in range(0, 10):
         mc.setBlock(0,1,y,1)#stone y-koordinate
#########################################################################################
def makeMythenquai():
    for x in range(0,100):  #fence to the street
        mc.setBlock(x,1,0  ,85)
        mc.setBlock(x,2,0  ,85)

    makeTree(96,0,75)  #tree at Nordiska, lakeside
    
    for x in range(0,8):   #trees at the street
        makeTree(x*13,0,4)

    for x in range(0,8):   #trees at the parking space
        makeTree(x*13,0,-20)
#########################################################################################
def makeNordiska():
    mc.setBlocks(80,0,20,100,12,60  ,24)     #NORDISKA first and second floor
    mc.setBlocks(81,1,21,  99,11,59  ,0)     #air in NORDISKA
    mc.setBlocks(84,1,20,   87,4,21  ,0)     #front door opening
    mc.setBlocks(80,7,20,   100,11,23,0)     #front balcony opening
    mc.setBlocks(80,7,57,   100,11,60,0)     #lake  balcony opening


    mc.setBlocks( 80,7,60,  100,7,60,  24)   #lake balcony walls
    mc.setBlocks( 80,7,56,   80,7,60,  24)
    mc.setBlocks(100,7,56,  100,7,60,  24)  

    mc.setBlocks( 80,8,60,  80,11,60,  73)   #pilar lake balcony
    mc.setBlocks( 84,8,60,  84,11,60,  73)   #pilar lake balcony
    mc.setBlocks( 88,8,60,  88,11,60,  73)   #pilar lake balcony
    mc.setBlocks( 92,8,60,  92,11,60,  73)   #pilar lake balcony
    mc.setBlocks( 96,8,60,  96,11,60,  73)   #pilar lake balcony
    mc.setBlocks(100,8,60, 100,11,60,  73)   #pilar lake balcony


    mc.setBlocks( 80,7,20,  100,7,20,  24)   #front balcony walls
    mc.setBlocks( 80,7,20,   80,7,24,  24)
    mc.setBlocks(100,7,20,  100,7,24,  24)

    mc.setBlocks( 80,8,20,  80,11,20,  73)   #pilar front balcony
    mc.setBlocks( 84,8,20,  84,11,20,  73)   #pilar front balcony
    mc.setBlocks( 88,8,20,  88,11,20,  73)   #pilar front balcony
    mc.setBlocks( 92,8,20,  92,11,20,  73)   #pilar front balcony
    mc.setBlocks( 96,8,20,  96,11,20,  73)   #pilar front balcony
    mc.setBlocks(100,8,20, 100,11,20,  73)   #pilar front balcony


    mc.setBlock(90,4,20 ,0)     #toilet window boys
    mc.setBlock(93,4,20 ,0)     #toilet window girls

    mc.setBlocks(81,6,21, 99,6,59   ,1) #first floor


    mc.setBlocks(81,6,24  ,83,6,29   ,0) #air for groundfloor stairs
    makeStairs(81,0,23 ,7,3) #ground floor stairs

    mc.setBlocks(80,7,23,  100,11,23,  24) #outer wall locker room
    mc.setBlocks(89,7,23,   90,10,23,   0) #outer wall door
    mc.setBlocks(84,8,23,   86,10,23,   0) #outer wall window
    mc.setBlocks(93,8,23,   95,10,23,   0) #outer wall window

    mc.setBlocks(84,7,23,   84,12,30  ,24) #inner wall locker room to staircase
    mc.setBlocks(84,7,30,   100,11,30 ,24) #inner wall entry to locker room
    mc.setBlocks(86,7,30,   87,10,30,   0) #inner door to locker room

    mc.setBlocks(84,1,60  ,87,4,60  ,0)   #rowing boat door 1
    mc.setBlocks(93,1,60  ,96,4,60  ,0)   #rowing boat door 2

    for platte in range(0,9):
        mc.setBlock( 94,0,62+platte*2,  1)    #walking plates to the lake

    mc.setBlocks(93,0,80,   95,0,100    ,17)   #boat bridge, wood

    
 
    mc.setBlock(81,4,22,50) #torch at entry
    mc.setBlock(81,5,23,50) #torch at entry
    mc.setBlock(81,6,24,50) #torch at entry
    mc.setBlock(81,7,25,50) #torch at entry
    mc.setBlock(81,8,26,50) #torch at entry
    mc.setBlock(81,9,27,50) #torch at entry

    makeRoof(79,13,19)

    mc.setBlocks(85,12,34 ,87,12,38   ,0) #air for secondfloor stairs
    makeStairs(85,7,33 ,6,3) #stairs to second floor
#########################################################################################
def makeAviron():
    mc.setBlocks(65,0,17,  80,7,57  ,24)    #Aviron first floor
    mc.setBlocks(66,0,18,  79,5,56  ,0)     #air in Aviron
    mc.setBlocks(66,7,18,  79,7,56  ,0)     #air in Aviron
#########################################################################################   

initWorld()
makeMythenquai()
makeNordiska()
makeAviron()






mc.player.setTilePos(85, 1, 60)

