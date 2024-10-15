import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "페이드 인/아웃 효과 장면 전환"

class SceneA(arcade.View):
    def __init__(self):
        super().__init__()
        # 배경 스프라이트 설정
        self.background_sprite = arcade.Sprite("scene_a_background.png", scale=1.0)
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        # 페이드 아웃 관련 변수
        self.alpha = 255
        self.fade_out = False  # 페이드 아웃 트리거

        self.spritelist = arcade.SpriteList()
        self.background_sprite.alpha = self.alpha
        self.spritelist.append(self.background_sprite)

    def on_draw(self):
        self.background_sprite.alpha = self.alpha  # 투명도 적용
        self.spritelist.draw()

    def on_update(self, delta_time):
        if self.fade_out:
            # 페이드 아웃 효과: alpha 값을 감소시킴
            self.alpha -= 5
            if self.alpha <= 0:
                # 페이드 아웃 완료 후 SceneB로 전환
                scene_b = SceneB()
                self.window.show_view(scene_b)
        else:
            # 페이드 아웃 조건을 충족하면 fade_out 트리거
            self.fade_out = True

    def on_key_press(self, key, modifiers):
        # 아무 키나 누르면 페이드 아웃 시작
        self.fade_out = True

class SceneB(arcade.View):
    def __init__(self):
        super().__init__()
        # 배경 스프라이트 설정
        self.background_sprite = arcade.Sprite("scene_b_background.png", scale=1.0)
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        # 페이드 인 관련 변수
        self.alpha = 0

    def on_draw(self):
        self.background_sprite.alpha = self.alpha  # 투명도 적용
        self.background_sprite.draw()

    def on_update(self, delta_time):
        # 페이드 인 효과: alpha 값을 증가시킴
        self.alpha += 5
        if self.alpha > 255:
            self.alpha = 255  # alpha 값은 최대 255로 유지

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.current_view = SceneA()
        self.show_view(self.current_view)

# 게임 실행
window = MyGame()
arcade.run()
