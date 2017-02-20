from math import pi, sin, cos

import arcade
from random import randrange, random

SPRITE_SCALING = 0.5
GRAVITY = 0.3
BOUNCINESS = 0.5


class Coin(arcade.Sprite):
    filename = 'examples/images/coin_01.png'
    scaling = SPRITE_SCALING / 3

    def __init__(self, screen_width, screen_height):
        super().__init__(self.filename, self.scaling)
        self.center_x = 0
        self.center_y = 0
        self.angle = random() * 2 * pi
        self.radius = randrange(10, 200)
        self.speed = 0.008
        self.circle_center_x = randrange(screen_width)
        self.circle_center_y = randrange(screen_height)

    def update(self):
        self.center_x = self.radius * sin(self.angle) \
                        + self.circle_center_x
        self.center_y = self.radius * cos(self.angle) \
                        + self.circle_center_y

        self.angle += self.speed


class Player(arcade.Sprite):
    def __init__(self, filename, scaling, screen_x, screen_y):
        super().__init__(filename, scaling)
        self.center_x = 0
        self.center_y = 0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.velocity_x = 5
        self.velocity_y = 0

    def update(self):
        self.center_x += self.velocity_x
        self.center_y += self.velocity_y
        self.velocity_y -= GRAVITY

        is_at_right = self.center_x > self.screen_x
        is_moving_right = self.velocity_x > 0
        if is_at_right and is_moving_right:
            self.velocity_x *= -BOUNCINESS

        is_at_left = self.center_x < 1
        is_moving_left = self.velocity_x < 0
        if is_at_left and is_moving_left:
            self.velocity_x *= -BOUNCINESS

        is_at_top = self.center_y > self.screen_y
        is_moving_up = self.velocity_y > 0
        if is_at_top and is_moving_up:
            self.velocity_y *= -BOUNCINESS

        is_at_bottom = self.center_y < 1
        is_moving_down = self.velocity_y < 0
        if is_at_bottom and is_moving_down:
            # If we bounce with a decent velocity, do a normal bounce.
            # Otherwise we won't have enough time resolution to accurate
            # represent
            # the bounce and it will bounce forever. So we'll divide the
            # bounciness
            # by half to let it settle out.
            if self.velocity_y * -1 > GRAVITY * 15:
                self.velocity_y *= -BOUNCINESS
            else:
                self.velocity_y *= -BOUNCINESS / 2

    def go_right(self):
        self.velocity_x = abs(self.velocity_x) * -1

    def go_left(self):
        self.velocity_x = abs(self.velocity_x)

    def go_up(self):
        self.velocity_y += 10


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)

        # Make a player
        self.player = Player('examples/images/character.png', SPRITE_SCALING,
                             width, height)

        # Make sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

        for i in range(20):
            coin = Coin(width, height)
            self.coin_list.append(coin)
            self.all_sprites_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.go_right()
        elif key == arcade.key.RIGHT:
            self.player.go_left()
        elif key == arcade.key.UP:
            self.player.go_up()


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.player.center_x = 1
    arcade.run()


if __name__ == '__main__':
    main()
