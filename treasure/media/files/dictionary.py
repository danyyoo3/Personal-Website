import re
from collections import defaultdict
import pygame
import sys
import random
import os


class WordDictionary:

    width, height = 500, 600
    r = 25
    b = 198
    g = 26
    green_changer = 1

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.dictionary = defaultdict(list)
        self._running = True
        self._adding = False
        self._seeing = False
        self._gaming = False
        self._empty = True
        self._word_fall = False
        self._snake = False
        self._text = ''
        self._search = ''
        self._result = ''
        self._eraser = ''
        self._cooldown = 0
        self._points = 0
        self._random_set = set()
        self._falling_words = []

        self._snake_width = 25
        self._snake_height = 30
        self._snake_length = 1
        self._x = 0
        self._y = 0
        self._velx = 0
        self._vely = 0
        self._snake_length = 1
        self._isfood = True
        self._blocksize = 20
        self._foodx = 0
        self._foody = 0

    def run(self)-> None:
        """Main pygame funning function"""
        pygame.init()

        
        window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('My Dictionary')

        
        while self._running:
            self._handle_events()
            
            while self._adding:
                self._handle_events_add()
                self._update_background()
                self._adding_screen(window)
                pygame.display.flip()
                pygame.display.update()
                
            while self._seeing:
                self._handle_events_show()
                self._update_background()
                self._showing_screen(window)
                pygame.display.flip()
                pygame.display.update()

            while self._gaming:
                self._handle_events_games()
                self._update_background()
                self._games_screen(window)
                pygame.display.flip()
                pygame.display.update()
                while self._word_fall:
                    self._handle_events_wordfall()
                    self._update_background()
                    self._word_fall_screen(window)
                    if self._cooldown == 0:
                        self._fall_word()
                        self._cooldown = 100
                    else:
                        self._cooldown -= 1
                    self._game_over(window)
                    pygame.display.flip()
                    pygame.display.update()
                if self._snake:
                    self._snake_map(window)
                    self._x = random.randint(0, self._snake_width-self._blocksize)
                    self._y = random.randint(0, self._snake_height-self._blocksize)
                    pygame.display.update()
                    while self._snake:
                        self._snake_map(window)
                        if self._isfood:
                            self._foodx = random.randint(0, self._snake_width-self._blocksize)
                            self._foody = random.randint(0, self._snake_height-self._blocksize)
                            self._isfood = False
                        #self._eat_food()
                        self._make_food(window)
                        self._snake_game(window)
                        self._handle_events_snake()
                        pygame.display.flip()
                        pygame.display.update()
                
                
            self._update_background()
            self.display_title(window)
            pygame.display.flip()
            pygame.display.update()

        self.file.close()
            

            




    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        file = open('dictionary.txt', 'a+')
        file.write(word+';')
        file.close()
        #self.dictionary[len(word)].append(word)
        #self._random_set.add(word)
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        file = open('dictionary.txt', 'r')
        words = file.read().split(';')
        for w in words:
            if w == word:
                return True
        file.close()
        
