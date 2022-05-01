import pygame
import time
import sys
import threading

scoreA = 0
scoreB = 0

BLACK = (0,0,0)

class pungle(pygame.sprite.Sprite):

    def __init__(self, link):
        super().__init__()

        self.image = pygame.image.load(link)
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def RightA(self,pixels):
        self.rect.x += pixels

    def LeftA(self,pixels):
        self.rect.x -= pixels

    def RightB(self,pixels):
        self.rect.x += pixels


    def LeftB(self,pixels):
        self.rect.x -= pixels

    def imageChange(self, link):
        self.image = pygame.image.load(link)

    def hit(self, ataker):
        atakers = pygame.mask.from_surface(ataker.image)
        if pygame.sprite.collide_mask(ataker, self):

            beamB.rect.x = -2000
            beamA.rect.x = 2000
            global rounded
            rounded += 1

            global scoreChk
            scoreChk = True

            if ataker == beamA:
                global scoreA
                scoreA += 1
            if ataker == beamB:
                global scoreB
                scoreB += 1

            global changAt
            changAt = not changAt

            global eatA1
            global eatB1
            global eatA
            global eatB

            if ataker == beamA:
                if gibonB == True:
                    if eatB < 3:
                        pungleB.imageChange("imgs/pangs_eat.gif")
                    elif eatB >= 3:
                        pungleB.imageChange("imgs/pangs_eat1.gif")
                if juguckB == True:
                    if eatB < 3:
                        pungleB.imageChange("imgs/sn_s_eat.gif")
                    elif eatB >=  3:
                        pungleB.imageChange("imgs/sn_s_eat (1).gif")
                if dobalB == True:
                    if eatB < 3:
                        pungleB.imageChange("imgs/db_s_eat.gif")
                    elif eatB >= 3:
                        pungleB.imageChange("imgs/db_s_eat1.gif")
                if deapoB == True:
                    if eatB < 3:
                        pungleB.imageChange("imgs/hl_s_eat.gif")
                    elif eatB >= 3:
                        pungleB.imageChange("imgs/hl_b_eat1.gif")
                armB = 5
                armA = 0
                eatB += 1

            if ataker == beamB:
                if gibonA == True:
                    if eatA < 3:
                        pungleA.imageChange("imgs/pangc_eat.gif")
                    elif eatA >=  3:
                        pungleA.imageChange("imgs/pangc_eat1.gif")
                if juguckA == True:
                    if eatA < 3:
                        pungleA.imageChange("imgs/sn_c_eat.gif")
                    elif eatA >= 3:
                        pungleA.imageChange("imgs/sn_c_eat (1).gif")
                if dobalA == True:
                    if eatA < 3:
                        pungleA.imageChange("imgs/db_c_eat.gif")
                    elif eatA >= 3:
                        pungleA.imageChange("imgs/db_c_eat1.gif")
                if deapoA == True:
                    if eatA < 3:
                        pungleA.imageChange("imgs/hl_c_eat.gif")
                    elif eatA >= 3:
                        pungleA.imageChange("imgs/hl_c_eat1.gif")
                armB = 0
                armA = 5
                eatA += 1

class Beam(pygame.sprite.Sprite):
    global dobalA
    global juguckA
    global deapoA
    global gibonA
    global dobalB
    global juguckB
    global deapoB
    global gibonB

    def __init__(self, link):
        super().__init__()

        self.image = pygame.image.load(link)
        self.rect = self.image.get_rect()

    def moveLeft(self):
        global atchA;
        global armA
        global armAC
        if atchA == False:
            beamA.rect.x = pungleA.rect.x + 70;
            beamA.rect.y = pungleA.rect.y + 25;
            atchA = True;
        if armAC == False:
            beamsound.play()
            armA -= 1
            armAC = True

    def moveRight(self):
        global atchB;
        global armB
        global armBC
        if atchB == False:
            beamB.rect.x = pungleB.rect.x - 10;
            beamB.rect.y = pungleB.rect.y + 25;
            atchB = True;
        if armBC == False:
            beamsound.play()
            armB -= 1
            armBC = True

class MainScreen:
    def __init__(self):
        ms = pygame.image.load("imgs/back1.gif")
        while True:
            screen.fill(BLUE)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        global chak
                        chak = True
                        break
                    if event.key==pygame.K_y:
                        global story
                        story = True
            if story == True:
                StoryScreen();
            if st_pl == True:
                break


            screen.blit(ms, (0,0))
            pygame.display.update()

