import os
import random
import pygame
last = True
pygame.init()
pygame.font.init()
score = 0
best = 0



if os.path.exists("My_Text_File.txt"):
    file = open("My_Text_File.txt", "r")
    for i in file:
        if i == "coolglasses31!":
            admin = True
        else:
            admin = False
else:
    admin = False




screen_width = 600
screen_height = 600
background_colour = ('black')
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("PYTHON RNG")  
screen.fill(background_colour) 
running = True

img = pygame.image.load("roll.png")
img = pygame.transform.scale(img, (200, 50))
rect = img.get_rect()
rect.center = (300,500)
screen.blit(img, rect)




img2 = pygame.image.load("blank.png")
img2 = pygame.transform.scale(img2, (200, 50))
rect2 = img.get_rect()
rect2.center = (0,500)
screen.blit(img2, rect2)


def rarity( size1, size2, file1, x , y):
    image = pygame.image.load(file1)
    image = pygame.transform.scale(image, (size1,size2))
    screen.blit(image, (x, y))
rarity(50,100, "blank.png", 0, 30)


rotating = ["legendary.png","rare.png", "good.png", "uncommon.png", "common.png"]
transx = [300, 150, 150, 300, 200]
imgx = [159,225, 225, 165, 200]



if admin == True:
    luck = 250
else:
    luck = 1
score = 1

def auto_roll():
    global score
    global best
    global luck
    global last

    if not score == 1:
        last = False

    
    score += 1
    pygame.display.flip() 

    fast = 100
    for i in range(3):
        for i in range(len(rotating)):
            rarity(transx[i], 100, rotating[i], imgx[i], 200) 
            pygame.display.flip()
            rarity(500,200, "blank.png", 165,200)
            pygame.time.delay(fast)
        

        
        fast += 100
    rarity(500,200, "blank.png", 165,200) 




    Roll = random.randint(1,round(250/luck))
    pygame.time.delay(400)
    if Roll == 1:
        rarity(500,200, "blank.png", 165,200) 
        points = ("1/250")
        rarity(300,100, "legendary.png", 159, 200) 
        pygame.display.flip()
        pygame.time.wait(1000)
        rarity(500,200, "blank.png", 165,200) 
        pygame.display.flip()
        best = "1/250"
    
    else:
            
        Roll = random.randint(1,round(25/luck))
        if Roll == 1:
            
            rarity(500,200, "blank.png", 165,200) 
            points = ("1/25")
            rarity(150,100, "rare.png", 225, 200) 
            pygame.display.flip()
            pygame.time.wait(1000)
            rarity(500,200, "blank.png", 165,200) 
            pygame.display.flip()
            if not best == "1/250":
                best = "1/25"
    
        else:
            Roll = random.randint(1,round(10/luck))
            if Roll == 1:
                rarity(500,200, "blank.png", 165,200) 
                points = ("1/10")
                rarity(150,100, "good.png", 225, 200) 
                pygame.display.flip()
                pygame.time.wait(1000)
                rarity(500,200, "blank.png", 165,200) 
                pygame.display.flip()
                if best == 0 or best == "1/2" or best == "1/5":
                    best = "1/10"
            else:
                Roll = random.randint(1,round(5))
                if Roll == 1:   
                    rarity(500,200, "blank.png", 165,200) 
                    points = ("1/5")
                    rarity(300,100, "uncommon.png", 165,200) 
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    rarity(500,200, "blank.png", 165,200) 
                    pygame.display.flip()
                    if best == 0 or best == "1/2":
                        best = "1/5"
                else:
                    rarity(500,200, "blank.png", 165,200) 
                    points = ("1/2")
                    rarity(200,100, "common.png", 200,200)  
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    rarity(500,200, "blank.png", 165,200) 
                    pygame.display.flip()
                    if best == 0 or best == "1/2":
                        best = "1/2"
    last = True                    
while running:
    if score%25 == 0:
        luck += 1
        pygame.time.wait(1000) 
    if admin != True and luck > 10:
        luck = 10

    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if last == True: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 or 2:
                        mouse_position = pygame.mouse.get_pos()
                        if rect.collidepoint(mouse_position):
                                auto_roll()
                                last = True




    score_text = font.render(f'Rolls: {score}', True, (255, 255, 255))
    rarity(500,200, "blank.png", 10,10) 
    screen.blit(score_text, (10,10))
    
    #pygame.display.flip() 

    best_text = font2.render(f'Best: {best}', True, (255, 255, 255))
    rarity(500,200, "blank.png", 480,10)
    screen.blit(best_text, (480,10)) 

    luck_text = font2.render(f'Luck: {luck}', True, (255, 255, 255))
    rarity(500,200, "blank.png", 230,50)
    screen.blit(luck_text, (250,50)) 
    


    pygame.display.flip() 

    if event.type == pygame.QUIT: 
        running = False
        break


pygame.quit()