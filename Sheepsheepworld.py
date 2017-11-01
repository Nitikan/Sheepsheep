import arcade

import arcade.key

from pyglet.window import key

from models import Sheep,World

from random import randint

keys = key.KeyStateHandler()

SCREEN_WIDTH = 1200

SCREEN_HEIGHT = 800

class ModelSprite(arcade.Sprite):

    def __init__(self, *args, **kwargs):

        self.model = kwargs.pop('model', None)

 

        super().__init__(*args, **kwargs)

 

    def sync_with_model(self):

        if self.model:

            self.set_position(self.model.x, self.model.y)

            self.angle = self.model.angle

    def draw(self):

        self.sync_with_model()

        #sheep.control(keys)   

        super().draw()



class SpaceGameWindow(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

 

        arcade.set_background_color(arcade.color.LEMON)

        self.world = World(width,height)

        self.sheep_sprite = ModelSprite('images/sheep.png',0.15,model=self.world.sheep)

        self.grass_sprite = ModelSprite('images/grass.png',0.15,model=self.world.grass)

        self.wolf_sprite = ModelSprite('images/wolf.png',0.15,model=self.world.wolf)

        self.bush_sprite = ModelSprite('images/bush.png',0.3,model=self.world.bush)

        #arcade.get_window().push_handlers(keys)

    def on_key_press(self, key, key_modifiers):

        self.world.on_key_press(key, key_modifiers)

    def update(self, delta):

        self.world.update(delta)


    def on_draw(self):

        arcade.start_render()

        self.sheep_sprite.draw()

        self.grass_sprite.draw()

        self.wolf_sprite.draw()

        self.bush_sprite.draw()

        arcade.draw_text(str(self.world.score),

                         self.width - 50, self.height - 50,

                         arcade.color.WHITE, 40)

if __name__ == '__main__':

    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)

    arcade.run()