##        if '.' in word:
##            pattern = "^"
##            pattern = pattern + word.replace('.', '[a-z]') + "$"
##            finder = re.compile(pattern)
##            for k in self.dictionary[len(word)]:
##                if finder.match(k) != None:
##                    return True
##            return False
##            
##        else:
##            return word in self.dictionary[len(word)]


    def _handle_events(self)-> None:
        """Handle events of user"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            #Add word
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (140 < mouse[0] < 340) and (250 < mouse[1] < 300):
                    self._adding = True

            #Search dictionary
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (140 < mouse[0] < 340) and (350 < mouse[1] < 400):
                    self._seeing = True

            #Start games
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (140 < mouse[0] < 340) and (450 < mouse[1] < 500):
                    if os.path.isfile('./dictionary.txt'):
                        self._empty = False
                        self._gaming = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                    pygame.quit()
                    sys.exit()
                
            

                        
    def _handle_events_add(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                #Adding add button
                if (140 < mouse[0] < 340) and (350 < mouse[1] < 400):
                    self.addWord(self._text)
                    self._text = ''
                    self._empty = False
                    
                #Back button
                if (140 < mouse[0] < 340) and (450 < mouse[1] < 500):
                    self._adding = False

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.addWord(self._text)
                    self._text = ''
                    self._empty = False
                elif event.key == pygame.K_ESCAPE:
                    self._adding = False
                else:
                    self._text += event.unicode
                    
                    
    def _handle_events_show(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                #Search button
                if (140 < mouse[0] < 340) and (350 < mouse[1] < 400):
                    result = self.search(self._search)
                    if result:
                        self._result = "Word is in dictionary!"
                    else:
                        self._result = "Word is not in dictionary!"

                #Back button
                if (140 < mouse[0] < 340) and (450 < mouse[1] < 500):
                    self._seeing = False

                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._search = self._search[:-1]
                elif event.key == pygame.K_ESCAPE:
                        self._seeing = False
                elif event.key == pygame.K_RETURN:
                    result = self.search(self._search)
                    if result:
                        self._result = "Word is in dictionary!"
                    else:
                        self._result = "Word is not in dictionary!"
                    
                else:
                    self._search += event.unicode

    def _handle_events_wordfall(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self._eraser = self._eraser[:-1]
                    elif event.key==pygame.K_RETURN:
                        self._delete_word()
                        self._eraser = ''
                    elif event.key == pygame.K_ESCAPE:
                        self._word_fall = False
                    else:
                        self._eraser += event.unicode

    def _handle_events_games(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._gaming = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                #wordfall game button
                if (140 < mouse[0] < 340) and (100 < mouse[1] < 150):
                    self._create_dictionary()
                    self._falling_words = []
                    self._word_fall = True
                    self._points = 0
                    
                #snake game
                if (140 < mouse[0] < 340) and (175 < mouse[1] < 225):
                    self._snake_length = 1
                    self._snake = True

    def _handle_events_snake(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._snake = False
                    self._x = 0
                    self._y = 0
                    self._velx = 0
                    self._vely = 0
                    self._snake_length = 1

                if event.key == pygame.K_UP and self._vely == 0:
                    self._vely = -0.03
                    self._velx = 0
                if event.key == pygame.K_DOWN and self._vely == 0:
                    self._vely = 0.03
                    self._velx = 0
                if event.key == pygame.K_RIGHT and self._velx == 0:
                    self._velx = 0.03
                    self._vely = 0
                if event.key == pygame.K_LEFT and self._velx == 0:
                    self._velx = -0.03
                    self._vely = 0
            



    def display_title(self, window)->None:
        title_font = pygame.font.SysFont('didot.ttf', 70)
        text = title_font.render('MY DICTIONARY', True, pygame.Color(255,255,255))
        textRect = text.get_rect()  
        textRect.center = (250, 125)
        window.blit(text, textRect)

        title_font = pygame.font.SysFont('didot.ttf', 32)
        
        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 250, 200, 50))
        add_text = title_font.render("ADD WORD", True, pygame.Color(255,255,255))
        add_rect = add_text.get_rect()
        add_rect.center = (240, 275)
        window.blit(add_text, add_rect)

        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 350, 200, 50))
        see_text = title_font.render("SEARCH DICT", True, pygame.Color(255,255,255))
        see_rect = see_text.get_rect()
        see_rect.center = (240, 375)
        window.blit(see_text, see_rect)
    
        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 450, 200, 50))
        play_text = title_font.render("PLAY GAMES", True, pygame.Color(255,255,255))
        play_rect = play_text.get_rect()
        play_rect.center = (240, 475)
        window.blit(play_text, play_rect)


        if not os.path.isfile('./dictionary.txt'):
            word_font = pygame.font.SysFont('didot.ttf', 30)
            message = word_font.render('Dictionary is empty', True, pygame.Color(255,255,255))
            window.blit(message, (145, 520))

        
        

    def _adding_screen(self,window)->None:
        """Screen for adding word to dictionary"""
        title_font = pygame.font.SysFont('didot.ttf', 70)
        text = title_font.render('ADD YOUR WORD', True, pygame.Color(255,255,255))
        textRect = text.get_rect()  
        textRect.center = (250, 125)
        window.blit(text, textRect)
        
        title_font = pygame.font.SysFont('didot.ttf', 32)

        word_input = title_font.render(self._text, True, pygame.Color(255,255,255))
        window.blit(word_input, (150, 250))

        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 350, 200, 50))
        add_text = title_font.render("ADD WORD", True, pygame.Color(255,255,255))
        add_rect = add_text.get_rect()
        add_rect.center = (240, 375)
        window.blit(add_text, add_rect)

        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 450, 200, 50))
        see_text = title_font.render("BACK", True, pygame.Color(255,255,255))
        see_rect = see_text.get_rect()
        see_rect.center = (240, 475)
        window.blit(see_text, see_rect)

    def _showing_screen(self, window)->None:
        title_font = pygame.font.SysFont('didot.ttf', 70)
        text = title_font.render('SEARCH', True, pygame.Color(255,255,255))
        text2 = title_font.render('DICTIONARY', True, pygame.Color(255,255,255))
        textRect = text.get_rect()  
        textRect.center = (250, 125)
        window.blit(text, textRect)
        
        textRect2 = text2.get_rect()  
        textRect2.center = (250, 175)
        window.blit(text2, textRect2)
        
        title_font = pygame.font.SysFont('didot.ttf', 32)
        result_font = pygame.font.SysFont('didot.ttf', 25)

        word_input = title_font.render(self._search, True, pygame.Color(255,255,255))
        window.blit(word_input, (150, 250))

        result_text = result_font.render(self._result, True, pygame.Color(255,0,0))
        window.blit(result_text, (150, 300))

        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 350, 200, 50))
        add_text = title_font.render("SEARCH", True, pygame.Color(255,255,255))
        add_rect = add_text.get_rect()
        add_rect.center = (240, 375)
        window.blit(add_text, add_rect)
        
        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 450, 200, 50))
        see_text = title_font.render("BACK", True, pygame.Color(255,255,255))
        see_rect = see_text.get_rect()
        see_rect.center = (240, 475)
        window.blit(see_text, see_rect)

    def _word_fall_screen(self, window)->None:
        title_font = pygame.font.SysFont('didot.ttf', 30)
        text = title_font.render('Press ESC to exit', True, pygame.Color(255,255,255))
        window.blit(text, (150, 30))

        points = title_font.render('Points:' + str(self._points), True, pygame.Color(255,255,255))
        window.blit(points, (10, 5))
        
        word_input = title_font.render(self._eraser, True, pygame.Color(255,255,255))
        window.blit(word_input, (150, 550))

        word_font = pygame.font.SysFont('didot.ttf', 40)

        
        #Adding falling words
        for w in self._falling_words:
            falword = word_font.render(w[0], True, pygame.Color(255,255,255))
            window.blit(falword, (w[1], w[2]))
            w[2] += 0.5


    def _games_screen(self, window)->None:
        title_font = pygame.font.SysFont('didot.ttf', 30)
        text = title_font.render('Choose a game', True, pygame.Color(255,255,255))
        window.blit(text, (160, 30))

        sub_font = pygame.font.SysFont('didot.ttf', 32)
        
        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 100, 200, 50))
        word_fall = sub_font.render("WORD FALL", True, pygame.Color(255,255,255))
        window.blit(word_fall, (172, 115))

        pygame.draw.rect(window, pygame.Color(240,0,0), (140, 175, 200, 50))
        snake_game = sub_font.render("SNAKE GAME", True, pygame.Color(255,255,255))
        window.blit(snake_game, (160, 190))
        

    def _create_dictionary(self)->None:
        file = open('dictionary.txt', 'r')
        self._random_set = set(file.read().split(';')[:-1])
        print(self._random_set)
        file.close()

    def _fall_word(self)->None:
        word = random.sample(self._random_set, 1)
        x_coordinate = random.randint(10, 400)
        y_coordinate = 5
        self._falling_words.append([word[0], x_coordinate, y_coordinate])
        


    def _update_background(self)->None:
        """Update changing background"""
        screen = pygame.display.get_surface()
        self.g += self.green_changer
        screen.fill(pygame.Color(self.r,self.g,self.b))
        if self.g == 198 or self.g == 25:
            self.green_changer *= -1


    def _delete_word(self)->None:
        for w in self._falling_words:
            if self._eraser == w[0]:
                i = self._falling_words.index(w)
                self._falling_words.pop(i)
                self._points += 1

    def _game_over(self, window)->None:
        if self._word_fall:
            for w in self._falling_words:
                if w[2] >= 550:
                    title_font = pygame.font.SysFont('didot.ttf', 70)
                    game_over = title_font.render('GAME OVER', True, pygame.Color(255,255,255))
                    window.blit(game_over, (100, 200))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    self._gaming = False
        
        

    def _snake_map(self, window)->None:
        screen = pygame.display.get_surface()
        screen.fill(pygame.Color(0,0,0))
        for x in range(int(self.width/20)):
            for y in range(int(self.height/20)):
                rect = pygame.Rect(x*self._blocksize, y*self._blocksize, \
                                   self._blocksize, self._blocksize)
                pygame.draw.rect(window, pygame.Color(255,255,255), rect, 1)

        
    
    def _snake_game(self, window)->None:
        self._x += self._velx
        self._y += self._vely
        for i in range(self._snake_length+1):
            if (self._x+(i*20)) > self._snake_width:
                self._x = 0
                rect = pygame.Rect((self._x+(i*20))*self._blocksize,\
                                   (self._y+(i*20))*self._blocksize, \
                                  self._blocksize, self._blocksize)
                player = pygame.draw.rect(window, pygame.Color(255,0,0), rect, 1)
                window.fill(pygame.Color(255,0,0), player)
            elif (self._x+(i*20)) < 0:
                self._x = self._snake_width
                rect = pygame.Rect((self._x+(i*20))*self._blocksize,\
                                   (self._y+(i*20))*self._blocksize, \
                                  self._blocksize, self._blocksize)
                player = pygame.draw.rect(window, pygame.Color(255,0,0), rect, 1)
                window.fill(pygame.Color(255,0,0), player)
            elif (self._y+(i*20)) < 0:
                self._y = self._snake_height
                rect = pygame.Rect((self._x+(i*20))*self._blocksize,\
                                   (self._y+(i*20))*self._blocksize, \
                                  self._blocksize, self._blocksize)
                player = pygame.draw.rect(window, pygame.Color(255,0,0), rect, 1)
                window.fill(pygame.Color(255,0,0), player)
            elif (self._y+(i*20)) > self._snake_height:
                self._y = 0
                rect = pygame.Rect((self._x+(i*20))*self._blocksize,\
                                   (self._y+(i*20))*self._blocksize, \
                                  self._blocksize, self._blocksize)
                player = pygame.draw.rect(window, pygame.Color(255,0,0), rect, 1)
                window.fill(pygame.Color(255,0,0), player)
            else:
                rect = pygame.Rect((self._x+(i*20))*self._blocksize,\
                                   (self._y+(i*20))*self._blocksize, \
                                  self._blocksize, self._blocksize)
                player = pygame.draw.rect(window, pygame.Color(255,0,0), rect, 1)
                window.fill(pygame.Color(255,0,0), player)




    def _eat_food(self)->None:
        if (self._foodx <= self._x <= self._foodx + self._blocksize) and \
            (self._foody <= self._y <= self._foody + self._blocksize):
            self._snake_length += 1
            self._isfood = True
            print(self._snake_length)
##        if self._foodx <= self._x + self._blocksize <= self._foodx + self._blocksize or \
##            self._foodx <= self._x <= self._foodx + self._blocksize or \
##            self._foody <= self._y <= self._foody + self._blocksize or \
##            self._foody <= self._y + self._blocksize <= self._foody + self._blocksize:
##            self._snake_length += 1
##            self._isfood = True

    def _make_food(self, window)->None:
        food = pygame.Rect(self._foodx*self._blocksize, self._foody*self._blocksize, \
                           self._blocksize,self._blocksize)
        pygame.draw.rect(window, pygame.Color(255,0,0), food, 1)
        window.fill(pygame.Color(255,255,51), food)
        


        


if __name__ == "__main__":
    WordDictionary().run()

    #Snake game:add making snake longer, remove and add new food
    
    #games with the words you have
    #Add difficulty to word falling game
    #In search menu, delete the words
    
    #island app. Can be able to create island and show the perimeter of the island
    
