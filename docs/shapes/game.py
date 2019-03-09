import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.position = 0
        self.velocity = 10
        self.radius = 30

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        arcade.draw_circle_filled(self.position, y, self.radius, arcade.color.RED)

    def update(self, delta_time):
        self.position += self.velocity


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.position = 1
    arcade.run()


if __name__ == '__main__':
    main()
