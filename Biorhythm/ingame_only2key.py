import arcade
import arcade.gui
from time import time
from globals import SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, FULLSCREEN_RECT # 전역변수 갖고오기


class Ingame_Only2key(arcade.View): #인게임(바이오리듬 2키)

    def __init__(self):
        super().__init__()
        self.AllSpriteList = arcade.SpriteList()

        self.FirstLineList = arcade.SpriteList() #리듬게임 첫번째 라인(호흡)
        self.TwiceLineList = arcade.SpriteList() #리듬게임 두번째 라인(심장박동)

        #self.x = 0, self.y = 0

        self.LoadingComplete = False #로딩시작
        

    def setup(self):
        #기어와 노트 이미지 로드
        self.LoadingImage = arcade.Sprite("sprites/loading....png", SCALING)
        self.GearImage = arcade.Sprite("sprites/testGear.png", SCALING*10)
        self.ButtonImage = arcade.Sprite("sprites/testNote.png", SCALING*10)
        #로딩끝
        self.LoadingComplete = True

        #arcade.schedule(self.FallNote(SCREEN_WIDTH/3, SCREEN_HEIGHT), 1)
        arcade.schedule(self.FloatGearImage(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 1)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            pass

        #pause
        if key == arcade.key.ESCAPE:
            self.Pause()


    def on_draw(self):
        self.clear()
        if self.LoadingComplete == False:
            self.LoadingImage.draw()

        #모든 스프라이트 출럭
        self.AllSpriteList.draw()

        #로딩중일때 로딩창 출력
        
    
    def on_update(self, deltatime):

        self.FloatGearImage(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            

    #기어 표시(x, y는 기어의 중심)
    def FloatGearImage(self, center_x, center_y):
        self.GearImage.center_x = center_x
        self.GearImage.center_y = center_y
    

    #노트 이미지 낙하(판정에 영향 X)
    def FallNote(self, x, y, notespeed, ButtenImage):
        self.ButtonImage = ButtenImage
        self.x = x
        self.y = y+notespeed

        #노트 생성시 타임스탬프
        self.NoteAppendTimestamp = time.time

        #노트 낙하 시작 위치, 속도
        self.ButtonImage.center_x = self.x
        self.ButtonImage.center_y = self.y
        self.ButtonImage.velocity = (0, notespeed*-10)
        self.AllSpriteList.append(self.ButtonImage)

        #일정 y이하시 노트 삭제
        if(self.ButtonImage.center_y <= 50):
            self.AllSpriteList.remove(self.ButtonImage)

        return self.NoteAppendTimestamp

            
    
    def HitNote(self):
        pass

    def MissNote(self, x, y):
        return(4)
            
    def Pause(self):
        print("pause!!")
        pass


    # 타임스탬프 판정 시스템(판정에 영향O. 타임스탬프를 비교해서 판정을 얻어냄.) -> return 판정
    def TimestampVerdictSystem(self):  
        now = time.time