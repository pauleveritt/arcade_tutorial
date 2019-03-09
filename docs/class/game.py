import arcade

GAME_TITLE = 'Drawing Example'


class MyGame(arcade.Window):
    def on_draw(self):
        arcade.set_background_color(arcade.color.WHEAT)
        arcade.start_render()
        arcade.draw_text(GAME_TITLE, 200, 300, arcade.color.BLACK, 12)


def main():
    game = MyGame(600, 600, GAME_TITLE)
    arcade.run()


if __name__ == '__main__':
    main()
