import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.position = 0
        self.velocity = 1
        self.radius = 30

    def reverse(self):
        self.velocity *= -1

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        arcade.draw_circle_filled(self.position, y, 30, arcade.color.RED)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

        # Did the circle hit the right/left side of screen?
        is_at_right = self.position > self.width - self.radius
        is_at_left = self.position < self.radius
        if is_at_right or is_at_left:
            self.reverse()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.reverse()


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.position = 1
    game.velocity = 200
    arcade.run()


if __name__ == '__main__':
    main()
