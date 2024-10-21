import arcade
import arcade.gui
from arcade import open_window
from arcade.gui import UIOnClickEvent, UIOnChangeEvent, UIBoxLayout, UILabel, UIDropdown, UIAnchorLayout, UIView
import time

from globals import USER_SCREEN_WIDTH, USER_SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, FULLSCREEN_RECT, ZOOM_VELUE #전역변수 갖고오기
import fade_in_out_effect

ICON_SMALLER = arcade.load_texture(":resources:gui_basic_assets/icons/smaller.png")
TEX_SWITCH_GREEN = arcade.load_texture(":resources:gui_basic_assets/toggle/green.png")
TEX_SWITCH_RED = arcade.load_texture(":resources:gui_basic_assets/toggle/red.png")

# 설정 메뉴
class SettingMenu(UIView):
    def __init__(self): 
        super().__init__()
        self.camera = arcade.Camera2D()

        # 임시 수치들 (저장하기> 로 원본 수치에 대입.)
        self.width = SCREEN_WIDTH 
        self.height = SCREEN_HEIGHT
        self.scaling = SCALING
        self.zoomvelue = ZOOM_VELUE
        self.fullscreen = self.window.fullscreen
        self.FullscreenCheck = self.window.fullscreen
        self.vsync = self.window.vsync
        
        #gui 관련
        self.UI_manager = arcade.gui.UIManager()
        self.UI_manager.enable()
        self.tabs = arcade.gui.UIBoxLayout(x=100, y=950, vertical=False)
        self.UI_manager.add(self.tabs)
        self.contents = arcade.gui.UIBoxLayout(x=100, y=600, vertical=True, space_between=20)
        self.UI_manager.add(self.contents)
        
        self.tab_index = 0 #현재 탭 번호
        self.show_graphics_options(None)


    def setup(self):
        if self.window.fullscreen == True: #전체화면일때 비율 유지
            self.camera.zoom = ZOOM_VELUE

        self.re_load_sprite()
        self.create_tabs()


    def re_load_sprite(self): #스프라이트 모두 불러오기
        # 스프라이트 리스트 초기화
        self.all_sprite_list = None
        self.AllAnimationSpriteList = None
        self.all_sprite_list = arcade.SpriteList()
        # 배경 오브젝트 추가
        self.backgroundTexture = arcade.Sprite("sprites/background_GRAY.png", SCALING, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.all_sprite_list.insert(0, self.backgroundTexture)
        # 텍스트 오브젝트 정의 
        self.key_guide = arcade.Text("F: 선택\n<- ->: 수치 조절\nEnter: 적용하기\nESC: 나가기\n", SCREEN_WIDTH*7/8, SCREEN_HEIGHT*1/8, arcade.color.GOLD, SCALING*20, width=300, multiline=True)
        #스프라이트 오브젝트 정의
        self.tab_bar = arcade.Sprite("sprites/bar_YEllO.png", SCALING*2, 125, 900)  
        self.all_sprite_list.append(self.tab_bar)


    def on_draw_before_ui(self):
        self.all_sprite_list.draw()
        self.UI_manager.draw()
        
        # 모든 텍스트 그리기
        self.key_guide.draw()
    
    def on_draw(self):
        self.clear()

    def on_draw_after_ui(self):
        pass


    def on_update(self, deltatime):
        pass


    def on_key_press(self, key, modifiers):
        #탭 전환(키보드로)
        if key == arcade.key.RSHIFT:
            self.tab_index = (self.tab_index + 1) % 3 #<- 탭의 개수
            self.confirm_tab_change()

        elif key == arcade.key.LSHIFT:
            self.tab_index = (self.tab_index - 1) % 3
            self.confirm_tab_change()

        
    def on_key_release(self, key, modifiers):
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        global SCALING
        global ZOOM_VELUE

        if key == arcade.key.ENTER: #적용하기 (전체화면 해제 -> 해상도 변경 -> -> 전체화면 복구)
            
            if self.window.fullscreen == True:
                self.FullscreenCheck = True
                
            self.window.set_fullscreen(False)
            
            SCREEN_WIDTH = self.width
            SCREEN_HEIGHT = self.height
            SCALING = self.scaling
            self.window.set_size(SCREEN_WIDTH, SCREEN_HEIGHT)
            print(SCREEN_WIDTH , "SETTING" , SCREEN_HEIGHT, "SETTING", SCALING)
            self.camera.viewport_width = SCREEN_WIDTH
            self.camera.viewport_height = SCREEN_HEIGHT
            self.window.set_fullscreen(self.fullscreen)            
            
        if key == arcade.key.ESCAPE: #타이틀로 되돌아가기
            from title_menu import TitleMenu
            time.sleep(0.5)
            NextScene = TitleMenu()
            self.window.show_view(NextScene)
            NextScene.setup()
            self.scene = None

        if key == arcade.key.A:
            self.width = 1280
            self.height = 720
            self.scaling = 1/1.5
            self.zoomvelue = 1.5
            
        if key == arcade.key.B:
            self.fullscreen = False

        if key == arcade.key.C:
            self.fullscreen = True


    def create_tabs(self):
        # 그래픽 탭 버튼
        self.graphics_button = arcade.gui.UIFlatButton(text="Graphics", width=150)
        self.tabs.add(self.graphics_button)
        @self.graphics_button.event("on_click")
        def on_click(event: UIOnClickEvent):
            self.tab_index = 0
            self.show_graphics_options(None)

        # 사운드 탭 버튼
        self.sound_button = arcade.gui.UIFlatButton(text="Sound", width=150)
        self.tabs.add(self.sound_button)
        @self.sound_button.event("on_click")      
        def on_click(event: UIOnClickEvent):
            self.tab_index = 1
            self.show_sound_options(None)
        print(self.sound_button.center_x)
        
        # 컨트롤 탭 버튼
        self.controls_button = arcade.gui.UIFlatButton(text="Controls", width=150)
        self.tabs.add(self.controls_button)
        @self.controls_button.event("on_click")      
        def on_click(event: UIOnClickEvent):
            self.tab_index = 2
            self.show_controls_options(None)
        print(self.controls_button.center_x)


    def confirm_tab_change(self): #탭인덱스 수치에 따라서 옵션들 그리기
        if self.tab_index == 0:
            self.show_graphics_options(None)
            arcade.schedule(self.move_tab_bar, 1/60)
        elif self.tab_index == 1:
            self.show_sound_options(None)
            arcade.schedule(self.move_tab_bar, 1/60)
        elif self.tab_index == 2:
            self.show_controls_options(None)
            arcade.schedule(self.move_tab_bar, 1/60)


    def show_graphics_options(self, event): #그래픽 옵션 그리기
        self.contents.clear()
        self.graphics_options = arcade.gui.UIBoxLayout(x=200, y=100) #호출할때마다 초기화 안하면 오류
        self.graphics_options.add(arcade.gui.UILabel(text="Graphics"))
        self.contents.add(self.graphics_options)

        #전체화면 온오프(토글 버튼)
        fullscreen_toggle_button = arcade.gui.UIFlatButton(text="전체 화면", width=640)
        fullscreen_toggle_button.place_text(anchor_x="left", align_x=45)
        fullscreen_toggle_button.add(child=arcade.gui.UIImage(texture=ICON_SMALLER, width=20, height=20),anchor_x="left", align_x=10)
        fullscreen_toggle = fullscreen_toggle_button.add(child=arcade.gui.UITextureToggle(value=not self.fullscreen, on_texture=TEX_SWITCH_RED, off_texture=TEX_SWITCH_GREEN, width=60, height=30), anchor_x="right", align_x=-10)
        self.contents.add(fullscreen_toggle_button)
        @fullscreen_toggle.event("on_change")
        def on_change(event: UIOnChangeEvent):
            self.fullscreen = not event.new_value
            fullscreen_toggle_button.disabled = event.new_value
            print("FULLLLLLLLL")

        #해상도 변경(드롭다운 버튼)
        changeScreen_dropdown_button = arcade.gui.UIFlatButton(text="Screen Size", width=640)
        changeScreen_dropdown_button.place_text(anchor_x="left", align_x=45)
        changeScreen_dropdown = changeScreen_dropdown_button.add(child=UIBoxLayout(vertical=False, size_hint=(0.3, 0.3), space_between=10), anchor_x="right", align_x=10)
        changeScreen_dropdown.add(UIDropdown(default="1920 X 1080", options=["1920 X 1080", "1280 X 720", "640 X 360"]))
        self.contents.add(changeScreen_dropdown_button)
        """ChangeScreen_dropdown.on_event = self.on_dropdown_change"""
    

        #프레임레이트 제한 (드롭다운 버튼)
        changeScreen_dropdown_button = arcade.gui.UIFlatButton(text="최대 프레임", width=640)
        changeScreen_dropdown_button.place_text(anchor_x="left", align_x=45)
        changeScreen_dropdown = changeScreen_dropdown_button.add(child=UIBoxLayout(vertical=False, size_hint=(0.3, 0.3), space_between=10), anchor_x="right", align_x=10)
        changeScreen_dropdown.add(UIDropdown(default="Vsync", options=["Vsync", "30", "60", "120", "144", "165", "240", "360", "unlimited"]))
        self.contents.add(changeScreen_dropdown_button)
        @changeScreen_dropdown.event("on_change")
        def  on_change(event: UIOnChangeEvent):
            print(f"Selected option: {event.new_value}")
            if event.new_value == "Vsync":
                self.vsync = True

    def show_sound_options(self, event): #사운드 옵션 그리기
        self.contents.clear()
        self.sound_options = arcade.gui.UIBoxLayout(x=400, y=100)
        self.sound_options.add(arcade.gui.UILabel(text="Sound"))
        self.contents.add(self.sound_options)

    def show_controls_options(self, event): #컨트롤 옵션 그리기
        self.contents.clear()
        self.controls_options = arcade.gui.UIBoxLayout(x=600, y=100)
        self.controls_options.add(arcade.gui.UILabel(text="Controls"))
        self.contents.add(self.controls_options)
        
    def move_tab_bar(self, deltatime):
        if self.tab_bar.center_x == 100 + (self.tab_index+1)*75:
            arcade.unschedule(self.move_tab_bar)
        elif self.tab_bar.center_x > 100 + self.tab_index*75:
            self.tab_bar.center_x += 5
        elif self.tab_bar.center_x < 100 + self.tab_index*75:
            self.tab_bar.center_x -= 5
    
    def smooth_move_accel(self, start_x, start_y, arrive_x, arrive_y, current_value, intensity):
        square_value = current_value**intensity
        return start_x + (arrive_x - start_x) * square_value, start_y + (arrive_y-start_y)* intensity

    def smooth_move_decel(self, start_x, start_y, arrive_x, arrive_y, current_value, intensity):
        square_value = current_value**(intensity)
        return start_x + (arrive_x - start_x) * square_value, start_y + (arrive_y-start_y)* intensity
        
    
class ButtonAdd(UIAnchorLayout):
    def __init__(self, **kwargs):
        pass

    def on_dropdown_change(self, event: UIOnChangeEvent):
        pass
