import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1200,800))
    scrn_rct = scrn_sfc.get_rect()

    #練習1
    bg_sfc = pg.image.load("ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect() #練習1

    #練習3
    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400

    #練習5
    bomb_sfc = pg.Surface((20,20)) #空のSurface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255,0,0),(10,10), 10 ) #円を描く
    bomb_rect = bomb_sfc.get_rect()
    bomb_rect.center = random.randint(0,scrn_rct.width), random.randint(0,scrn_rct.height)
    vx = 1
    vy = 1 
    

    clock = pg.time.Clock() #タイムインスタンス作成
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct) #練習2
        
        clock.tick(1000)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習4
        key_status = pg.key.get_pressed()
        if key_status[pg.K_UP] and tori_rct.centery-1 > 0 + (tori_rct.height//2) : 
            tori_rct.centery += -1
        if key_status[pg.K_DOWN] and tori_rct.centery+1 < scrn_rct.height - (tori_rct.height//2):
            tori_rct.centery += 1
        if key_status[pg.K_LEFT] and tori_rct.centerx-1 > 0 +(tori_rct.width//2):
            tori_rct.centerx += -1
        if key_status[pg.K_RIGHT] and tori_rct.centerx+1 < scrn_rct.width - (tori_rct.width//2):
            tori_rct.centerx += 1

        bomb_rect.centerx += vx
        bomb_rect.centery += vy

        if not 0 <= bomb_rect.centerx + vx <= scrn_rct.width: #画面内にないならば
            bomb_rect.centerx += -vx
            vx *= -1
        
        if not 0 <= bomb_rect.centery + vy <= scrn_rct.height: #画面内にないならば
            bomb_rect.centery += -vy
            vy *= -1
        
        if tori_rct.colliderect(bomb_rect): #こうかとんと爆弾がぶつかっているか判定
            return
        scrn_sfc.blit(tori_sfc,tori_rct) #こうかとんブリット
        scrn_sfc.blit(bomb_sfc,bomb_rect)#ボムblit

        pg.display.update()


# def check_bound(obj,scrn_rct):

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()