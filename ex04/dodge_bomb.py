import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1200,600))
    
    bg_sfc = pg.image.load("ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect() #練習1
    clock = pg.time.Clock() #タイムインスタンス作成
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct) #練習2
        pg.display.update()
        clock.tick(1000)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()