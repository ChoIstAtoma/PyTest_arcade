import arcade
from globals import USER_SCREEN_WIDTH, USER_SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, FULLSCREEN_RECT, ZOOM_VELUE #전역변수 갖고오기

class FadeInOut(arcade.View):
    def __init__(self, previous_view, next_view, whether_fade, fade_fpeed): 
        super().__init__(previous_view)
        self.previous_view = previous_view
        self.next_scene = next_view
        self.whether_fade = whether_fade #인/아웃 여부. 인:0 아웃:1
        self.alpha = 0 if whether_fade else 255 #시작 알파
        self.fade_speed = fade_fpeed
        
        self.AllSpriteList = arcade.SpriteList()
        self.background = arcade.Sprite("sprites/background_BLACK.png", SCALING, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.background.alpha = self.alpha
        self.AllSpriteList.append(self.background)
        
    def on_draw(self):
        self.AllSpriteList.draw()
    

    def on_update(self, delta_time):
        #투명도 조절  
        if self.whether_fade == True: #아웃: 어두워짐
            self.alpha += self.fade_speed
            if self.alpha >= 255:
                self.window.show_view(FadeInOut(self.next_scene, False, self.fade_speed))
                self.scene = None

        if self.whether_fade == False: #인: 밝아짐 
            self.alpha -= self.fade_speed*-1
            if self.alpha <= 0:
                self.window.show_view(self.next_scene)
                self.scene = None
                
        self.alpha = max(0, min(255, self.alpha))
        self.background.alpha = self.alpha
        print(self.alpha)

"""페이드인/아웃(페이드아웃 True) -> 시작알파:0 -> 증가 -> 알파==255일때 장면전환"""