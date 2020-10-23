import pygame
r,sw,sh,x1,y1,x,y,vel,width,hight,dt,vx,vy,mx,my,scoreA,scoreB=10,1000,700,30,200,500,350,10,10,100,10,5,-2,0,0,0,0
y2=y1
x2=sw-x1
pygame.init()
win=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Ping Pong")
run,running,main_menu,options,pause,Awon,Bwon=False,True,True,False,True,False,False
font = pygame.font.SysFont('Sans', 32)
while running:
    if main_menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                main_menu=False
                running=False
                options=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if textRect1.bottomright[0]>mx>textRect1.topleft[0] and textRect1.bottomright[1]>my> textRect1.topleft[1]:
                    main_menu=False
                    options=False
                    run=True
                if textRect2.bottomright[0]>mx>textRect2.topleft[0] and textRect2.bottomright[1]>my> textRect2.topleft[1]:
                    main_menu=False
                    options=True
                    run=False
                if textRect3.bottomright[0]>mx>textRect3.topleft[0] and textRect3.bottomright[1]>my> textRect3.topleft[1]:
                    run=False
                    main_menu=False
                    running=False
                    options=False
        win.fill((0,0,0))
        mx,my=pygame.mouse.get_pos()
        text1= font.render('START', True,(202,247,241),(0,0,0))
        textRect1 = text1.get_rect()
        textRect1.center = (500, 350)
        text2= font.render('HOW TO PLAY', True,(202,247,241),(0,0,0))
        textRect2 = text2.get_rect()
        textRect2.center = (500, 400)
        text3= font.render('QUIT', True,(202,247,241),(0,0,0))
        textRect3 = text3.get_rect()
        textRect3.center = (500, 450)
        if textRect1.bottomright[0]>mx>textRect1.topleft[0] and textRect1.bottomright[1]>my> textRect1.topleft[1]:
            text1= font.render('START', True,(255,100,0),(0,0,0))
            textRect1 = text1.get_rect()
            textRect1.center = (500, 350)
        if textRect2.bottomright[0]>mx>textRect2.topleft[0] and textRect2.bottomright[1]>my> textRect2.topleft[1]:
            text2= font.render('HOW TO PLAY', True,(255,100,0),(0,0,0))
            textRect2 = text2.get_rect()
            textRect2.center = (500, 400)
        if textRect3.bottomright[0]>mx>textRect3.topleft[0] and textRect3.bottomright[1]>my> textRect3.topleft[1]:
            text3= font.render('QUIT', True,(255,100,0),(0,0,0))
            textRect3 = text3.get_rect()
            textRect3.center = (500, 450)
        win.blit(text1,textRect1)
        win.blit(text2,textRect2)
        win.blit(text3,textRect3)
        pygame.display.update()
    if options:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                main_menu=False
                options=False
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if textRectb.bottomright[0]>mx>textRectb.topleft[0] and textRectb.bottomright[1]>my> textRectb.topleft[1]:
                    run=False
                    options=False
                    main_menu=True
        win.fill((0,0,0))
        mx,my=pygame.mouse.get_pos()
        textb= font.render('BACK', True,(202,247,241),(0,0,0))
        textRectb = textb.get_rect()
        textRectb.center = (500, 600)
        texti1= font.render('W - left paddle up', True,(202,247,241),(0,0,0))
        texti2= font.render('S - left paddle down', True,(202,247,241),(0,0,0))
        texti3= font.render('UP Arrow - right paddle up', True,(202,247,241),(0,0,0))
        texti4= font.render('DOWN Arrow - right paddle up', True,(202,247,241),(0,0,0))
        texti5= font.render('Score 100 to win',True,(202,247,241),(0,0,0))
        textRecti1= texti1.get_rect()
        textRecti2= texti2.get_rect()
        textRecti3= texti3.get_rect()
        textRecti4= texti4.get_rect()
        textRecti5= texti5.get_rect()
        textRecti1.center=(500,200)
        textRecti2.center=(500,250)
        textRecti3.center=(500,300)
        textRecti4.center=(500,350)
        textRecti5.center=(500,450)
        win.blit(texti1,textRecti1)
        win.blit(texti2,textRecti2)
        win.blit(texti3,textRecti3)
        win.blit(texti4,textRecti4)
        win.blit(texti5,textRecti5)
        if textRectb.bottomright[0]>mx>textRectb.topleft[0] and textRectb.bottomright[1]>my> textRectb.topleft[1]:
            textb= font.render('BACK', True,(255,100,0),(0,0,0))
            textRectb = textb.get_rect()
            textRectb.center = (500, 600)
        win.blit(textb,textRectb)
        pygame.display.update()
    if run:
        pygame.time.delay(dt)
        if y==r:
            vy=-vy
        if y==sh-r-100:
            vy=-vy
        if x==x2-r:
            if y2<y<y2+hight:
                vx=-vx
        if x==x1+r:
            if y1<y<y1+hight:
                vx=-vx
        if (x>sw-r):
            pause=True
            scoreA+=10
            if scoreA==100:
                pause=True
                Awon=True
        if (x<r):
            pause=True
            scoreB+=10
            if scoreB==100:
                pause=True
                Bwon=True
        while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    running=False
                    pause=False
            if pause==False:
                break
            result="PRESS SPACE TO PLAY"
            if Awon:
                result="PLAYER 1 HAS WON!!!"
            if Bwon:
                result="PLAYER 2 HAS WON!!!"
            win.fill((255,255,255))
            textA= font.render('Player 1'+': '+str(scoreA), True,(255,0,0),(255,255,255))
            textRectA = textA.get_rect()
            textRectA.bottomleft = (0,650)
            win.blit(textA,textRectA)
            textB= font.render('Player 2'+': '+str(scoreB), True,(0,0,255),(255,255,255))
            textRectB = textB.get_rect()
            textRectB.bottomleft = (830,650)
            win.blit(textB,textRectB)
            texts= font.render(result, True,(0,0,0),(255,255,255))
            textRects = texts.get_rect()
            textRects.center = (500, 300)
            win.blit(texts,textRects)
            pygame.draw.circle(win,(0,0,0),(500,250),10)
            pygame.draw.rect(win,(255,0,0),(30,200,width,hight))
            pygame.draw.rect(win,(0,0,255),(sw-30,200,width,hight))
            pygame.draw.rect(win,(0,0,0),(0,sh-100,sw,1))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE]) and not(Awon) and not(Bwon):
                pause=False
                x1,y1,y2,x,y=30,200,200,500,250
                x2=sw-30
        x+=vx
        y+=vy
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                running=False
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w]) and (y1>0):
            y1 -= vel
        if (keys[pygame.K_s]) and (y1<sh-hight-100):
            y1 += vel
        if (keys[pygame.K_UP]) and (y2>0):
            y2 -= vel
        if (keys[pygame.K_DOWN]) and (y2<sh-hight-100):
            y2 += vel
        win.fill((255,255,255))
        textA= font.render('Player 1'+': '+str(scoreA), True,(255,0,0),(255,255,255))
        textRectA = textA.get_rect()
        textRectA.bottomleft = (0, 650)
        win.blit(textA,textRectA)
        textB= font.render('Player 2'+': '+str(scoreB), True,(0,0,255),(255,255,255))
        textRectB = textB.get_rect()
        textRectB.bottomleft = (830, 650)
        win.blit(textB,textRectB)
        pygame.draw.circle(win,(0,0,0),(x,y),10)
        pygame.draw.rect(win,((255,0,0)),(x1,y1,width,hight))
        pygame.draw.rect(win,((0,0,255)),(x2,y2,width,hight))
        pygame.draw.rect(win,(0,0,0),(0,sh-100,sw,1))
        pygame.display.update()
pygame.quit()