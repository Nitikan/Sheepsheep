import arcade.key

from random import randint

class Model:

    def __init__(self, world, x, y, angle):

        self.world = world

        self.x = x

        self.y = y

        self.angle = 0

    def hit(self, other, hit_size):

        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Sheep(Model):

    def __init__(self, width, height, x, y):

        self.x = x
        
        self.y = y

        self.speedx = 0

        self.speedy = 0
        
        self.width = width

        self.height = height

        self.angle = 0

    def update(self, delta):

        self.x += self.speedx

        self.y += self.speedy

        if self.x > self.width :

            self.x = 0
        
        elif self.x < 0 :

            self.x = self.width 
        
        elif self.y > self.height:

            self.y = 0

        elif self.y < 0:

            self.y = self.height

class Grass(Model):

    def __init__(self, world, x, y):

        super().__init__(world, x, y, 0)

    def random_location(self):

        self.x = randint(0, self.world.width - 1)

        self.y = randint(0, self.world.height - 1)

class Wolf(Model):

    def __init__(self, world, x, y):

        super().__init__(world, x, y, 0)
        
        self.speedx = randint(-7,7)
        self.speedy = randint(-7,7)
        self.x = randint(0, self.world.width - 1)

        self.y = randint(0, self.world.height - 1)

    def walk(self):
        self.x += self.speedx
        self.y += self.speedy
    
        if self.x > self.world.width or self.x < 0 :

            self.speedx *= -1
        
        if self.y > self.world.height or self.y < 0:

            self.speedy *= -1



class Bush(Model):

    def __init__(self, world, x, y):

        super().__init__(world, x, y, 0)

    def random_location(self):

        self.x = randint(0, self.world.width - 1)

        self.y = randint(0, self.world.height - 1)

class World:

    def __init__(self, width, height):

        self.width = width

        self.height = height

        self.grass= Grass(self, 400, 400)

        self.sheep = Sheep(self.width, self.height , 600, 400)
        self.enemy = []
        for i in range(4):
            self.enemy.append(Wolf(self, 800, 100))
        
        self.bush = Bush(self, 50, 50)
        self.dotx = self.bush.x + 128
        self.doty = self.bush.y + 128
        self.status = 0
        self.score = 0

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.UP:

            self.sheep.speedy = 5

            #self.sheep.speedx = 0

            self.sheep.angle = -180
        
        elif key == arcade.key.DOWN: 
    
            self.sheep.speedy = -5

            #self.sheep.speedx = 0
            
            self.sheep.angle = 0
        
        elif key == arcade.key.RIGHT: 

            self.sheep.speedx = 5

            self.sheep.speedy = 0

            self.sheep.angle = 90
        
        elif key == arcade.key.LEFT:

            self.sheep.speedx = -5

            self.sheep.speedy = 0

            self.sheep.angle = -90
        

    def update(self, delta):
        if(self.status == 0):
            self.sheep.update(delta)
            #self.wolf.walk()
            for i in self.enemy:
                i.walk()
        
            if self.sheep.hit(self.grass, 15):

                self.grass.random_location()

                self.score += 1
        
            for i in self.enemy:
                if(i.x<self.dotx and i.y <self.doty):
                    i.speedx*=-1
                    i.speedy*=-1
                if i.hit(self.sheep, 15):
                    self.status = 1

