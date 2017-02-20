import arcade

if __name__ == '__main__':
    arcade.open_window('Drawing Example', 600, 600)
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()
