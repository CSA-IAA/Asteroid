'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Asteroid
Version 3.0
'''

import pygame
import sys
import random
import time
def newGame():
    background = (0, 0, 0)
    entity_color = (255, 255, 255)

    global spedIncr
    spedIncr = 5

    laser_list = []
    asteroid_list = []
    asteroid_list2 = []
    #scores
    global score
    score = 0
    global lives
    lives = 3

    newLevel = 50 #for when you have to make asteroids faster
    newAsteroid = newLevel
    newLevel2 = 50 #for when you have to make asteroids faster
    newAsteroid2 = newLevel2


    def draw_text(surf, text, font_size, x, y): #for showing higscores
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, entity_color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    class Background(pygame.sprite.Sprite): #game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

    class Entity(pygame.sprite.Sprite):
        """Inherited by any object in the game."""

        def __init__(self, x, y, width, height):
            pygame.sprite.Sprite.__init__(self)

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            # This makes a rectangle around the entity, used for anything
            # from collision to moving around.
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    class DestroyerShip(Entity):
        """
        Player controlled or AI controlled, main interaction with
        the game
        """

        def __init__(self, x, y, width, height):
            super(DestroyerShip, self).__init__(x, y, width, height)

            self.image = spaceship #makes spaceship accessible to player class

    class Player(DestroyerShip):
        """The player controlled Destroyer"""

        def __init__(self, x, y, width, height):
            super(Player, self).__init__(x, y, width, height)

            # How many pixels the Player Destroyer should move on a given frame.
            self.y_change = 0
            # How many pixels the Destroyer should move each frame a key is pressed.
            self.y_dist = 5

        def MoveKeyDown(self, key):
            """Responds to a key-down event and moves accordingly"""

            if (key == pygame.K_UP):
                self.y_change += -self.y_dist

            elif (key == pygame.K_DOWN):
                self.y_change += self.y_dist

            elif (key == pygame.K_SPACE):
                # Fires a laser when the user clicks the spacebar
                # Sets the laser so that it comes out from the appropriate place
                x = Laser(player.rect.x + 85, player.rect.y + 47, 5, 2) #where laser comes out of the Destroyer
                # Add the laser to the lists
                all_sprites_list.add(x)
                laser_list.append(x)
                soundObj2.play()  # plays it for this function

        def MoveKeyUp(self, key):
            """Responds to a key-up event and stops movement accordingly"""

            if (key == pygame.K_UP):
                self.y_change += self.y_dist

            elif (key == pygame.K_DOWN):
                self.y_change += -self.y_dist

        def update(self):
            """
            Moves the Destroyer while ensuring it stays in bounds
            """
            # Moves it relative to its current location.
            self.rect.move_ip(0, self.y_change)
            # If the Destroyer moves off the screen, put it back on.
            if self.rect.y < 30:
                self.rect.y = 30
            elif self.rect.y > (window_height - self.height) + 50: #since there is box around ship makes sure the actual ship thing can reach bottom
                self.rect.y = (window_height - self.height) + 50

    class Laser(Entity):
        """ This class represents the laser . """

        def __init__(self, x, y, width, height):
            super(Laser, self).__init__(x, y, width, height)

            self.image = laser  #sets laser as sprite
            self.x_direction = 5

        def update(self):
            """ Move the laser. """
            self.rect.x += 8

    class Asteroid(Entity):
        """
        The Asteroid!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Asteroid, self).__init__(x, y, width, height)

            self.image = asteroidImg
            #Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            #Moves the asteroid left
            self.rect.x -= spedIncr

    class Asteroid2(Entity):
        """
        The Asteroid!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Asteroid2, self).__init__(x, y, width, height)

            self.image = asteroidImg2
            #Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            #Moves the asteroid left
            self.rect.x -= spedIncr

    def LasAstCol(asteroids,lasers): #Checks to see if the laser hit an asteroid and removes BOTH laser and asteroid while adding score
        global score
        global spedIncr
        for asta in asteroids:
            for lasa in laser_list:
                if asta.rect.colliderect(lasa):
                    soundObj.play()  # plays it for this duration, play explosion first cuz its weird if there is explosion with no asteroid
                    asta.remove(all_sprites_list)
                    lasa.remove(all_sprites_list)
                    asteroids.remove(asta)
                    lasers.remove(lasa)
                    score += 100 #increases score by 100 each time an asteroid is hit
                    spedIncr +=.3 #increases the speed by .1

    def LasAstCol2(asteroids,lasers): #Checks to see if the laser hit an asteroid and removes BOTH laser and asteroid while adding score
        global score
        global spedIncr
        for asta in asteroids:
            for lasa in laser_list:
                if asta.rect.colliderect(lasa):
                    soundObj.play()  # plays it for this duration, play explosion first cuz its weird if there is explosion with no asteroid
                    asta.remove(all_sprites_list)
                    lasa.remove(all_sprites_list)
                    asteroids.remove(asta)
                    lasers.remove(lasa)
                    score += 250 #increases score by 250 each time an asteroid is hit, 250 incase have to choose between another asteroid. 250-100 = 150, 50 increase from reg asteroid
                    spedIncr +=.3 #increases the speed by .1

    def DatHitTho(all): #Checks to see if if spaceship collided with asteroid and removes asteroid
        global lives
        for a in all:
            if a.rect.colliderect(player.rect):
                all.remove(a)
                a.remove(all_sprites_list)
                lives -= 1
    def DatHitTho2(all): #Checks to see if if spaceship collided with asteroid and removes asteroid
        global lives
        for a in all:
            if a.rect.colliderect(player.rect):
                all.remove(a)
                a.remove(all_sprites_list)
                lives -= 1

    pygame.init()

    #screen info
    window_width = 950
    window_height = 500
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Asteroid")
    clock = pygame.time.Clock()
    screen.fill([255, 255, 255])

    #images
    spaceship = pygame.image.load('destroyer1.png')
    laser = pygame.image.load('laser2.png')
    laser = pygame.transform.scale(laser, (36, 12))

    BackGround = Background('space.png', [0, 0])
    asteroidImg = pygame.image.load('asteroid1.png')#imports asteroid pic
    asteroidImg2 = pygame.image.load('asteroid2.png')#imports asteroid pic

    #sprites,lists
    player = Player(0, 130,165, 160)
    asteroid = Asteroid(window_width, random.randint(20,window_height-60),100,73) #100 and 73 are the actual dimensions of the image
    asteroid_list.append(asteroid)
    asteroid2 = Asteroid2(window_width, random.randint(20,window_height-60),100,73) #100 and 73 are the actual dimensions of the image
    asteroid_list2.append(asteroid2)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(asteroid)
    all_sprites_list.add(asteroid2)
    all_sprites_list.add(player)

    #text
    basicfont = pygame.font.SysFont(None, 35)  # 35 is font size, no font type
    basicfont2 = pygame.font.SysFont(None, 35)  # 35 is font size, no font type
    highscore = pygame.font.SysFont(None, 25)  # 25 is font size, no font type

    #music
    pygame.mixer.music.load('DarkKnight.mp3') #imports the music
    pygame.mixer.music.play(-1, 0.0) #duration of the music, in this case -1 means forever
    soundObj = pygame.mixer.Sound('Explosion.wav')  # imports the music on standby
    soundObj2 = pygame.mixer.Sound('Laser.wav')  # imports the music on standby
    soundObj3 = pygame.mixer.Sound('Fail.wav')  # imports the music on standby

    end_it = False
    while (end_it == False):
        screen.blit(BackGround.image, BackGround.rect)
        myfont = pygame.font.SysFont(None, 40)
        nlabel = myfont.render("Welcome to my Asteroid Game!", 1, (255, 0, 0))
        nLabel2 = myfont.render("You'll have fun shooting lasers at asteroids with The Destroyer!", 1, (255, 0, 0))
        nLabel3 = myfont.render("Left click the mouse to get started!", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #so game doesnt get all glitchy when you try to exit without this code
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Left mouse button.
                    end_it = True #stops the while true
        screen.blit(nlabel,(250,1))
        screen.blit(nLabel2,(40,50))
        screen.blit(nLabel3,(250,350))
        pygame.display.flip()

    while True:
        LasAstCol(asteroid_list, laser_list) #if laser collide with asteroid
        DatHitTho(asteroid_list) #if asteroid hit The Destroyer
        LasAstCol2(asteroid_list2, laser_list) #if laser collide with asteroid
        DatHitTho2(asteroid_list2) #if asteroid hit The Destroyer

        if newAsteroid <= 0: #Creates asteroids after set amount of time
            if len(asteroid_list) < 12 and lives > 0:
                x = Asteroid(window_width - 1, random.randint(20, window_height - 60), 100, 73) #100 and 73 are the actual dimensions of the image
                asteroid_list.append(x)
                all_sprites_list.add(x)
                newLevel -= .5 #each time an asteroid is formed we make it shorter until next is made
                newAsteroid = newLevel

        if newAsteroid2 <= 0: #Creates asteroids after set amount of time
            if lives > 0:
                x2 = Asteroid2(window_width - 1, random.randint(20, window_height - 60), 100, 73) #100 and 73 are the actual dimensions of the image
                asteroid_list2.append(x2)
                all_sprites_list.add(x2)
                newLevel2 -= .07  # each time an asteroid is formed we make it shorter until next is made
                newAsteroid2 = newLevel2

        # Event processing here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                pygame.mixer.music.stop()
                soundObj.stop()
                soundObj2.stop()
                soundObj3.stop()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)

        for ent in all_sprites_list:
            ent.update()

        #checks to see if asteroid off screen
        for asto in asteroid_list:
            if asto.rect.x <= 0:
                asto.remove(all_sprites_list)
                asteroid_list.remove(asto)
                score -= 100
        #checks to see if laser off screen
        for laso in laser_list:
            if laso.rect.x >= 910:
                laso.remove(all_sprites_list)
                laser_list.remove(laso)
        #checks to see if special asteroid off screen
        for asto in asteroid_list2:
            if asto.rect.x <= 0:
                asto.remove(all_sprites_list)
                asteroid_list2.remove(asto)

        screen.blit(BackGround.image, BackGround.rect)

        #prints the scores to the GUI
        text = basicfont.render("Player: "+str(score), True, entity_color, (BackGround.image, BackGround.rect))  # first set of parenthesis is the font color, second set is the background of the words
        screen.blit(text, (50, 10))
        text2 = basicfont2.render("Lives: "+str(lives), True, entity_color, (BackGround.image, BackGround.rect))  # first set of parenthesis is the font color, second set is the background of the words
        screen.blit(text2, (750, 10))

        if lives == 0:
            try:
                pygame.mixer.music.stop()
                soundObj3.play()

                draw_text(screen, "Game Over!", 32, 475, 10)
                draw_text(screen, "Your score: "+str(score), 32, 475, 45)
                draw_text(screen,"Top Ten High Scores:",25,472,80)

                outfile = open("highscore.txt", "a")
                outfile.write(str(score) + '\n')
                infile = open("highscore.txt", "r")
                l=[]
                aline = infile.readline()
                db = []
                while aline:
                    l.append(aline)
                    aline = infile.readline()

                l.append(str(score))
                #original places, restarts everything as if new
                del asteroid_list[:]
                del asteroid_list2[:]
                del laser_list[:]
                newAsteroid = 50
                spedIncr = 5
                player.rect.y = 130
                score = 0 #put score here cuz it put same place as lives wont change and if palced above .flip(), it becoems buggy

                for ab in l:
                    db.append(int(ab))
                db = sorted(db, reverse=True)
                db=db[:10]

                infile.close()

                cn = 105
                hn=1

                for i in db:
                    draw_text(screen, str(hn)+". "+str(i).replace('\n',''), 25, 472, cn)
                    cn+=25
                    hn+=1

                outfile.close()
                soundObj.stop()
                soundObj2.stop()

                end_it = False
                while (end_it == False):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # so game doesnt get all glitchy when you try to exit without this code
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:  # Left mouse button.
                                end_it = True  # stops the while true
                    pygame.display.flip()
                    pygame.time.wait(5000)
                    newGame()
                    lives = 3


            except FileNotFoundError: #in case file does not exist
                with open('highscore.txt', 'w') as outfile:
                    for i in range(10):
                        outfile.write("0" + "\n")

        all_sprites_list.draw(screen)
        newAsteroid -= .5
        newAsteroid2 -= .07
        pygame.display.flip()

        clock.tick(60)
newGame()