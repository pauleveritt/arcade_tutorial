import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.title = title

    def on_draw(self):
        arcade.start_render()
        x = self.width / 2
        y = self.height / 2
        arcade.draw_text(self.title, x, y, arcade.color.BLACK, 12)


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    arcade.run()

if __name__ == '__main__':
    main()
