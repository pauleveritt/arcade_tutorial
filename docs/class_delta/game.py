import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.title = title
        self.position = 0

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        message = self.title + ': ' + str(self.position)
        arcade.draw_text(message, self.position, y, arcade.color.BLACK, 12)

    def update(self, delta_time):
        self.position += 1


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.position = 100
    arcade.run()


if __name__ == '__main__':
    main()
