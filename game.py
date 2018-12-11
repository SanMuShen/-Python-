import pygame
from pygame.locals import *
import sys
from MySprite import MySprite
import time
import random
    
class DH_png():
    def dh_png(self):
        self.cat = MySprite(screen)
        # 传入帧的位置 帧的宽度高度  文件位置 以及帧数
        self.cat.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
        self.cat.position = 200,200

        self.cat1 = MySprite(screen)
        self.cat1.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat2 = MySprite(screen)
        self.cat2.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat3 = MySprite(screen)
        self.cat3.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat4 = MySprite(screen)
        self.cat4.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat5 = MySprite(screen)
        self.cat5.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat6 = MySprite(screen)
        self.cat6.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat7 = MySprite(screen)
        self.cat7.load("D:/tongcheng/game/hy0.png", 35, 40, 9)

        self.cat_ao = MySprite(screen)
        self.cat_ao.load("D:/tongcheng/game/zhengmian.png",90,95,4)


class Two():
    def two_window(self):
        screen = pygame.display.set_mode((1024,615),0,32)
        pygame.display.set_caption("京城保卫战")
        # font = pygame.font.Font(None,18)
        framerate = pygame.time.Clock()
        background = pygame.image.load("D:/tongcheng/game/com.jpg").convert_alpha()

        # 设置背景音乐
        pygame.mixer.music.load("D:/tongcheng/music/ZhanDou1.mp3")

        # 设置鼠标样式
        mouse = pygame.image.load("D:/tongcheng/game/shubiao.png").convert_alpha()

        text = pygame.font.SysFont("宋体",50)
        text_fmt = text.render("You must guard the barrier",1,(255,255,255))
        text_fmt1 = text.render('ESC exit game',1,(255,255,255))

        game_font = pygame.font.SysFont('宋体', 50, True)

        self.cat_ao1 = MySprite(screen)
        self.cat_ao1.load("D:/tongcheng/game/long.png",80,110,8)
        self.cat_ao1.position = 0,230
        self.cat_ao1.first_frame = 8
        self.cat_ao1.last_frame = 15

        Y = random.randint(120,260)  #120 190 260 
        cat_fhg = MySprite(screen)
        cat_fhg.load("D:/tongcheng/game/fhss.png",125,95,4)
        cat_fhg.position = 850,Y
        cat_fhg.first_frame = 0
        cat_fhg.last_frame = 3
        Y = random.randint(120,260)
        cat_fhg1 = MySprite(screen)
        cat_fhg1.load("D:/tongcheng/game/fhss.png",125,95,4)
        cat_fhg1.position = 850,Y
        cat_fhg1.first_frame = 0
        cat_fhg1.last_frame = 3
        Y = random.randint(120,260)
        cat_fhg2 = MySprite(screen)
        cat_fhg2.load("D:/tongcheng/game/fhss.png",125,95,4)
        cat_fhg2.position = 850,Y
        cat_fhg2.first_frame = 0
        cat_fhg2.last_frame = 3

        cat_fhg_list = [cat_fhg1,cat_fhg2]
        cat_fhg_list.append(cat_fhg)

        self.catgroup_s = pygame.sprite.Group()
        self.catgroup_s.add(cat_fhg,cat_fhg1,cat_fhg2)

        self.catgroup_z = pygame.sprite.Group()
        self.catgroup_z.add(self.cat_ao1)

        score = 0
        cat_fhg_dict = dict()
        FH_SCORE = 100

        while True:
            pygame.init()
            # 清屏
            # screen.fill((0,0,100))

            x = random.randint(1,10)
            cat_fhg.X -= x
            x = random.randint(1,10)
            cat_fhg1.X -= x
            x = random.randint(1,10)
            cat_fhg2.X -= x

            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()

            if len(self.catgroup_s) == 0:
                Y = random.randint(120,260)
                cat_fhg.position = 850,Y
                Y = random.randint(120,260)
                cat_fhg1.position = 850,Y
                Y = random.randint(120,260)
                cat_fhg2.position = 850,Y

                self.catgroup_s.add(cat_fhg,cat_fhg1,cat_fhg2)
            # 游戏失败
            if cat_fhg.X <= 0 or cat_fhg2.X <= 0 or cat_fhg1.X <= 0:
                self.score = score 
                self.gameover()

            # 游戏胜利
            if score >= 10000:
                self.gamevictory()
            
            # 设置帧的速率
            framerate.tick(15)
            # 得到以毫秒为间隔的时间
            ticks = pygame.time.get_ticks()

            #接收键盘事件
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                #上下左右
                elif keys[K_UP] or keys[K_w]:
                    self.cat_ao1.direction = 6
                elif keys[K_RIGHT] or keys[K_d]:
                    self.cat_ao1.direction = 2
                elif keys[K_DOWN] or keys[K_s]:
                    self.cat_ao1.direction = 4
                elif keys[K_LEFT] or keys[K_a]:
                    self.cat_ao1.direction = 3
                elif keys[K_x]:
                    self.cat_ao1.direction = 5
                else:
                    #玩家静止
                    self.cat_ao1.direction = 1

                # 接收鼠标当前悬浮位置
                if event.type == MOUSEMOTION:
                    mouse_x,mouse_y = event.pos

            #键盘输入esc退出
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                exit()

            #角色的状态帧的起点终点取决于方向direction
            self.cat_ao1.first_frame = self.cat_ao1.direction * self.cat_ao1.columns
            self.cat_ao1.last_frame = self.cat_ao1.first_frame + self.cat_ao1.columns-1
            # self.frame #???
            if self.cat_ao1.frame < self.cat_ao1.first_frame:
                self.cat_ao1.frame = self.cat_ao1.first_frame

            #算出移动距离, 实施移动玩家坐标, 移动距离和 方向 和 速度(速度定义为V, 单位帧移动像素距离) 有关
            V = 10
            if self.cat_ao1.direction == 6:
                self.cat_ao1.Y += -V 
            elif self.cat_ao1.direction == 2:
                self.cat_ao1.X += V
            elif self.cat_ao1.direction == 4:
                self.cat_ao1.Y += V
            elif self.cat_ao1.direction == 3:
                self.cat_ao1.X += -V

            elif self.cat_ao1.direction == 5:
                cat_fhg_dict = pygame.sprite.groupcollide(self.catgroup_s,self.catgroup_z,True,False)
                score += len(cat_fhg_dict) * FH_SCORE  # 计算得分
            

            screen.blit(background,(0,0))
            
            # 鼠标的x，y坐标
            m_x,m_y = pygame.mouse.get_pos()
            # 隐藏鼠标
            pygame.mouse.set_visible(False)

            m_x -= mouse.get_width() / 3
            m_y -= mouse.get_height() / 3
            #用其他图形代替鼠标
            screen.blit(mouse, (m_x, m_y))

            # 更新显示屏幕
            self.catgroup_z.update(ticks,5)
            self.catgroup_z.draw(screen)
            self.catgroup_s.update(ticks,120)
            self.catgroup_s.draw(screen)
            screen.blit(text_fmt,(0,0))
            screen.blit(text_fmt1,(750,0))
            screen.blit(game_font.render('SCORE: %d' % score, True, [0, 0, 0]), [20, 50])
            pygame.display.update()
    
    def gamevictory(self):
        pygame.init()
        screen = pygame.display.set_mode((1088,664),0,32)
        pygame.display.set_caption("京城保卫战")
        background = pygame.image.load("D:/tongcheng/game/gamevictor.png").convert_alpha()

        pygame.mixer.music.load("D:/tongcheng/music/victory.mp3")

        text = pygame.font.SysFont("宋体",50)
        text_fmt = text.render("Press SPACE to continue",1,(255,255,255))

        while True:
            screen.fill((0,0,100))

            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
            
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                if keys[K_SPACE]:
                    main()

            #键盘输入esc退出
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                main()

            screen.blit(background,(0,0))
            screen.blit(text_fmt,(0,600))
            pygame.display.update()

    def gameover(self):
        pygame.init()
        screen = pygame.display.set_mode((1088,664),0,32)
        framerate = pygame.time.Clock()
        pygame.display.set_caption("京城保卫战")
        background = pygame.image.load("D:/tongcheng/game/gameover.png").convert_alpha()
        pygame.mixer.music.load("D:/tongcheng/music/gameover.mp3")

        text = pygame.font.SysFont("宋体",50)
        text_fmt = text.render("Press SPACE to continue",1,(255,255,255))
        text1 = pygame.font.SysFont("宋体",120)
        text_fmt1 = text1.render("GAME OVER",1,(255,0,0))
        gameover_font = pygame.font.SysFont('宋体', 50, True)

        while True:
            screen.fill((0,0,100))
            # 设置帧的速率
            framerate.tick(15)
            ticks = pygame.time.get_ticks()

            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
            
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                if keys[K_SPACE]:
                    main()

            #键盘输入esc退出
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                exit()

            screen.blit(background,(0,0))

            screen.blit(text_fmt,(350,400))
            screen.blit(text_fmt1,(330,100))
            screen.blit(gameover_font.render('SCORE: %d' % self.score, True, [0, 0, 0]), [410, 280])
            pygame.display.update()




