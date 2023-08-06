import arcade

from illumigator import util


class Slider:
    def __init__(self, center_x=0, center_y=0, scale=1, pos=1):
        self._pos = pos
        self.center_x = center_x
        self.center_y = center_y
        self.scale = scale

        self.slider_width = 128 * scale
        self.rel_cursor_pos = (
            center_x - self.slider_width // 2
        ) + pos * self.slider_width
        self.slider = util.load_sprite(
            "slider.png", scale=scale, center_x=center_x, center_y=center_y
        )
        self.cursor = util.load_sprite(
            "cursor.png", scale=scale, center_x=self.rel_cursor_pos, center_y=center_y
        )

        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.pos = self.pos - 0.01
        if self.right:
            self.pos = self.pos + 0.01

        self.cursor.center_x = (
            self.center_x - self.slider_width // 2
        ) + self._pos * self.slider_width

    def draw(self):
        self.slider.draw(pixelated=True)
        self.cursor.draw(pixelated=True)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        if pos < 0:
            self._pos = 0
        elif pos > 1:
            self._pos = 1
        else:
            self._pos = pos


class MainMenu:
    @staticmethod
    def draw():
        options = ("Press ENTER to start",
                   "Press O to select an official level",
                   "Press C to select a community level",
                   "Press ESCAPE to quit")

        arcade.draw_text(
            "Illumi",
            util.X_MIDPOINT + 25,
            util.Y_MIDPOINT,
            arcade.color.YELLOW,
            util.H2_FONT_SIZE,
            anchor_x="right",
            font_name=util.MENU_FONT,
        )
        arcade.draw_text(
            "Gator",
            util.X_MIDPOINT + 25,
            util.Y_MIDPOINT,
            arcade.color.GREEN,
            util.H2_FONT_SIZE,
            anchor_x="left",
            font_name=util.MENU_FONT,
            bold=True,
        )

        for i in range(len(options)):
            arcade.draw_text(
                options[i],
                util.X_MIDPOINT,
                util.Y_MIDPOINT - 50 * (i+1),
                arcade.color.WHITE,
                util.BODY_FONT_SIZE,
                anchor_x="center",
                font_name=util.MENU_FONT
            )


class GenericMenu:
    def __init__(self, title, options, selection=0, overlay=False):
        self.title = title
        self.options = options
        self._selection = selection
        self.overlay = overlay
        self.overlay_sprite = util.load_sprite(
                "overlay_background.png",
                scale=4,
                center_x=util.X_MIDPOINT,
                center_y=util.Y_MIDPOINT,
            )

    def draw(self):
        dy = 0
        if self.overlay:
            self.overlay_sprite.draw(pixelated=True)
        else:
            arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text(
            self.title,
            util.X_MIDPOINT,
            util.Y_MIDPOINT + util.WORLD_HEIGHT // 4,
            arcade.color.WHITE,
            util.H2_FONT_SIZE,
            anchor_x="center",
            anchor_y="top",
            font_name=util.MENU_FONT,
        )
        for index, option in enumerate(self.options):
            color = arcade.color.WHITE
            if index == self._selection:
                color = arcade.color.YELLOW if self.overlay else arcade.color.RED
            arcade.draw_text(
                option,
                util.X_MIDPOINT,
                util.Y_MIDPOINT - dy,
                color,
                util.H3_FONT_SIZE,
                anchor_x="center",
                font_name=util.MENU_FONT,
            )
            dy += 50

    def increment_selection(self):
        self._selection = (
            0 if self._selection == len(self.options) - 1 else self._selection + 1
        )

    def decrement_selection(self):
        self._selection = (
            len(self.options) - 1 if self._selection == 0 else self._selection - 1
        )

    @property
    def selection(self):
        return self._selection


