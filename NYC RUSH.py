


                                                                                                                                                                                                                                                               #Gamers2303
#New York Rush
#Adriana,Briget,Rosario,Jozka
#
from gamelib import*#import game library
game = Game(800,600,"New York Rush")

#title
title = Image("title.png",game)
title.y -= 150

#bk
bk = Image("Backup Cover.jpg",game)#Image Object
bk.resizeTo(800,600)
game.setBackground(bk)

#BK- Level 1
bk1 = Image("NYC.jpg",game)
bk1.resizeTo(800,600)

#bm
bm = Image("BM1.gif",game)
bm.resizeTo(50,40)
bm.moveTo(50,513)
bm.resizeBy(330)

#tc
tc = []
for index in range(20):
    tc.append(Image("tc.png",game))
for index in range(20):
    x = randint(900,4000)  
    tc[index].resizeBy(-90)
    tc[index].moveTo(x, 550)
    tc[index].setSpeed(5,90)

#You Win
yw = Image("YW.png",game)
yw.moveTo(405,150)

    
    

#elderly
elderly = Image("elderly.png",game)
elderly.resizeTo(30,40)
elderly.moveTo(470,513)
elderly.resizeBy(330)

#play
play = Image("play.png",game)
play.moveTo(550,20)
play.resizeBy(-40)
play.y += 200

#END
end = Image ("end.jpg",game)
end.resizeTo(800,600)

#gameover
gameover = Image ("gameover.png",game)
gameover.moveTo(405,150)


jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

#Title Screen - first game loop
while not game.over:
    game.processInput()

    bk.draw()
    play.draw()
    title.draw()
    

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False
#Level 1
tcPassed = 0
while not game.over:
    game.processInput()

    bk1.draw()
    bm.draw()

    #tc
    for index in range(20):
        tc[index].move()
        if tc[index].collidedWith(bm):
            bm.health -=1
        if tc[index].isOffScreen("left") and tc[index].visible:
            tcPassed += 1
            tc[index].visible = False

        if tcPassed >= 20:
            end.draw()
            yw.draw()
            game.drawText("YOU WIN!",100,5)
            

        if tc[index].isOffScreen("left"):
            x = randint(900,4000)  
            tc[index].moveTo(x, 550)
            
            
            
            

        
        if bm.health <0:         
            end.draw()
            gameover.draw()
            game.drawText("YOU LOSE!",100,5)
            


       
            
            
           

    


    

#jumping
    if bm.y< 400:
        landed = False#not landed
        #if bm.collidedWith(platform,"rectangle"):
            #landed = True
    else:
        landed = True

    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
        bm.y -=40*factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .12:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
        
    if not landed:
        bm.y +=17#adjust as needed
#bm keys 
    if keys.Pressed[K_RIGHT]:
        bm.x += 8
    if keys.Pressed[K_LEFT]:
        bm.x -= 8


    game.drawText("Health: " + str(bm.health) , bm.x-20, bm.y+50)


   
    game.update(30)

    





    
    
    game.update(60)
game.quit()

