import arcade

SPRITE_SCALING = 0.5


class Player(arcade.Sprite):
    def __init__(self, filename, scaling, screen_x, screen_y):
        super().__init__(filename, scaling)
        self.center_x = 0
        self.center_y = 0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.velocity = 1

    def update(self):
        self.center_x += self.velocity

        # Did the player hit the right side of the screen while moving right?
        is_at_right = self.center_x > self.screen_x
        is_moving_right = self.velocity > 0
        if is_at_right and is_moving_right:
            self.velocity *= -1

        # Same for left edge
        is_at_left = self.center_x < 1
        is_moving_left = self.velocity < 0
        if is_at_left and is_moving_left:
            self.velocity *= -1

    def go_right(self):
        self.velocity = abs(self.velocity) * -1

    def go_left(self):
        self.velocity = abs(self.velocity)

    def go_up(self):
        self.center_y += 10

    def go_down(self):
        self.center_y += -10


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)

        # Make a player
        self.player = Player('examples/images/character.png', SPRITE_SCALING,
                             width, height)

        # Make a sprite list
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

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
        elif key == arcade.key.DOWN:
            self.player.go_down()


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.player.center_x = 1
    arcade.run()


if __name__ == '__main__':
    main()
