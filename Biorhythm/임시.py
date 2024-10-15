import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.camera = arcade.Camera2D()
        self.player_sprite = arcade.Sprite(center_x=400, center_y=300)
        self.scene = arcade.Scene()
        self.scene.add_sprite("Player", self.player_sprite)

    def on_draw(self):
        self.clear()
        with self.camera.activate():
            self.scene.draw()

    def on_update(self, delta_time):
        self.camera.position = (self.player_sprite.center_x - SCREEN_WIDTH / 2, 
                                self.player_sprite.center_y - SCREEN_HEIGHT / 2)

class MenuView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Menu Screen - click to start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Camera2D Example with Views")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
