import random
import time
import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(self.width,self.height,"My Game")
        self.width=1000
        self.height=600
        self.background_image=arcade.load_texture("img/bg.gif")
        self.me=Player()
        self.ground_list=arcade.SpriteList()
        self.enemy_list=arcade.SpriteList()
        self.start=time.time()

        self.key=arcade.Sprite(':resources:images/items/keyYellow.png')
        self.key.center_x=100
        self.key.center_y=500
        self.key.width=45
        self.key.height=45

        self.lock=arcade.Sprite(':resources:images/tiles/lockYellow.png')
        self.lock.center_x=900
        self.lock.center_y=120
        self.lock.width=50
        self.lock.height=50
        
        for i in range(0,1090,120):
            self.ground_list.append(Ground(i,30))
        
        for i in range(400,800,120):
            self.ground_list.append(Ground(i,210))
        
        for i in range(100,400,120):
            self.ground_list.append(Ground(i,400))

        self.physics=arcade.PhysicsEnginePlatformer(self.me,self.ground_list,gravity_constant=0.4)
        self.enemy=arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background_image)
        
        self.me.draw()

        try:
            self.key.draw()
        except(AttributeError):
            pass

        self.lock.draw()

        for ground in self.ground_list:
            ground.draw()
        for enemy in self.enemy_list:
            enemy.draw()

    def on_update(self, delta_time: float):
        self.end=time.time()

        try:
            if arcade.check_for_collision(self.me,self.key):
                self.me.pocket.append(self.key)
                del self.key
        except(AttributeError):
            pass

        if len(self.me.pocket)==1:
            if arcade.check_for_collision(self.me,self.lock):
                self.lock.texture=arcade.load_texture(':resources:images/items/flagYellow2.png')


        if self.start-self.end>5:
            enemy=Enemy()
            self.enemy_list.append(enemy)
            self.enemy.append(arcade.PhysicsEnginePlatformer(enemy,self.ground_list,gravity_constant=0.4))
            self.start=time.time()

        self.physics.update()
        for item in self.enemy:
            item.update()
        
        self.me.update_animation()


    def on_key_press(self, symbol, modifiers): 
        if symbol==arcade.key.LEFT:
            self.me.change_x=-1*self.me.speed

        elif symbol==arcade.key.RIGHT:
            self.me.change_x=1*self.me.speed
        
        elif symbol==arcade.key.UP:
            if self.physics.can_jump():
                self.me.change_y=3*self.me.speed

    def on_key_release(self, symbol, modifiers):
        self.me.change_x=0

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.stand_right_textures=[arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_idle.png")]
        self.stand_left_textures=[arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_idle.png",mirrored=True)]
        
        self.walk_left_textures=[arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk0.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk1.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk2.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk3.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk4.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk5.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk6.png",mirrored=True),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk7.png",mirrored=True),  ]

        self.walk_right_textures=[arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk0.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk1.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk2.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk3.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk4.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk5.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk6.png"),
                                  arcade.load_texture(":resources:images/animated_characters/female_person/femalePerson_walk7.png"),  ]

        self.center_x=500
        self.center_y=500
        self.speed=4
        self.pocket=[]


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture=arcade.load_texture(":resources:images/animated_characters/zombie/zombie_idle.png")
        self.center_x=random.randint(0,1000)
        self.center_y=400
        self.speed=2
        self.change_x=random.choice([-1,1])*self.speed


class Ground(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.texture=arcade.load_texture(":resources:images/tiles/grassHalf.png")
        self.center_x=x
        self.center_y=y
        self.width=120
        self.height=120


game=Game()
arcade.run()