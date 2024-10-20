import arcade

from globals import SCREEN_WIDTH, SCREEN_HEIGHT, SCALING, SCREEN_TITLE,FULLSCREEN_RECT, DRAW_RATE # 전역변수 갖고오기
from title_menu import TitleMenu


# 게임 실행
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True, fixed_rate=1/60, draw_rate=DRAW_RATE)
    first_view = TitleMenu()
    first_view.setup()
    window.show_view(first_view)
    arcade.run()
    
if __name__ == "__main__":
    main()
    
