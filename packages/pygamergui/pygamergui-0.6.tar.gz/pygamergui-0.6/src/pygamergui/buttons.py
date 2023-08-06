# importing main module pygame
import pygame
from pygamergui import text

text=text.text

# @class for button---------------


class simple_button:
    """ this is to crete a simple button either with color change OR with no color change """

    def __init__(self, w=70, h=70, color=(0, 0, 255), color1=(0, 255, 0), target=None, text=None, fg="white",
                 text_size=40, args=[], font=None):
        self.h = h
        self.w = w
        self.color = color
        self.color1 = color1
        self.target = target
        self.text = text
        self.text_size = text_size
        self.fg = fg
        self.args = args
        pygame.font.init()
        if font is None:
            self.font = pygame.font.Font("freesansbold.ttf", text_size)
        else:
            self.font = pygame.font.Font(font, text_size)

    def show_no_anemi(self, x, y, window, boder_width=0, corner_round_level=0):
        # --------for target-----------
        mouse = pygame.mouse.get_pos()
        rect = pygame.Rect(x, y, self.w, self.h)
        if self.target is not None:
            if rect.collidepoint(mouse):
                if window.eve.type == pygame.MOUSEBUTTONDOWN:
                    self.target(self.args)
        # ------------------------------

        # ---------draw rect-----------------
        pygame.draw.rect(window.scren, self.color, rect, boder_width, corner_round_level)
        # ------------------------------------

        # -------for text----------------
        if self.text is not None:
            txt = self.font.render(self.text, True, self.fg)
            window.scren.blit(txt, (x + (rect.h / 20), rect.midleft[1] - 18))
        # --------------------------------

    def show_color_change(self, x, y, window, boder_width=0, corner_round_level=0):
        # -------------some variables------------
        color = self.color
        mouse = pygame.mouse.get_pos()
        rect = pygame.Rect(x, y, self.w, self.h)
        # ----------------------------------------

        # ---------for target---------------------
        if self.target is not None:
            if rect.collidepoint(mouse):
                if window.eve.type == pygame.MOUSEBUTTONDOWN:
                    self.target(self.args)
        # ---------------------------------------

        # -------------for color change----------
        if rect.collidepoint(mouse):
            if window.eve.type == pygame.MOUSEBUTTONDOWN:
                color = self.color1
        # ---------------------------------------

        # -------draw rect-------------
        pygame.draw.rect(window.scren, color, rect, boder_width, corner_round_level)
        # ------------------------------

        # -------for text----------------
        if self.text is not None:
            txt = self.font.render(self.text, True, self.fg)
            window.scren.blit(txt, (x + (rect.h / 20), rect.midleft[1] - 18))


# ---------------------------

# @class for radio-button-----


class button_radio():
    def __init__(self, radius=10, color='black'):
        self.r = radius
        self.color = color
        self.active = False

    def show(self, window, x, y):
        mouse = pygame.mouse.get_pos()
        pygame.draw.circle(window.scren, self.color, (x, y), self.r, 3)
        rect_circle = pygame.Rect(x, y, self.r * 2, self.r * 2)
        rect_circle.center = (x, y)
        if window.eve.type == pygame.MOUSEBUTTONDOWN:
            if rect_circle.collidepoint(mouse):
                if self.active == False:
                    self.active = True
                else:
                    self.active = False
        if self.active:
            pygame.draw.circle(window.scren, self.color, (x, y), self.r / 1.5)
            return True
        else:
            return False


# ----------------------------
