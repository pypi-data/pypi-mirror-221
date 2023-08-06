import arcade
from importlib.resources import files
from robot_rumble.Characters.entities import Entity

from arcade import gl

from robot_rumble.Characters.death import Player_Death
from robot_rumble.Characters.entities import Entity
from robot_rumble.Util import constants
from robot_rumble.Util.spriteload import load_spritesheet_pair, load_spritesheet_pair_nocount
from robot_rumble.Characters.Player.playerBase import PlayerBase


class PlayerFighter(PlayerBase):
    def __init__(self):
        super().__init__()
        # Load textures
        self.idle_r, self.idle_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "idle.png", 2, 32, 32)
        self.attack_r, self.attack_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "attack_unmasked.png", 37, 48, 32)
        self.running_r, self.running_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "run_unmasked.png", 8, 32, 32)
        self.running_attack_r, self.running_attack_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "attack_unmasked.png", 37, 48, 32)
        # FIX
        self.jumping_r, self.jumping_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "jump_unmasked.png", 7, 32, 32)
        self.jumping_attack_r, self.jumping_attack_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "attack_unmasked.png", 7, 48, 32)
        self.damaged_r, self.damaged_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "damaged_masked.png", 6, 32, 32)
        self.blocking_r, self.blocking_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "flashing.png", 2, 32, 32)

        self.sparkle_r, self.sparkle_l = load_spritesheet_pair_nocount("robot_rumble.assets.fighter_assets", "sparkle.png", 13, 32, 32)
        self.sparkle = [0, self.sparkle_r]

        self.idle = [0, self.idle_r]
        self.running = [0, self.running_r]
        self.jumping = [0, self.jumping_r]
        self.damaged = [0, self.damaged_r]
        self.dash = [0, self.dash_r]
        self.attack = [0, self.attack_r]
        self.running_attack = [0, self.running_attack_r]
        self.jumping_attack = [0, self.jumping_attack_r]
        self.blocking = [0, self.blocking_r]

        self.PLAYER_MOVEMENT_SPEED = constants.MOVE_SPEED_PLAYER

        # Set an initial texture. Required for the code to run.
        self.texture = self.idle_r[0]

        self.slash_can_hit = [True, True, True, True]
        self.jump_can_hit = True
        self.slashes = [7, 14, 24]
        self.character = 2

        self.death.change_player_type("fighter")



    def update(self,delta_time):
        super().update(delta_time)

    def update_animation(self, delta_time):
        super().update_animation(delta_time)

        if self.fix_slash:
            self.slash_can_hit = [True, True, True, True]
            self.fix_slash = False
            self.jump_can_hit = True

        if not self.is_blocking and not self.is_damaged:
            # This condition must mean that the player WAS jumping but has landed
            if self.change_y == 0 and self.is_jumping and \
                    (self.texture == self.jumping[1][4]
                     or self.texture == self.jumping_attack[1][6]):
                # Update the tracker for future jumps
                self.is_jumping = False
                self.jumping_attack[0] = 0
                # Animation depending on whether facing left or right and moving or still
                if self.change_x == 0:
                    if self.is_attacking:
                        self.texture = self.attack[1][self.attack[0]]
                    else:
                        self.texture = self.idle[1][self.idle[0]]
                else:
                    if self.is_attacking:
                        self.texture = self.running_attack[1][self.running_attack[0]]
                    else:
                        self.texture = self.running[1][self.running[0]]
                return

            # Moving
            if self.change_x != 0 or self.change_y != 0:
                # Check to see if the player is jumping (while moving right)
                if self.change_y != 0:
                    self.is_jumping = True
                    if self.is_attacking:
                        self.texture = self.jumping_attack[1][self.jumping_attack[0]]
                    # Check if the player is mid-jump or mid-fall, and adjust which sprite they're on accordingly
                    # We DON'T loop back to 1 here because the character should hold the pose until they start falling.
                    if self.is_attacking:
                        if self.jumping_attack[0] >= 6:
                            self.jumping_attack[0] = 0
                            self.is_attacking = False
                            self.jumping[0] = 3
                        else:
                            self.jumping_attack[0] = self.jumping_attack[0] + 1
                return

