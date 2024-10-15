import arcade
from arcade import open_window
from arcade.gui import UIAnchorLayout, UIEvent, UIFlatButton, UIView, UIDropdown, UIOnChangeEvent


A = -1
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Panel(UIAnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.with_background(color=arcade.uicolor.RED_POMEGRANATE)
        self.with_border(color=arcade.uicolor.WHITE_CLOUDS, width=2)

        button = self.add(UIDropdown(default="asdf", options=["1920 X 1080", "1280 X 720", "640 X 360"]))
        button.on_change = self.on_dropdown_change

    def on_dropdown_change(self, event: UIOnChangeEvent):
        if event.new_value == "1280 X 720":
            print("@@@@@@@@@@@@@@@@@@@@@@@")

class MyView(UIView):
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.BLACK

        # code to reproduce the error goes here

        root = self.add_widget(UIAnchorLayout())

        root.add(UIFlatButton(text="Button"), anchor_x="left", anchor_y="center")

        root.add(Panel(size_hint=(0.5, 0.5)))

        self.SpriteList = arcade.SpriteList()
        self.Sprite = arcade.Sprite(":resources:gui_basic_assets/icons/smaller.png", 1, )
        self.SpriteList.append(self.Sprite)

    def on_draw_before_ui(self):
        self.SpriteList.draw()
        pass

    def on_draw_after_ui(self):
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        global SCREEN_WIDTH, SCREEN_HEIGHT
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
            return True

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
            return True
        
        if symbol == arcade.key.A:
            SCREEN_WIDTH = 1920
            SCREEN_HEIGHT = 1080
            self.window.set_size(SCREEN_WIDTH, SCREEN_HEIGHT)

        if symbol == arcade.key.B:
            SCREEN_WIDTH = 720
            SCREEN_HEIGHT = 480
            self.window.set_size(SCREEN_WIDTH, SCREEN_HEIGHT) 
        
    """def on_draw(self):
        self.SpriteList.draw()"""

class Aclass(arcade.View):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    open_window(window_title="Minimal example", width=SCREEN_WIDTH, height=SCREEN_HEIGHT, resizable=False).show_view(
        MyView()
    )
    arcade.run()