import pygame as pg
import sys
from random import randint

class Screen:
    def __init__(self, title, size, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size) #(600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird: 
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

        self.dy = 1
        self.jump = False

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.centery += self.dy
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
        
        if key_states==[pg.K_SPACE]:
            self.jump == True
        
        if self.dy < 1:
            self.dy += 0.5

        #こうかとんが画面外にいかないようにする
        if self.rct.top <= 0: #上
            self.rct.top = 0

        if self.rct.bottom >= scr.rct.height: #下
            self.rct.bottom = scr.rct.height

        if  self.rct.left <= 0: #左
            self.rct.left = 0

        if self.rct.right >= scr.rct.width: #右
            self.rct.right = scr.rct.width
        
        self.blit(scr)

    def jump(self,event):
        if event.type  == pg.KEYUP and self.jump == True:
            self.dy = -3
            self.jump = False
        else:
            pass 



class Floor: #足場の表示
    pass


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main(): #ゲーム
    scr = Screen("ホッピングゲーム",(600,900),"fig/pg_bg.jpg") #ウィンドウ作成
    kouka = Bird("fig/6.png", 1.5, (300, 300))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 閉じるボタンが押されたら終了
                return
            kouka.jump(event)
        scr.blit()
        kouka.update(scr)
        pg.display.update()



if __name__=="__main__":
    pg.init() #初期化
    main()    #ゲーム実行
    pg.quit()
    sys.exit()


# class floor:

#     def __init__(self,scr:Screen):
#         self.sfc = pg.draw.rect(scr,(255,255,255),(0,scr.height-10,scr.width,scr.height))
#         self.sfc_rect = self.sfc.get_rect()

#     def blit(self,scr:Screen):
#         scr.blit(self.sfc,self.sfc_rect)
    
#     def update(self,scr:Screen):