class ControlsMenu:
    def __init__(self):
        self.wasd_row = ("A", "S", "D")

    def draw(self):
        # ========================= Movement Key Sprites =========================
        util.load_sprite(
            "key.png",
            1,
            center_x=util.WORLD_WIDTH // 4,
            center_y=util.WORLD_HEIGHT // 2,
        ).draw(pixelated=True)
        for index in range(-1, 2):
            util.load_sprite(
                "key.png",
                1,
                center_x=util.WORLD_WIDTH // 4 + index * 64,
                center_y=util.WORLD_HEIGHT // 2 - 64,
            ).draw(pixelated=True)

        util.load_sprite(
            "arrow.png",
            1,
            center_x=util.WORLD_WIDTH // 4,
            center_y=util.WORLD_HEIGHT // 2 - 164,
        ).draw(pixelated=True)
        for index in range(-1, 2):
            util.load_sprite(
                "arrow.png",
                1,
                center_x=util.WORLD_WIDTH // 4 + index * 64,
                center_y=util.WORLD_HEIGHT // 2 - 228,
                angle=90 + (index + 1) * 90,
            ).draw(pixelated=True)

        # ========================= Rotation Key Sprites =========================
        util.load_sprite(
            "key.png",
            1,
            center_x=util.WORLD_WIDTH * 3 // 4 - 32,
            center_y=util.WORLD_HEIGHT // 2,
        ).draw(pixelated=True)
        util.load_sprite(
            "key.png",
            1,
            center_x=util.WORLD_WIDTH * 3 // 4 + 32,
            center_y=util.WORLD_HEIGHT // 2,
        ).draw(pixelated=True)

        # ========================= Titles =========================
        arcade.draw_text(
            "PRESS ESCAPE TO RETURN",
            util.WORLD_WIDTH // 2,
            util.WORLD_HEIGHT - util.H3_FONT_SIZE,
            font_size=util.H3_FONT_SIZE,
            anchor_x="center",
            anchor_y="top",
            color=arcade.color.RED,
            font_name=util.MENU_FONT,
        )
        arcade.draw_text(
            "MOVEMENT",
            util.WORLD_WIDTH // 4,
            util.WORLD_HEIGHT // 2 + 100,
            font_size=util.BODY_FONT_SIZE,
            anchor_x="center",
            font_name=util.MENU_FONT,
        )
        arcade.draw_text(
            "ROTATION",
            util.WORLD_WIDTH * 3 // 4,
            util.WORLD_HEIGHT // 2 + 100,
            font_size=util.BODY_FONT_SIZE,
            anchor_x="center",
            font_name=util.MENU_FONT,
        )

        # ========================= Movement Key Labels =========================
        arcade.draw_text(
            "W",
            util.WORLD_WIDTH // 4,
            util.WORLD_HEIGHT // 2,
            font_size=util.H3_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            color=arcade.color.BLACK_OLIVE,
            font_name=util.MENU_FONT,
        )
        for index in range(-1, 2):
            arcade.draw_text(
                self.wasd_row[index + 1],
                util.WORLD_WIDTH // 4 + index * 64,
                util.WORLD_HEIGHT // 2 - 64,
                font_size=util.H3_FONT_SIZE,
                anchor_x="center",
                anchor_y="center",
                color=arcade.color.BLACK_OLIVE,
                font_name=util.MENU_FONT,
            )

        # ========================= Rotation Key Labels =========================
        arcade.draw_text(
            "Q",
            util.WORLD_WIDTH * 3 // 4 - 32,
            util.WORLD_HEIGHT // 2,
            font_size=util.H3_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            color=arcade.color.BLACK_OLIVE,
            font_name=util.MENU_FONT,
        )
        arcade.draw_text(
            "E",
            util.WORLD_WIDTH * 3 // 4 + 32,
            util.WORLD_HEIGHT // 2,
            font_size=util.H3_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            color=arcade.color.BLACK_OLIVE,
            font_name=util.MENU_FONT,
        )


class AudioMenu:
    def __init__(self, label_list: (), volume_list: (), selection=0):
        self._selection = selection
        self.slider_list = []
        self.label_list = label_list
        self.volume_list = volume_list

        for index in range(0, len(volume_list)):
            self.slider_list.append(
                Slider(util.WORLD_WIDTH // 2, int(util.WORLD_HEIGHT * 0.66 - index * 150), 2, self.volume_list[index]))

    def draw(self):
        arcade.draw_text("PRESS ESCAPE TO RETURN",
                         util.WORLD_WIDTH // 2,
                         util.WORLD_HEIGHT - util.H3_FONT_SIZE,
                         font_size=util.H3_FONT_SIZE,
                         anchor_x="center",
                         anchor_y="top",
                         color=arcade.color.RED,
                         font_name=util.MENU_FONT
                         )

        for index in range(0, len(self.label_list)):
            arcade.draw_text(self.label_list[index] + ": " + str(int(self.slider_list[index].pos * 100)),
                             self.slider_list[index].center_x,
                             self.slider_list[index].center_y + 50,
                             font_size=util.H3_FONT_SIZE,
                             color=arcade.color.BLUE,
                             anchor_x="center",
                             font_name=util.MENU_FONT
                             )

        for index, slider in enumerate(self.slider_list):
            if index == self._selection:
                slider.slider.color = arcade.color.RED
            else:
                slider.slider.color = arcade.color.WHITE
            slider.draw()

    def update(self):
        for slider in self.slider_list:
            slider.update()

    def increment_selection(self):
        self._selection = (
            0 if self._selection == len(self.slider_list) - 1 else self._selection + 1
        )

    def decrement_selection(self):
        self._selection = (
            len(self.slider_list) - 1 if self._selection == 0 else self._selection - 1
        )

    @property
    def selection(self):
        return self._selection
