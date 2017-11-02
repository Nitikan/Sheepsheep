import arcade

from models import Sheep,World

from random import randint




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



        super().draw()



class SpaceGameWindow(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

 

        arcade.set_background_color(arcade.color.LEMON_MERINGUE)

        self.world = World(width,height)

        self.sheep_sprite = ModelSprite('images/sheep.png',0.15,model=self.world.sheep)

        self.grass_sprite = ModelSprite('images/grass.png',0.15,model=self.world.grass)

        self.enemy = []
        for i in self.world.enemy:
             self.enemy.append(ModelSprite('images/wolf.png',0.15,model=i))    

        self.bush_sprite = ModelSprite('images/bush.png',0.5,model=self.world.bush)



    def on_key_press(self, key, key_modifiers):

        self.world.on_key_press(key, key_modifiers)

    def update(self, delta):

        self.world.update(delta)


    def on_draw(self):

        arcade.start_render()

        self.sheep_sprite.draw()

        self.grass_sprite.draw()


        for i in self.enemy:
            i.draw()

        self.bush_sprite.draw()

        arcade.draw_text(str(self.world.score),

                         self.width - 50, self.height - 50,

                         arcade.color.GRAY, 40)

if __name__ == '__main__':


    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)

    arcade.run()