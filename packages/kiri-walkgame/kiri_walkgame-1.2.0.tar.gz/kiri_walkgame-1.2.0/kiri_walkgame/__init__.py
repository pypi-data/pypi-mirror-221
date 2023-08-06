#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:23:42 2023

@author: Anthony Chow

"""
from io import BytesIO
import argparse
import sys
import pygame
import numpy as np
from kiri_pathfinding.map_generator import generate_map
from kiri_pathfinding import PathFinding
from kiri_walkgame.characters import Kiri, Button
from kiri_walkgame.shortcuts import SOURCES, equal_pos
from kiri_walkgame.output import map_to_png


RATIO = 20
COST_RATIOS = [5, 15, 20, 1]
FPS = 20


class Game:
    """
    the main class of the game

    """

    __panel_size = RATIO * 4

    __margin = RATIO

    __c_size = RATIO * 2  # character's size

    def __init__(self, size=20, width=None, **kwargs):
        size, width = self.__init_args(size, width)
        self.height, self.width = size * RATIO, width * RATIO
        self.__generate_map(size, width, **kwargs)
        self.__stop = None
        self.__queue = []
        self.__channel = None
        self.__init_character()
        self.__init_target()
        self.__init_buttons()
        self._reset()

        self._running = False
        self._waiting = False
        self.screen = None
        self.__to_flip = False
        self.__volume = True

    @staticmethod
    def __init_args(size, width):
        if width is None:
            width = size
        assert isinstance(size, int) and isinstance(width, int)
        return size, width

    @property
    def _stopped(self):
        "test if the game stopped"
        return (any((x is None for x in (self.start, self.stop))) or
                equal_pos(self.start, self.stop))

    def __init_character(self):
        character = Kiri(self.__c_size, FPS)
        self.__kiri = character

    def __init_target(self):
        self.__target = pygame.transform.scale(
            pygame.image.load(SOURCES.box), (self.__c_size, self.__c_size))

    def __init_buttons(self):
        self.__buttons = []
        height = self.__panel_size - self.__margin * 2
        width = int(height * 2)
        self.__init_b_reset(width, height)
        self.__init_b_voice(width, height)

    def __init_meow(self):
        self.__meow = pygame.mixer.Sound(SOURCES.audios.meow)
        self.__channel = pygame.mixer.find_channel()

    def __play_meow(self):
        if self.__channel is None:
            return
        self.__stop_meow()
        self.__channel.play(self.__meow, loops=-1)

    def __stop_meow(self):
        if self.__channel is None:
            return
        self.__channel.fadeout(2)

    def __play_music(self):
        pygame.mixer.music.load(
            SOURCES.audios.Fantasy_by_Pufino_on_freetouse_com)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(self.__volume)

    def __init_b_reset(self, width, height):
        position = (self.__margin, self.height + self.__margin * 2)
        button = Button(SOURCES.icons.refresh,
                        position=position, size=(width, height),
                        action=self.__e_reset)
        self.__buttons.append(button)

    def __e_reset(self, *args, **kwargs):
        self.__generate_map(self.height // RATIO, self.width // RATIO)
        self._reset()
        self.__to_flip = True

    def __e_volumn(self, *args, **kwargs):
        self.__volume = not self.__volume
        pygame.mixer.music.set_volume(self.__volume)
        self.__channel.set_volume(self.__volume)

    def __init_b_voice(self, width, height):
        position = (self.__margin + self.width - width,
                    self.height + self.__margin * 2)
        button = Button(
            (SOURCES.icons.voice_on, SOURCES.icons.voice_off),
            position=position, size=(width, height),
            action=self.__e_volumn)
        self.__buttons.append(button)

    def __generate_map(self, height, width, **kwargs):
        self.map = generate_map(height, width, **kwargs)
        map_size = self.width, self.height
        self.__window_size = (
            map_size[0] + self.__margin * 2,
            map_size[1] + self.__margin + self.__panel_size)

        # get bg image
        map_to_show = BytesIO()
        map_to_png(self.map, map_to_show)
        map_to_show.seek(0)
        self.__img_bg = pygame.transform.scale(
            pygame.image.load(map_to_show), map_size)

    def _reset(self):
        "reset the map and status"
        # game status
        self.start = None
        self.stop = None
        self.__queue.clear()
        self.cost = 0
        self.expected_cost = 0
        self.__kiri.reset()

    @property
    def stop(self):
        "the target point"
        return self.__stop

    @stop.setter
    def stop(self, val):
        self.__stop = val
        self.__set_queue()
        self.__play_meow()

    def __draw_background(self):
        self.screen.fill((255, 255, 255))
        map_position = (self.__margin, self.__margin)
        self.screen.blit(self.__img_bg, map_position)

    def __draw_kiri(self):
        return self.__kiri.draw(self.screen)

    def __move_kiri(self):
        # refuse to control kiri when it is moving
        if self.start is None or self.__kiri.moving:
            return

        # place kiri in a position
        if self.__kiri._current_pos is None:
            speed = 1
        # move kiri to a new position
        else:
            speed = COST_RATIOS[self.map[tuple(self.start)]] * 3

        position = self.__c_pixel_to_position(self.__kiri, self.start)
        self.__kiri.move(position, speed)

    def __draw_target(self):
        if self.stop is None:
            return
        position = self.__c_pixel_to_position(self.__target, self.stop)
        return self.screen.blit(self.__target, position)

    def __c_pixel_to_position(self, character, pixel):
        "return a adjust position for characters"
        position = self.__pixel_to_position(pixel)
        width, height = character.get_size()
        position = (position[0] - (width + RATIO) / 2, position[1] - height)
        return position

    def __pixel_to_position(self, pixel):
        "transform the pixel on the map to the position on the screen"
        return [x * RATIO + self.__margin + RATIO for x in pixel][::-1]

    def __position_to_pixel(self, position):
        "transform the position on the screen to the pixel on the map"
        return [(x - self.__margin) // RATIO for x in position][::-1]

    def on_init(self):
        "init the game"
        pygame.init()
        logo = pygame.image.load(SOURCES.logo)
        pygame.display.set_icon(logo)
        pygame.display.set_caption("kiri walk game")
        self.screen = pygame.display.set_mode(self.__window_size)
        self.__draw_background()
        self.__draw_buttons()
        pygame.display.flip()
        self.__play_music()
        self.__init_meow()
        self._running = True

    def __on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            return
        if self._waiting:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__event_on_buttons(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.__set_start_stop(event)
            return

    def __event_on_buttons(self, event):
        for button in self.__buttons:
            if button.on_event(event):
                return True
        return False

    def __draw_buttons(self):
        rects = []
        for button in self.__buttons:
            rects.append(button.draw(self.screen))
        return rects

    def __set_start_stop(self, event):
        "set the start point and stop point"
        if event.button != 1:
            return
        pixel = self.__position_to_pixel(event.pos)
        if not self.__check_pixel(pixel):
            return
        if self.start is None:
            self.start = pixel
        # elif self.stop is None or self._stopped:
        else:
            self.stop = pixel

    def __check_pixel(self, pixel):
        "test if the pixel still in the map"
        pixel = np.asarray(pixel)
        return np.all((pixel >= 0) & (pixel < self.map.shape))

    def __set_queue(self):
        "set queue to move"
        if self._stopped or self.stop is None:
            return
        self.__kiri.stop()
        self.__queue = PathFinding(self.map, cost_ratios=COST_RATIOS).find(
            tuple(self.start), tuple(self.stop))[:0:-1]

    def __on_loop(self):
        # next point
        if not self.__kiri.moving and len(self.__queue) > 0:
            self.start = self.__queue.pop()
        self.__move_kiri()

        # kiri reach the point
        if self._stopped and not self.__kiri.moving:
            self.__stop_meow()

    def __on_render(self, pre_rects):
        rects = []
        self.__draw_background()
        rects.extend(self.__draw_buttons())
        rects.append(self.__draw_target())
        rects.append(self.__draw_kiri())

        # kiri get into the box
        if equal_pos(self.start, self.stop) and not self.__kiri.moving:
            rects.append(self.__draw_target())
        if self.__to_flip:
            pygame.display.flip()
            rects = [self.screen.get_rect()]
            self.__to_flip = False
        else:
            pygame.display.update(pre_rects + rects)
        return rects

    def __on_cleanup(self):
        pygame.quit()

    def on_run(self):
        "run the game"
        self.on_init()

        clock = pygame.time.Clock()
        pre_rects = []
        while (self._running):
            for event in pygame.event.get():
                self.__on_event(event)
            self.__on_loop()
            pre_rects = self.__on_render(pre_rects)
            clock.tick(FPS)
        self.__on_cleanup()


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', required=False,
                        help='Height of the map, the default is 20.',
                        default=20, type=int)
    parser.add_argument('-w', '--width', required=False,
                        help='Width of the map, the default is same as @size',
                        default=None, type=int)
    return parser.parse_args(sys.argv[1:])


def main():
    "Execute"
    args = init_args()
    game = Game(args.size, args.width)
    game.on_run()


if __name__ == '__main__':
    main()
