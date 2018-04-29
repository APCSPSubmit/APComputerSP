import pygame
from data import constants
import platforms

class Level():
    """Super-cass that defines all levels. Create a child class for each level with level-specific info"""

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
                    collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
    # Update everything on this level
    def update(self):
        """Update everything in this level"""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on the screen"""

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3,0))

        #Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right we need to scroll everything"""

        # Keep track of the shift amount:
        self.world_shift += shift_x

        #Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """Definition for level 1."""

    def __init__(self, player):
        """ Create level 1"""

        # Call the parent constructor:

        Level.__init__(self, player)

        self.background = pygame.image.load("resources\graphics\Final.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        #Array with type of platform, and x, y location of the platform.

        level = [ [platforms.GROUND_BLOCK, 0, 287],
                  [platforms.GROUND_BLOCK, 16, 287],
                  [platforms.GROUND_BLOCK, 32, 287],
                  [platforms.GROUND_BLOCK, 48, 287],
                  [platforms.GROUND_BLOCK, 64, 287],
                  [platforms.GROUND_BLOCK, 80, 287],
                  [platforms.GROUND_BLOCK, 96, 287],
                  [platforms.GROUND_BLOCK, 112, 287],
                  [platforms.GROUND_BLOCK, 128, 287],
                  [platforms.GROUND_BLOCK, 144, 287],
                  [platforms.GROUND_BLOCK, 160, 287],
                  [platforms.GROUND_BLOCK, 176, 287],
                  [platforms.GROUND_BLOCK, 192, 287],
                  [platforms.GROUND_BLOCK, 208, 287],
                  [platforms.GROUND_BLOCK, 224, 287],
                  [platforms.GROUND_BLOCK, 240, 287],
                  [platforms.GROUND_BLOCK, 256, 287],
                  [platforms.GROUND_BLOCK, 272, 287],
                  [platforms.GROUND_BLOCK, 288, 287],
                  [platforms.GROUND_BLOCK, 304, 287],
                  [platforms.GROUND_BLOCK, 320, 287],
                  [platforms.GROUND_BLOCK, 336, 287],
                  [platforms.GROUND_BLOCK, 352, 287],
                  [platforms.GROUND_BLOCK, 368, 287],
                  [platforms.GROUND_BLOCK, 384, 287],
                  [platforms.GROUND_BLOCK, 400, 287],
                  [platforms.GROUND_BLOCK, 416, 287],
                  [platforms.GROUND_BLOCK, 432, 287],
                  [platforms.GROUND_BLOCK, 448, 287],
                  [platforms.GROUND_BLOCK, 464, 287],
                  [platforms.GROUND_BLOCK, 480, 287],
                  [platforms.GROUND_BLOCK, 496, 287],
                  [platforms.GROUND_BLOCK, 512, 287],
                  [platforms.GROUND_BLOCK, 528, 287],
                  [platforms.GROUND_BLOCK, 544, 287],
                  [platforms.GROUND_BLOCK, 560, 287],
                  [platforms.GROUND_BLOCK, 576, 287],
                  [platforms.GROUND_BLOCK, 592, 287],
                  [platforms.GROUND_BLOCK, 608, 287],
                  [platforms.GROUND_BLOCK, 624, 287],
                  [platforms.GROUND_BLOCK, 640, 287],
                  [platforms.GROUND_BLOCK, 656, 287],
                  [platforms.GROUND_BLOCK, 672, 287],
                  [platforms.GROUND_BLOCK, 688, 287],
                  [platforms.GROUND_BLOCK, 704, 287],
                  [platforms.GROUND_BLOCK, 720, 287],
                  [platforms.GROUND_BLOCK, 736, 287],
                  [platforms.GROUND_BLOCK, 752, 287],
                  [platforms.GROUND_BLOCK, 768, 287],
                  [platforms.GROUND_BLOCK, 784, 287],
                  [platforms.GROUND_BLOCK, 800, 287],
                  [platforms.GROUND_BLOCK, 816, 287],
                  [platforms.GROUND_BLOCK, 832, 287],
                  [platforms.GROUND_BLOCK, 848, 287],
                  [platforms.GROUND_BLOCK, 864, 287],
                  [platforms.GROUND_BLOCK, 880, 287],
                  [platforms.GROUND_BLOCK, 896, 287],
                  [platforms.GROUND_BLOCK, 912, 287],
                  [platforms.GROUND_BLOCK, 928, 287],
                  [platforms.GROUND_BLOCK, 944, 287],
                  [platforms.GROUND_BLOCK, 960, 287],
                  [platforms.GROUND_BLOCK, 976, 287],
                  [platforms.GROUND_BLOCK, 992, 287],
                  [platforms.GROUND_BLOCK, 1008, 287],
                  [platforms.GROUND_BLOCK, 1024, 287],




        ]
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
