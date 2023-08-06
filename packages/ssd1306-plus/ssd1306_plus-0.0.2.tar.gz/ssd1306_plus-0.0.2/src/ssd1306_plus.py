# Import and augment the SSD1306_I2C library
from ssd1306 import SSD1306_I2C

class SSD1306_PLUS(SSD1306_I2C):
    def draw_sprite(self,sprite,x,y,fill_character,clear_character):
        rows = sprite.split("\n")
        for i in range(len(rows)):
            if len(rows[i]) == 0:
                continue
            for j in range(len(rows[i])):
                if rows[i][j] == fill_character:
                    self.pixel(x+j,y+i,1)
                elif rows[i][j] == clear_character:
                    self.pixel(x+j,y+i,0)
