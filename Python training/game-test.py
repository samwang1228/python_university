import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 640, 480                        #遊戲畫面寬和高
screen = pg.display.set_mode((width, height))   #依設定顯示視窗
pg.display.set_caption("my game")           #設定程式標題
#建立畫布bg
bg = pg.Surface(screen.get_size()) #get_size()取得視窗尺寸
bg = bg.convert() #convert()建立副本，加快畫布在視窗顯示速度
bg.fill((255, 255, 255))  #白色 
#(顏色由3個0到255整數組成，如:(255,0,0)為紅色、(0,255,0)為綠色、 (0,0,255)為藍色)

#繪製幾何圖形
#矩行 pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
#圓形 pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
#橢圓形 pygame.draw.ellipse(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)
#圓弧形 pygame.draw.arc(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
# 直線 pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
# pg.draw.rect(bg, (0,255,255),[70, 70, 500, 60], 4) 
# pg.draw.rect(bg, (0,0,255),[70, 150, 500, 60], 0)            #線寬0為實心
# pg.draw.circle(bg, (0,0,255),(100,300), 50, 4) 
# pg.draw.ellipse(bg, (0, 0, 255), [200, 250, 150, 80], 4)
# pg.draw.arc(bg, (0, 0, 255), [400, 250, 70, 150], 5, 1.5, 4)
# pg.draw.line(bg, (0, 0, 255), (550, 250), (550, 400), 4)
# #要在以下這兩條程式碼上面喔!!
# screen.blit(bg, (0,0))
# pg.display.update()

#圖片
# 圖片變數 = pygame.image.load(圖片檔案路徑)
# 圖片載入通常會用convert方法處理，增加繪製速度:
# 圖片變數.convert()
# 記得這也要用blit()方法繪製在視窗中喔!
# image = pg.image.load("test.jpg")
# image.convert()
# bg.blit(image, (20,10))
#文字
# #改字體、大小
# 字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
# #繪製
# 文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
font = pg.font.SysFont("simhei", 24)
text = font.render("Hello", True, (0,0,255), (255,255,255))
bg.blit(text, (320, 240))

#音效
#音效功能初始化
# pg.mixer.init()
# s = pg.mixer.Sound(hit.wav)  #括弧為音檔名稱
# s.set_volume(0.7)  #設定音量大小，參值0~1
# s.play()           #播放音效  
#顯示 
# 視窗變數.blit(背景變數, 繪製位置)  #繪製覆蓋整個視窗
screen.blit(bg, (0,0))
pg.display.update()

#關閉程式的程式碼
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()              