class StoryScreen:
    def __init__(self):
        ms = pygame.image.load("imgs/story.gif")
        while True:
            screen.fill(BLUE)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        global chak
                        chak = True
                        global story
                        story = False
                        global st_pl
                        st_pl = True
                        break
                    if event.key==pygame.K_y:
                        story = False
                        break

            screen.blit(ms, (0,0))
            pygame.display.update()

class AWin:
    global dobalA
    global juguckA
    global deapoA
    global gibonA
    def __init__(self):
        if gibonA == True:
            ms = pygame.image.load("imgs/win_c.gif")
        if juguckA == True:
            ms = pygame.image.load("imgs/win_sn_c clone.gif")
        if deapoA == True:
            ms = pygame.image.load("imgs/win_hl_c.gif")
        if dobalA == True:
            ms = pygame.image.load("imgs/win_db_c.gif")
        pygame.mixer.music.stop()
        winsound.play()
        while True:
            screen.fill(RED)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        global chak
                        chak = False
                        break
            font = pygame.font.Font(None, 74)
            text = font.render("replay : x", 1, BLACK)
            screen.blit(ms, (0,0))
            screen.blit(text, (0,0))
            pygame.display.update()

class BWin:
    global dobalB
    global juguckB
    global deapoB
    global gibonB
    def __init__(self):
        if gibonB == True:
            ms = pygame.image.load("imgs/win_s.gif")
        if juguckB == True:
            ms = pygame.image.load("imgs/win_sn_s.gif")
        if deapoB == True:
            ms = pygame.image.load("imgs/win_hl_s.gif")
        if dobalB == True:
            ms = pygame.image.load("imgs/win_db_s.gif")
        pygame.mixer.music.stop()
        winsound.play()
        while True:
            screen.fill(RED)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        global chak
                        chak = False
                        break
            font = pygame.font.Font(None, 74)
            text = font.render("replay : x", 1, BLACK)
            screen.blit(ms, (0,0))
            screen.blit(text, (750,0))
            pygame.display.update()

class CharChoose:
    def __init__(self):
        global dobalA
        global juguckA
        global deapoA
        global gibonA
        global dobalB
        global juguckB
        global deapoB
        global gibonB
        global charA
        global charB
        asd = "imgs/ch_pang.gif"
        dsa = "imgs/ch_pang.gif"
        while True:
            screen.fill(RED)
            if charA == True and charB == True:
                    break;
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        if charA == False:
                            if gibonA == True:
                                juguckA = True
                                gibonA = False
                                asd = "imgs/ch_sn.gif"
                                continue
                            if juguckA == True:
                                dobalA = True
                                juguckA = False
                                asd = "imgs/ch_db.gif"
                                continue
                            if dobalA == True:
                                deapoA = True
                                dobalA = False
                                asd = "imgs/ch_hellchang.gif"
                                continue
                            if deapoA == True:
                                gibonA = True
                                deapoA = False
                                asd = "imgs/ch_pang.gif"
                                continue
                    if event.key==pygame.K_RETURN:
                        if charB == False:
                            if gibonB == True:
                                juguckB = True
                                gibonB = False
                                dsa = "imgs/ch_sn.gif"
                                continue
                            if juguckB == True:
                                dobalB = True
                                juguckB = False
                                dsa = "imgs/ch_db.gif"
                                continue
                            if dobalB == True:
                                deapoB = True
                                dobalB = False
                                dsa = "imgs/ch_hellchang.gif"
                                continue
                            if deapoB == True:
                                gibonB = True
                                deapoB = False
                                dsa = "imgs/ch_pang.gif"
                                continue

                    if event.key==pygame.K_q:
                        charA = not charA
                        if gibonA == True:
                            asd = "imgs/ck_pang.gif"

                        if juguckA == True:
                            asd = "imgs/ck_sn.gif"

                        if deapoA == True:
                            asd = "imgs/ck_hellchang.gif"

                        if dobalA == True:
                            asd = "imgs/ck_db.gif"

                    if event.key==pygame.K_RSHIFT:
                        charB = not charB
                        if gibonB == True:
                            dsa = "imgs/ck_pang.gif"

                        if juguckB == True:
                            dsa = "imgs/ck_sn.gif"

                        if deapoB == True:
                            dsa = "imgs/ck_hellchang.gif"

                        if dobalB == True:
                            dsa = "imgs/ck_db.gif"


            font = pygame.font.Font(None, 100)
            font1 = pygame.font.Font(None, 50)

            text = pygame.image.load(asd)
            text1 = pygame.image.load(dsa)
            ms = pygame.image.load("imgs/ch_back.gif")
            text3 = font1.render("change : space, enter", 1, BLACK)
            text4 = font1.render("pick : q, shift", 1, BLACK)
            screen.blit(text3, (430,10))
            screen.blit(ms, (0,0))
            screen.blit(text, (200,100))
            screen.blit(text1, (550,100))
            screen.blit(text3, (300,400))
            screen.blit(text4, (380,450))

            pygame.display.update()



