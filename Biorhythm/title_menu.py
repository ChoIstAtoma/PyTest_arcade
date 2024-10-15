import arcade
import arcade.gui
import time

from globals import SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, FULLSCREEN_RECT, ZOOM_VELUE # 전역변수 갖고오기

from  fade_in_out_effect import FadeInOut


# 시작 메뉴 
class TitleMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.camera = arcade.Camera2D()
        self.scene = arcade.Scene() # 스프라이트 총괄
        
        self.all_sprite_list = arcade.SpriteList()
        self.all_animation_sprite_list = arcade.SpriteList()
        print(SCREEN_WIDTH, "TITLE", SCREEN_HEIGHT, "TITLE", SCALING)
        
    def setup(self):
        if self.window.fullscreen == True: #전체화면일때 비율 유지
            self.camera.zoom = ZOOM_VELUE
        self.re_load_sprite()


    def re_load_sprite(self): #스프라이트 모두 불러오기
        self.all_sprite_list.clear()

        # 배경 스프라이트 추가
        self.backgroundTexture = arcade.Sprite("sprites/background_mountain.png", SCALING, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.all_sprite_list.insert(0, self.backgroundTexture)

        # 스프라이트 추가
        self.skarner = arcade.Sprite("sprites/skarner.png", SCALING/2, center_x = SCREEN_WIDTH/2, center_y = SCREEN_HEIGHT/4)
        self.all_sprite_list.append(self.skarner)

        #텍스트 오브젝트 정의
        self.title_text = arcade.Text("Biorhythm_only2key", SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4, arcade.color.GOLD, SCALING*50, anchor_x="center", font_name="Kenney Future")
        self.key_guide = arcade.Text("Setting: F10", SCREEN_WIDTH*7/8, SCREEN_HEIGHT*1/10, arcade.color.GOLD, SCALING*20, font_name="Kenney Future")

        #효과음 정의
        self.heart_sound = arcade.load_sound("sounds/heartbeat1.mp3")
        

    def on_draw(self):
        self.clear()
        self.camera.use()
        
        #모든 스프라이트 그리기
        self.all_sprite_list.draw()
        
        #모든 텍스트 그리기
        self.title_text.draw()
        self.key_guide.draw()


    def on_update(self, delta_time):
        arcade.SpriteList.update(self.all_animation_sprite_list)

        self.skarner.angle += 1
        if self.skarner.alpha > 0:
            self.skarner.alpha -= 1


    def on_mouse_release(self, x, y, button, modifiers):
        arcade.sound.play_sound(self.heart_sound)

    def on_key_release(self, key, modifiers):
        # 다른 메뉴 진입
        if key == arcade.key.KEY_2: #2키로 이동
            from ingame_only2key import Ingame_Only2key
            time.sleep(0.5)
            next_scene = Ingame_Only2key()
            self.window.show_view(next_scene)
            next_scene.setup()
            #self.scene = None # 메모리 누수 방지

        if key == arcade.key.F10: #설정창으로 이동
            from setting_menu import SettingMenu
            next_scene = FadeInOut(SettingMenu, True, 10)
            self.window.show_view(next_scene)
            #self.scene = None

        if key == arcade.key.F:
            self.skarner.center_x +=1
        if key == arcade.key.ENTER:
            self.all_sprite_list.append(self.skarner)

    def fade_in(self):
        pass