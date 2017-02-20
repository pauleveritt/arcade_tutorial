import arcade

GAME_TITLE = 'Drawing Example'
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


def on_draw(delta_time):
    arcade.start_render()
    arcade.draw_text(GAME_TITLE, 200, 300, arcade.color.BLACK, 12)


def main():
    arcade.open_window(GAME_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.schedule(on_draw, 1 / 2)
    arcade.run()


if __name__ == '__main__':
    main()