BLACK = (0, 0, 0)

BLUE = (0, 0, 255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

size = (1000, 500)
screen = pygame.display.set_mode(size)

back = pygame.image.load("imgs/back.gif")

pungleA = pungle("imgs/pangc.gif")

pungleB = pungle("imgs/pangs.gif")

beamA = Beam("imgs/pish1.png")
beamA.rect.x = 2000

beamB = Beam("imgs/pish.png")
beamB.rect.x = -2000


global changAt
changAt = False

global scoreChk
scoreChk = False

global chak
chak = False

global gamestart
gamestart = False

global atchA
atchA = False

global atchB
atchB = False

global story
story = False

global main
main = False

global st_pl
st_pl = False

global eatA
eatA = 0;

global eatB
eatB = 0;

global eatA1
eatA1 = False;

global eatB1
eatB1 = False;

dobalA = False
juguckA = False
deapoA = False
gibonA = True

dobalB = False
juguckB = False
deapoB = False
gibonB = True

global charA
charA = False
global charB
charB = False

global armA
armA = 0
global armB
armB = 0

global armAC
armAC = False
global armBC
armBC = True

all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(pungleA)
all_sprites_list.add(pungleB)
all_sprites_list.add(beamA)
all_sprites_list.add(beamB)

clock = pygame.time.Clock()

count = 10

global rounded
rounded = 0


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music/pangpang.mp3")
pygame.display.set_caption("PangShoot")
beamsound = pygame.mixer.Sound("music/BEAMM.wav")
winsound = pygame.mixer.Sound("music/win.wav")
def startTimer():
    global count
    global timer
    timer = threading.Timer(1, startTimer)
    timer.start()
    print(count)
    count -= 1

while True:
    if chak == False:
        charA = False
        charB = False
        eatB = 0
        eatA = 0

        dobalA = False
        juguckA = False
        deapoA = False
        gibonA = True

        dobalB = False
        juguckB = False
        deapoB = False
        gibonB = True
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/pangpang.mp3")
        pygame.mixer.music.play(-1)
        MainScreen();
        CharChoose();
        if gibonA == True:
            pungleA.imageChange("imgs/pangc.gif")
        if gibonB == True:
            pungleB.imageChange("imgs/pangs.gif")
        if juguckA == True:
            pungleA.imageChange("imgs/sn_c.gif")
        if juguckB == True:
            pungleB.imageChange("imgs/sn_s.gif")
        if dobalA == True:
            pungleA.imageChange("imgs/db_c.gif")
        if dobalB == True:
            pungleB.imageChange("imgs/db_s.gif")
        if deapoA == True:
            pungleA.imageChange("imgs/hl_c.gif")
        if deapoB == True:
            pungleB.imageChange("imgs/hl_s.gif")

        eatA1 = False
        eatB1 = False

        scoreA = 0
        scoreB = 0
        rounded = 0
        count = 10
        changAt = False

        pungleA.rect.x = 100
        pungleA.rect.y = 200

        pungleB.rect.x = 800
        pungleB.rect.y = 200


        beamA.rect.x = 2000
        beamB.rect.x = -2000
        startTimer()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/pangjun.mp3")
        pygame.mixer.music.play(-1)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        timer.cancel()
        pygame.quit()
    elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                timer.cancel()
                break

    if scoreChk == True:

        timer.cancel()
        pygame.mixer.music.stop()
        time.sleep(3)
        pygame.mixer.music.play(-1)
        if gibonA == True:
            pungleA.imageChange("imgs/pangc.gif")
        if gibonB == True:
            pungleB.imageChange("imgs/pangs.gif")
        if juguckA == True:
            pungleA.imageChange("imgs/sn_c.gif")
        if juguckB == True:
            pungleB.imageChange("imgs/sn_s.gif")
        if dobalA == True:
            pungleA.imageChange("imgs/db_c.gif")
        if dobalB == True:
            pungleB.imageChange("imgs/db_s.gif")
        if deapoA == True:
            pungleA.imageChange("imgs/hl_c.gif")
        if deapoB == True:
            pungleB.imageChange("imgs/hl_s.gif")

        pungleA.rect.x = 100
        pungleA.rect.y = 200

        pungleB.rect.x = 800
        pungleB.rect.y = 200

        beamA.rect.x = 2000
        beamB.rect.x = -2000

        count = 10

        scoreChk = False

        startTimer()

    if eatA >= 3:
        if gibonA == True:
            pungleA.imageChange("imgs/pangc1.gif")
        if juguckA == True:
            pungleA.imageChange("imgs/sn_c1.gif")
        if dobalA == True:
            pungleA.imageChange("imgs/db_c1.gif")
        if deapoA == True:
            pungleA.imageChange("imgs/hl_c1.gif")
        eatA1 = True;

    if eatB >= 3:
        if gibonB == True:
            pungleB.imageChange("imgs/pangs1.gif")
        if juguckB == True:
            pungleB.imageChange("imgs/sn_s (1).gif")
        if dobalB == True:
            pungleB.imageChange("imgs/db_s1.gif")
        if deapoB == True:
            pungleB.imageChange("imgs/hl_s1.gif")
        eatB1 = True;

    if count < 1:
        count = 10;
        beamB.rect.x = -2000
        beamA.rect.x = 2000
        if changAt == False:
            changAt = True;
            armB = 5
            armA = 0
        else:
            changAt = False;
            armB = 0
            armA = 5
    if armB == 0 and  changAt == True:
        changAt = False
        armA = 5
        count = 10
    if armA == 0 and  changAt == False:
        changAt = True
        armB = 5
        count = 10
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        pungleA.moveUp(10)
    if keys[pygame.K_s]:
        pungleA.moveDown(10)
    if keys[pygame.K_UP]:   
        pungleB.moveUp(10)
    if keys[pygame.K_DOWN]:
        pungleB.moveDown(10)
    if keys[pygame.K_a]:
        pungleA.LeftA(10)
    if keys[pygame.K_d]:
        pungleA.RightA(10)
    if keys[pygame.K_LEFT]:
        pungleB.LeftB(10)
    if keys[pygame.K_RIGHT]:
        pungleB.RightB(10)
    if keys[pygame.K_SPACE]:
        if changAt == False:
            beamA.moveLeft()
    if keys[pygame.K_RETURN]:
        if changAt == True:
            beamB.moveRight()


    if scoreA == 5:
        timer.cancel()
        AWin();
    elif scoreB == 5:
        timer.cancel()
        BWin();

    if atchA == True:
        beamA.rect.x += 30;
        if beamA.rect.x >= 1000:
            beamA.rect.x = 2000;
            atchA = False;
            armAC = False

    if atchB == True:
        beamB.rect.x -= 30;
        if beamB.rect.x <= 0:
            beamB.rect.x = 2000;
            atchB = False;
            armBC = False

    if pungleA.rect.y < -30:
        pungleA.imageChange("imgs/waterc.gif")
        scoreChk = True
        scoreB += 1
        rounded += 1

        if changAt == False:
            changAt = True;
        else:
            changAt = False;

    elif pungleA.rect.y > 400 or pungleA.rect.x < 30 or pungleA.rect.x > 440:
        pungleA.imageChange("imgs/waters.gif")

        scoreChk = True
        scoreB += 1
        rounded += 1

        if changAt == False:
            changAt = True;
        else:
            changAt = False;

    if pungleB.rect.y < -30:
        pungleB.imageChange("imgs/waters.gif")
        scoreChk = True
        scoreA += 1
        rounded += 1

        if changAt == False:
            changAt = True;
        else:
            changAt = False;
    elif pungleB.rect.y > 400 or pungleB.rect.x < 500 or pungleB.rect.x > 880:
        pungleB.imageChange("imgs/waters.gif")

        scoreChk = True
        scoreA += 1
        rounded += 1

        if changAt == False:
            changAt = True;
        else:
            changAt = False;


    pungleB.hit(beamA)
    pungleA.hit(beamB)

    screen.blit(back, (0, 0))

    all_sprites_list.update()


    all_sprites_list.draw(screen)


    font = pygame.font.Font(None, 74)

    text = font.render(str(scoreA), 1, BLACK)
    screen.blit(text, (430,10))

    text = font.render(str(scoreB), 1, BLACK)
    screen.blit(text, (550,10))

    text = font.render(str(count), 1, BLACK)
    screen.blit(text, (485,390))
    
    text = font.render(str("Have fish"), 1, BLACK)
    screen.blit(text, (150,450))

    text = font.render(str(armA), 1, BLACK)
    screen.blit(text, (450,450))

    text = font.render(str(armB), 1, BLACK)
    screen.blit(text, (530,450))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
