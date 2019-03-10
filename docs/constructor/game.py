import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.title = title

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.title, 200, 300, arcade.color.BLACK, 12)


def main():
    game1 = MyGame(600, 600, 'Drawing Example')
    arcade.run()


if __name__ == '__main__':
    main()
