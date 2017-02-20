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

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        arcade.draw_circle_filled(self.position, y, 30, arcade.color.RED)

    def animate(self, delta_time):
        self.position += self.velocity * delta_time

        # Did the circle hit the right side of the screen while moving right?
        is_at_right = self.position > self.width - self.radius
        is_moving_right = self.velocity > 0
        if is_at_right and is_moving_right:
            self.velocity *= -1

        # Same for left edge
        is_at_left = self.position < self.radius
        is_moving_left = self.velocity < 0
        if is_at_left and is_moving_left:
            self.velocity *= -1


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.position = 100
    game.velocity = 700
    arcade.run()


main()
