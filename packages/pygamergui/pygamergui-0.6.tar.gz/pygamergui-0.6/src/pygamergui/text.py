# importing random module for random ints
import random
import pygame
import time

class Word_Animation:
    """this is the class for word animation it scrambles the word
    and then unscramle it one by one """
    def __init__(self,word,font=None, size=38, color = "white"):
        self.word = word #--------> the variable that stores words
        self.scr = '' #-----------> it will store scrambled word
        self.spaceafter = [] #---> this list stores where to put spaces
        self.set_space_after()# -> this function sets the place to put spaces after
        self.scramble()# --------> this function scrambles the word
        self.size = size
        self.color = color
        self.font=None
        self.run=True
        self.txt_surface=None
        pygame.font.init()
        if font is None:
            self.font = pygame.font.Font("freesansbold.ttf", size)
        else:
            self.font = pygame.font.Font(font, size)
#-----------------------------------------------------------------------------------
    def set_space_after(self):
        '''this function ittrate over the word and stores the
        position where it found spaces in self.spaceafter list'''
        for i,j in enumerate(self.word):
            if j == " ":
                self.spaceafter.append(i)
#------------------------------------------------------------------------------------
    def scramble(self):
        """this function stores self.word variable in local variable word
        and removes spces in order to remove spaces forming in the middle of words
        we ittrate over i to length of word. add space if len of scr is in
        spaceafter list and we add random letter from word to scr"""
        word=self.word.replace(' ','')
        for i in range(len(word)):
            rand = random.randint(1,len(word)-1)
            if len(self.scr) in self.spaceafter:
                self.scr += ' '
            self.scr += word[rand]
        """ this code add a space if and extra space is in last of word"""
        if len(self.scr) < len(self.word) and self.word[len(self.word)-1]:
            self.scr += " "
#--------------------------------------------------------------------------------------
    def unscramble(self):
        """this function does following:
        1. ittrates over self.scr and srore its letters in lst
        2. ittrate over i to len of self.word and changes the ith value of lst to ith value of self.word
        3. converts lst to str and prints
        """
        lst = []
        rlst = []
        anmi = ''
        for leetrs in self.scr:
            lst.append(leetrs)
        for i in range(len(self.word)):
            lst[i]=self.word[i]
            for j in lst:
                anmi+=j
            rlst.append(anmi)
            anmi=''
        return rlst
#---------------------------------------------------------------------------------------
    def show(self, window, x, y, for_frame):
            if self.run == True:
                rlist = self.unscramble()
                for i in rlist:
                    window.set_fps(for_frame,self.run)
                    if window.bgimg is not None:
                        window.scren.blit(window.bgimg,(0,0))
                    else:
                        window.scren.fill("black")
                    self.txt_surface = self.font.render(i, True, self.color)
                    window.scren.blit(self.txt_surface, (x, y))
                    pygame.display.update()
                    window.colock.tick(window.fps)
                    if i == rlist[len(rlist)-1]:
                        self.run=False
            window.set_fps(for_frame,self.run)
            window.scren.blit(self.txt_surface, (x, y))


# @class for text------------


class text:
    def __init__(self, text, color='white', size=38, font=None):
        self.text = text
        self.color = color
        self.size = size
        pygame.font.init()
        if font is None:
            self.font = pygame.font.Font("freesansbold.ttf", size)
        else:
            self.font = pygame.font.Font(font, size)

    def show(self, window, x, y):
        txt_surface = self.font.render(self.text, True, self.color)
        window.scren.blit(txt_surface, (x, y))


#class for text_typed


class Text_Typed:
    def __init__(self, font=None, size=38, wait=5, text="simple text", color="white"):
        pygame.font.init()
        self.font = font
        self.size = size
        self.wait = wait
        self.run = True
        self.text = text
        self.color = color
        self.r_l_wrd = self.setwrd("rl")
        if font is None:
            self.font = pygame.font.Font("freesansbold.ttf", self.size)
        else:
            self.font = pygame.font.Font(font, self.size)

    def setwrd(self,case):
        match case:
            case 'lr':
                lst=[]
                wrd=""
                for i in self.text:
                        wrd+=i
                        lst.append(wrd)
                return lst
        
    def show_l_r(self, window, x,y):
        if self.run:
            wrd=self.setwrd("lr")
            for i in wrd:
                window.scren.blit(window.bgimg, (0, 0))
                self.txt_surface = self.font.render(i, True, self.color)
                window.scren.blit(self.txt_surface, (x, y))
                pygame.display.update()
                window.colock.tick(window.fps)
                if i == self.text:
                    self.run=False
                window.set_fps(self.wait, self.run)
        self.txt_surface = self.font.render(self.text, True, self.color)        
        window.scren.blit(self.txt_surface, (x, y))
    

