import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((300,300))
screen.fill([255,255,255])

#draw lines
pygame.draw.line(screen,(0,0,0),(100,300),(100,0))
pygame.draw.line(screen,(0,0,0),(200,300),(200,0))
pygame.draw.line(screen,(0,0,0),(300,100),(0,100))
pygame.draw.line(screen,(0,0,0),(300,200),(0,200))

#set up game data
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#get wining combos
wins = []
#rows and collums
for x in range(0,3):
    wins.append([[x,0],[x,1],[x,2]])
for y in range(0,3):
    wins.append([[0,y],[1,y],[2,y]])
#diagonals
wins.append([[0,0],[1,1],[2,2]])
wins.append([[0,2],[1,1],[2,0]])
#make all combos
wins2 = []
for mix in wins:
    wins2.append([mix[0],mix[2],mix[1]])
    wins2.append(mix)
    wins2.append([mix[1],mix[0],mix[2]])
    wins2.append([mix[1],mix[2],mix[0]])
    wins2.append([mix[2],mix[1],mix[0]])
    wins2.append([mix[2],mix[0],mix[1]])
wins = wins2

AIs = []
PLAYERs = []

def checkwin():
    global AIs
    global PLAYERs
    global board
    global wins
    for P1 in PLAYERs:
        for P2 in PLAYERs:
            for P3 in PLAYERs:
                if [P1,P2,P3] in wins:
                    pygame.time.delay(1000)
                    pygame.quit()
                    print "         YOU WON!        "
    for AI1 in AIs:
        for AI2 in AIs:
            for AI3 in AIs:
                if [AI1,AI2,AI3] in wins:
                    pygame.time.delay(1000)
                    pygame.quit()
                    print "         YOU LOST!        "
                    print "   WORSE LUCK NEXT TIME!"
    #check if it is a tie
    full = 1
    for tester1 in board:
        for tester2 in tester1:
            if tester2 == 0:
                full = 0
    if full == 1:
        pygame.time.delay(1000)
        pygame.quit()
        print "         YOU TIED!        "
        
                        
        
#define moves
def move(side, pos):
    board[pos[1]][pos[0]] = side
    pygame.draw.rect(screen,(side*100,0,side*100),(pos[0]*100,pos[1]*100,100,100))
    if side == 2:
        AIs.append(pos)
    if side == 1:
        PLAYERs.append(pos)

def moveAI():
    mover = [1,1]
    while board[mover[1]][mover[0]] != 0:
        mover = [random.randint(0,2),random.randint(0,2)]
        try:
            thingymibober = board[mover[1]][mover[0]]
        except:
            mover = [1,1]
    advantage = 0
    for ysquare in board:
        for xsquare in ysquare:
            curadvantage = 0
            for AI1 in AIs:
                for ysquare2 in board:
                    for xsquare2 in ysquare2:
                        if AI1!=[ysquare2.index(xsquare2),board.index(ysquare2)] and AI1!=[ysquare.index(xsquare),board.index(ysquare)]:
                            if ysquare[ysquare.index(xsquare)] == 0 and ysquare2[ysquare2.index(xsquare2)] == 0:
                                combo = [AI1,[ysquare2.index(xsquare2),board.index(ysquare2)],[ysquare.index(xsquare),board.index(ysquare)]]
                                if combo in wins:
                                    curadvantage += 1
                                    if curadvantage > advantage:
                                        mover = [ysquare.index(xsquare),board.index(ysquare)]
                                        advantage = curadvantage
    for ysquare in board:
        for xsquare in ysquare:
            if ysquare[ysquare.index(xsquare)] == 0:
                for AI1 in PLAYERs:
                    for AI2 in PLAYERs:
                        if AI1!=AI2:
                            combo = [AI1,AI2,[ysquare.index(xsquare),board.index(ysquare)]]
                            if combo in wins:
                                mover = [ysquare.index(xsquare),board.index(ysquare)]
    for ysquare in board:
        for xsquare in ysquare:
            if ysquare[ysquare.index(xsquare)] == 0:
                for AI1 in AIs:
                    for AI2 in AIs:
                        if AI1!=AI2:
                            combo = [AI1,AI2,[ysquare.index(xsquare),board.index(ysquare)]]
                            if combo in wins:
                                mover = [ysquare.index(xsquare),board.index(ysquare)]
    move(2,mover)

pygame.display.flip()
pygame.time.delay(500)
if raw_input("would you like to go first? (y/n)") == 'n':
    moveAI()                                
while True:
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[int(mousepos[1]/100)][int(mousepos[0]/100)] == 0:
                move(1,[int(mousepos[0]/100),int(mousepos[1]/100)])
                pygame.display.flip()
                checkwin()
                moveAI()
                pygame.display.flip()
                checkwin()
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
