import arcade

SPRITE_SCALING = 0.5


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.velocity = 1

        # Make a player
        self.player = arcade.Sprite('examples/images/character.png',
                                    SPRITE_SCALING)
        self.player.center_x = 0
        self.player.center_y = 0

        # Make a sprite list
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.player.center_x += self.velocity * delta_time

        # Did the circle hit the right side of the screen while moving right?
        is_at_right = self.player.center_x > self.width
        is_moving_right = self.velocity > 0
        if is_at_right and is_moving_right:
            self.velocity *= -1

        # Same for left edge
        is_at_left = self.player.center_x < 1
        is_moving_left = self.velocity < 0
        if is_at_left and is_moving_left:
            self.velocity *= -1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.velocity = abs(self.velocity) * -1
        elif key == arcade.key.RIGHT:
            self.velocity = abs(self.velocity)
        elif key == arcade.key.UP:
            self.player.center_y += 10
        elif key == arcade.key.DOWN:
            self.player.center_y -= 10


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.player.center_x = 1
    game.velocity = 200
    arcade.run()


if __name__ == '__main__':
    main()
