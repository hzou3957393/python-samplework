from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.x = 20
        self.y = 20
        
        self.title_lbl = Label(self, text="Roman Numeral Canvas")
        self.title_lbl.grid(row = 0, column = 0, columnspan = 5)

        self.number_lbl = Label(self, text = "Number:")
        self.number_lbl.grid(row = 1, column = 1)

        self.number_entry = Entry(self, width = 30)
        self.number_entry.grid(row = 1, column = 2)

        self.numbers = BooleanVar()
        self.numbers.set(False)

        Checkbutton(self, text = "Numbers", variable = self.numbers).grid(row = 1, column = 3, columnspan = 2)

        self.line_wid_lbl = Label(self, text = "Line Width:")
        self.line_wid_lbl.grid(row = 2, column = 1)

        self.line_width = StringVar()
        ##setting my default to width of 1
        self.line_width.set("1")

        Radiobutton(self, text = "1", variable = self.line_width, value = "1").grid(row = 2, column = 2)
        Radiobutton(self, text = "3", variable = self.line_width, value = "3").grid(row = 2, column = 3)
        Radiobutton(self, text = "5", variable = self.line_width, value = "5").grid(row = 2, column = 4)

        self.color_lbl = Label(self, text = "Line Color:")
        self.color_lbl.grid(row = 3, column = 1)
        
        self.line_color = StringVar()
        #setting my default to black
        self.line_color.set("black")

        Radiobutton(self, text = "Black", variable = self.line_color, value = "black").grid(row = 3, column = 2)
        Radiobutton(self, text = "Red", variable = self.line_color, value = "red").grid(row = 3, column = 3)
        Radiobutton(self, text = "Blue", variable = self.line_color, value = "blue").grid(row = 3, column = 4)

        self.random_gif = PhotoImage(file = "random.gif")
        self.roman_gif = PhotoImage(file = "roman.gif")
        
        self.roman_bttn = Button(self, image = self.roman_gif, command = self.draw_letter)
        self.roman_bttn.grid(row = 4, column = 2)

        self.random_bttn = Button(self, image = self.random_gif, command = self.random_draw)
        self.random_bttn.grid(row = 4, column = 3, columnspan = 2)

        self.canvas = Canvas(self, height = 310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 4)

    ## this function runs a loop through the string in the entry
    ## the corresponding letters would be drawn, tested by if and elif statements
    ## each time a letter is drawn, the x coordinate must move 10 pixels to the right of the previous letter
    ## when the line of letters reach the end of the canvas box, the x coordinate is back at 20 and the y coordinate is 10 pixels below the previous line

    ## NOTE: This code works most times I ran to test it, though on a couple occasions, typing a string of letters in the enty would give me an error message something about "bad spacing" in my first canvas.create_line line. I am not sure why.
    def draw_letter(self):
        width = 20
        height = 40
        line_width = int(self.line_width.get())
        color = self.line_color.get()
        for letter in self.number_entry.get():
            ## M has total of 8 lines
            if letter.upper() == "M":
                self.canvas.create_line(self.x, self.y, self.x + (width/2), self.y + (height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + (height/4), self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + width, self.y, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y, self.x + (width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (5*width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y + height,self.x + (width/4), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y + height, self.x + (5*width/4), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## D has 6 lines
            elif letter.upper() == "D":
                self.canvas.create_line(self.x, self.y, self.x + (width/2), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width, self.y + (height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + height, self.x + width, self.y + (3*height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x + width, self.y + (3*height/4), self.x + width, self.y + (height/4), width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## C has 5 lines
            elif letter.upper() == "C":
                self.canvas.create_line(self.x, self.y + (height/4), self.x + (width/2), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + (height/4), self.x, self.y + (3*height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + (3*height/4), self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## L has 3 lines
            elif letter.upper() == "L":
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y, self.x + (width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## X has 4 lines
            elif letter.upper() == "X":
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/4), self.y, self.x + (3*width/4), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (width/4), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## V has 4 lines
            elif letter.upper() == "V":
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/4), self.y, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            ## I has 3 lines
            elif letter.upper() == "I":
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width/2, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20

            ## this sets the next letter to be 10 pixels to the right of the previous letter
            ## if it gets to the end of the canvas box, it will start the x back at 20 and start 10 pixels below the previous line of letters
##            self.x += width + 10
##            if self.x >= 490:
##                self.y += height + 10
##                self.x = 20
            ##I ended up putting this under every if and elif statement in my for loop for the draw_letter method because this needs to happen every time a letter is drawn

    ##for the random button,  I am pasting all of my code for my draw_letter method here and modifying it
    ##instead of setting the line_width and fill variables at the beginning of the method outside the loop, I am setting it inside every if and elif statement using the random.choice() method
    ## for width, I am choosing between 1 - 5, and for fill, I put the colors options in a list and using the choice method to choose one
    def random_draw(self):
        width = 20
        height = 40
        
        for letter in self.number_entry.get():
            if letter.upper() == "M":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x + (width/2), self.y + (height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + (height/4), self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + width, self.y, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y, self.x + (width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (5*width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y + height,self.x + (width/4), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y + height, self.x + (5*width/4), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "D":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x + (width/2), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width, self.y + (height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + height, self.x + width, self.y + (3*height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x + width, self.y + (3*height/4), self.x + width, self.y + (height/4), width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "C":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y + (height/4), self.x + (width/2), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + (height/4), self.x, self.y + (3*height/4), width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + (3*height/4), self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "L":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y, self.x + (width/4), self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x - (width/4), self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "X":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/4), self.y, self.x + (3*width/4), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (width/4), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "V":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/4), self.y, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (3*width/4), self.y, self.x + (width/2), self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
            elif letter.upper() == "I":
                line_width = random.choice([1, 2, 3, 4, 5])
                color = random.choice(["black", "red", "blue", "green"])
                self.canvas.create_line(self.x, self.y, self.x + width, self.y, width = line_width, fill = color)
                self.canvas.create_line(self.x, self.y + height, self.x + width, self.y + height, width = line_width, fill = color)
                self.canvas.create_line(self.x + (width/2), self.y, self.x + width/2, self.y + height, width = line_width, fill = color)
                self.x += width + 10
                if self.x >= 490:
                    self.y += height + 10
                    self.x = 20
                    
## Attempted to write a conversion from number to letters in step 5, but had no time to finish
##    def convert(self, number_string):
##        string = ""
##        if len(number) == 4:
##            string += "M" * int(number_string[0])
##            if int(number_string[1]) >= 5:
##                string += "D"
##                string += "C" * (int(number_string[1] - 5)
##            else:
##                string += "C" * int(number_string[1])
# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("900x350")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
