import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.y = 0
        self.velocity = 200
        self.radius = 30
        self.x = self.radius

    def reverse(self):
        self.velocity *= -1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.RED)

    def update(self, delta_time):
        self.x += self.velocity * delta_time

        # Did the circle hit the right or left side of the screen?
        is_at_right = self.x > self.width - self.radius
        is_at_left = self.x < self.radius
        if is_at_right or is_at_left:
            self.reverse()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.reverse()
        elif key == arcade.key.UP:
            self.y += 10
        elif key == arcade.key.DOWN:
            self.y -= 10


def main():
    game1 = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    arcade.run()


if __name__ == '__main__':
    main()
