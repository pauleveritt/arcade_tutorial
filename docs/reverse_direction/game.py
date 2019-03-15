import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.position = 0
        self.velocity = 200
        self.radius = 30

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        arcade.draw_circle_filled(self.position, y, self.radius, arcade.color.RED)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

        # Did the circle hit the right side of screen?
        is_at_right = self.position > self.width - self.radius
        if is_at_right:
            self.velocity *= -1


def main():
    game1 = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game1.position = 10
    arcade.run()


if __name__ == '__main__':
    main()
