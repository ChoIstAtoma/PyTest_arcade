import arcade
from globals import USER_SCREEN_WIDTH, USER_SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, FULLSCREEN_RECT, ZOOM_VELUE  # 전역변수 가져오기

class FadeInOut(arcade.View):
    def __init__(self, previous_view, next_view, whether_fade, fade_speed): 
        # arcade.View의 초기화 메서드를 호출 (매개변수 없음)
        super().__init__()
        
        # 인자로 받은 값들을 클래스 속성으로 저장
        self.previous_view = previous_view
        self.next_view = next_view
        self.whether_fade = whether_fade  # 인/아웃 여부. 인:0 아웃:1
        self.alpha = 0 if whether_fade else 255  # 시작 알파
        self.fade_speed = fade_speed
        
        # 배경 및 스프라이트 설정
        self.all_sprite_list = arcade.SpriteList()
        self.background = arcade.Sprite("sprites/background_BLACK.png", SCALING)
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2
        self.background.alpha = self.alpha
        self.all_sprite_list.append(self.background)

    def on_draw(self):
        # 모든 스프라이트를 그립니다
        self.all_sprite_list.draw()
    
    def on_update(self, delta_time):
        # 투명도 조절  
        if self.whether_fade:  # 아웃: 어두워짐
            self.alpha += self.fade_speed
            if self.alpha >= 255:
                self.alpha = 255
                # 다음 뷰로 전환 (완전히 어두워지면 FadeInOut 인스턴스 생성)
                fade_in_view = FadeInOut(self.previous_view, self.next_view, False, self.fade_speed)  # 인스턴스 생성
                self.window.show_view(fade_in_view)  # 인스턴스 전달
                return

        else:  # 인: 밝아짐 
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                self.alpha = 0

                # 추가 디버깅: self.next_view가 arcade.View 인스턴스인지 확인
                if isinstance(self.next_view, arcade.View):
                    # 다음 뷰로 전환 (완전히 밝아지면 새로운 화면을 보여줌)
                    self.window.show_view(self.next_view)  # 이미 인스턴스이므로 바로 전달
                else:
                    print(f"Error: self.next_view is not an arcade.View instance. It is: {type(self.next_view)}")
                return
                
        # 알파값을 0과 255 사이로 제한
        self.alpha = max(0, min(255, self.alpha))
        self.background.alpha = self.alpha
        print(self.whether_fade , "@@@@@@", self.alpha)