def main():
    pygame.init()
    # 初始化窗口
    screen = pygame.display.set_mode((1088,664),0,32)
    
    # 设置标题
    pygame.display.set_caption("五军都督府")
    font = pygame.font.Font(None, 18)

    framerate = pygame.time.Clock()
    # 背景图片
    background = pygame.image.load("D:/tongcheng/game/lo.png").convert_alpha()
    mouse = pygame.image.load("D:/tongcheng/game/shubiao.png").convert_alpha()

    # 背景音乐
    pygame.mixer.music.load("D:/tongcheng/music/TianGong.mp3")
    pygame.mixer.music.play()

    cat = MySprite(screen)
    cat.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat.position = 300,90
    cat1 = MySprite(screen)
    cat1.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat1.position = 760,90
    cat2 = MySprite(screen)
    cat2.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat2.position = 85,200
    cat3 = MySprite(screen)
    cat3.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat3.position = 85,430
    cat4 = MySprite(screen)
    cat4.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat4.position = 300,540
    cat5 = MySprite(screen)
    cat5.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat5.position = 760,540
    cat6 = MySprite(screen)
    cat6.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat6.position = 980,430
    cat7 = MySprite(screen)
    cat7.load("D:/tongcheng/game/hy0.png", 35, 40, 9)
    cat7.position = 980,200

    cat_fh = MySprite(screen)
    cat_fh.load("D:/tongcheng/game/fhs.png",180,145,4)
    cat_fh.position = 850,70
    cat_fh.first_frame = 0
    cat_fh.last_frame = 3

    cat_lo = MySprite(screen)
    cat_lo.load("D:/tongcheng/game/long.png",80,110,8)
    cat_lo.position = 100,50
    cat_lo.first_frame = 0
    cat_lo.last_frame = 7

    catgroup = pygame.sprite.Group()
    catgroup.add(cat,cat1,cat2,cat3,cat4,cat5,cat6,cat7)

    catgroup1 = pygame.sprite.Group()
    catgroup1.add(cat_fh)

    catgroup3 = pygame.sprite.Group()
    catgroup3.add(cat_lo)

    while True:
        # 清屏
        screen.fill((0,0,100))
        # 设置帧的速率
        framerate.tick(15)
        ticks = pygame.time.get_ticks()

        # 使其可以循环播放背景音乐
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()

        #接收键盘事件
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            #上下左右
            elif keys[K_UP] or keys[K_w]:
                cat_lo.direction = 6
            elif keys[K_RIGHT] or keys[K_d]:
                cat_lo.direction = 2
            elif keys[K_DOWN] or keys[K_s]:
                cat_lo.direction = 4
            elif keys[K_LEFT] or keys[K_a]:
                cat_lo.direction = 3
            else:
                #玩家静止
                cat_lo.direction = 0

            # 接收鼠标当前悬浮位置
            if event.type == MOUSEMOTION:
                mouse_x,mouse_y = event.pos

        #键盘输入esc退出
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        #角色的状态帧的起点终点取决于方向direction
        cat_lo.first_frame = cat_lo.direction * cat_lo.columns
        cat_lo.last_frame = cat_lo.first_frame + cat_lo.columns-1
        # self.frame #???
        if cat_lo.frame < cat_lo.first_frame:
            cat_lo.frame = cat_lo.first_frame

        
        #算出移动距离, 实施移动玩家坐标, 移动距离和 方向 和 速度(速度定义为V, 单位帧移动像素距离) 有关
        V = 10
        if cat_lo.direction == 6:
            # X、Y 从哪来 #???
            cat_lo.Y += -V 
        elif cat_lo.direction == 2:
            cat_lo.X += V
        elif cat_lo.direction == 4:
            cat_lo.Y += V
        elif cat_lo.direction == 3:
            cat_lo.X += -V
        elif cat_lo.X >= 800:
            w = Two()
            w.two_window()
            
        screen.blit(background,(0,0))
        # 鼠标的x，y坐标
        m_x,m_y = pygame.mouse.get_pos()
        # 隐藏鼠标
        pygame.mouse.set_visible(False)

        m_x -= mouse.get_width() / 3
        m_y -= mouse.get_height() / 3
        #用其他图形代替鼠标
        screen.blit(mouse, (m_x, m_y))

        # 更新显示屏幕
        catgroup.update(ticks,120)
        catgroup.draw(screen)
        catgroup1.update(ticks,250)
        catgroup1.draw(screen)
        catgroup3.update(ticks,40)
        catgroup3.draw(screen)
        pygame.display.update()
        # pygame.display.flip()

main()