import arcade


def main():
    arcade.open_window(600, 600, 'Coin Game')
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()
    arcade.draw_text('Drawing Example', 200, 300, arcade.color.BLACK, 12)
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()
