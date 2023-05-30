from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import random



class Sort_List:
    # SET THE SPEED
    def __init__(self, root):
        vis_canvas = Canvas(root, width= 594, height= 200, bg= "darkgoldenrod3")
        vis_canvas.place(x= 100, y= 90)
        pass

    

    # create list of ints
    def create_new_list(self):
        """creates list of 20 integers and sets bar_list as that list"""

        # takes the empty list "bar_list"
        global list_length
        global bar_list

        # SET SIZE OF LIST TO BE SORTED
        list_length = 20                   ###########################   THIS IS get_slider_value() IN OG, which gets bar_count
        range_first = 1
        range_last = 99

        # sets bar list to empty
        bar_list = []


        # makes the list of bars
        for i in range(0, list_length):
            bar_height = random.randint(range_first, range_last)
            bar_list.append(bar_height)

        # call make_bars to draw the bars on the screen
        self.make_bars(bar_list, ["grey" for x in range(len(bar_list))])

    # DRAW THE BARS
    def make_bars(self, bar_list, bar_color):
        # list_length is imported for mutability of shape width. 
        # if list length is shorter, shape is wider
        global list_length
        # clear bars that are on screen
        self.vis_canvas.delete("all")
        # setting the vis_canvas width (not literal size of canvas)
        vis_canvas_width = 580
        # declare shape width
        # we covered this a lot in class, and 
        # I believe this is a vector relationship
        SHAPE_WIDTH = (vis_canvas_width / list_length)
        SHAPE_GAP = 4.3
        MAX_HEIGHT = 175
        X_OFFSET = 5
        Y_OFFSET = 1
        # creates temporary array which is a list that creates a 
        # bar for each element in bar_list
        temp_array = [i / max(bar_list) for i in bar_list] 

        # for each element in the array, create a bar using vector relationship
        for i in range(len(temp_array)):
            x1 = i * SHAPE_WIDTH + SHAPE_GAP + X_OFFSET
            y1 = MAX_HEIGHT - temp_array[i] * 150
            x2 = (i + 1) * SHAPE_WIDTH + X_OFFSET
            y2 = MAX_HEIGHT + Y_OFFSET

            # this is the part that causes the bars to be drawn onscreen
            self.vis_canvas.create_rectangle(x1, y1, x2, y2, fill= bar_color[i])
            
            # text placement under the bars
            x_text = (SHAPE_WIDTH) * i + (X_OFFSET*2)
            y_text = MAX_HEIGHT + Y_OFFSET + 7
            # this is the line that writes the numbers on the vis_canvas
            # main.vis_canvas.create_text(x_text, y_text, text= f"{bar_list[i]}")                    ############################################################### THIS MIGHT BE THE PROBLEM WITH NO BARS BEING DRAWN!!!!
        # update_idletasks can be used in tkinter to redraw the widgets without calling callbacks
        # so this updates the values when I call for make_bars later
        # main.root.update_idletasks()
        # return temp_array


    def set_speed(self):
        """This function changes the DELAY size, giving the user 3 choices
        
        Args:
            .get() from the speed_menu

        returns:
            float that represents a speed

        """

        # seven DELAY options
        dead = 10000
        sluggish = 750
        slow = 500
        medium = 250
        fast = 100
        hyper = 50
        ludicrous = 1

        # # this is the part of the function that actually changes the speed using get()    ############################# was trying to incorporate speed_menu/set_speed
        # # these are all the speed option
        # # using slow speeds for bubble can cause crash if user interacts during sort
        # if speed_menu.get() == "Dead":
        #     return dead
        # if speed_menu.get() == "Sluggish":
        #     return sluggish
        # if speed_menu.get() == "Slow":
        #     return slow
        # if speed_menu.get() == "Medium":
        #     return medium
        # if speed_menu.get() == "Fast":
        #     return fast
        # if speed_menu.get() == "Hyper":
        #     return hyper
        # if speed_menu.get() == "Ludicrous":
        #     return ludicrous


        # Base function for select sort ################################################################# THE BARS AND NUMBERS SOUNT DOWN, WANT IT INSTANT
    def select_sort(self):
        """this is the function that handles the selection sort"""

        # delay so we can see what is happening
        DELAY = self.set_speed()
        length = len(bar_list)

        # for each index in the length of bar list
        for i in range(0, length - 1):
            # and for each value in the bar_list, save the first element
            for j in range(i + 1, length):
                # if the left value is larger than the right value...
                if (bar_list[i] > bar_list [j]):
                    # swap bars
                    bar_list[i], bar_list[j] = bar_list[j], bar_list[i]
                    # select_sort_activate()
                    # this colors the bars different colors as the list 
                    # is iterated through ############################################################################### COLORS ARE WRONG
                    new_bar_list = self.make_bars(bar_list, ["gold" if x == j else "black" 
                                        if x == j + 1 else "grey"
                                        for x in range(length)])
                    # time to use delay
                    self.vis_canvas.after(int(DELAY), new_bar_list)



    # Base function for bubble sort
    def bubble_sort(self):
        """this is the function that handles the bubble sort"""

        # using set_speed func to set DELAY
        DELAY = self.set_speed()
        length = len(bar_list)

        # for index in range of list excluding one
        for i in range(length - 1):
            # and for each element to the left of the previous element
            for j in range(0, length - i - 1):
                # if the number on the left is larger, swap the two bars
                if (bar_list[j] > bar_list [j + 1]):
                    bar_list[j], bar_list[j + 1] = bar_list[j + 1], bar_list[j]

                    # draw new bars using bar_list
                    # make_bars(bar_list, ["gold" if x == j else "black" if x == j+1
                    #                      else "grey" for x in range(length)])
                    
                    new_bar_list = self.make_bars(bar_list, ["gold" if x == j else "black" if x == j+1############################### COLORS DO NOT SWAP PROPERLY
                                        else "grey" for x in range(length)])
                    
                    self.vis_canvas.after(int(DELAY), new_bar_list)


    # Merge
    def merge_sort(self, bar_list, begin, mid, end, make_bars):
        """function to merge sort the passed in bar_list
        
        Args:
            bar_list: list
            begin: left index of temp array
            mid: middle of index of temp array
            end: last in index of tem_array
            make_bars: drawn bars
        
        """

        # x is left side of the array, y is right
        x = begin
        y = mid + 1
        # temporary array to start teh merge process
        temp_array = []

        # for index in length of temp array
        for i in range(begin, end + 1):
            # if left index in temp array is greater than the value 
            # at middle index
            if x > mid:
                # append the right bar to the temp array
                temp_array.append(bar_list[y])
                # increment index counter
                y += 1
            # otherwise, if the value at the right index is greater 
            # than the final index
            elif y > end:
                # append the left bar to the temp array
                temp_array.append(bar_list[x])
                x += 1
            # otherwise, if the value at the first index is less 
            # than the middle index
            elif bar_list[x] < bar_list[y]:
                # append first index in barlist to temp array
                temp_array.append(bar_list[x])
                x += 1
            else:
                # if all else fails, append y to temp array, then increment y
                temp_array.append(bar_list[y])
                y += 1

        # this sets bar_list to be the same as temp_array
        for x in range(len(temp_array)):
            bar_list[begin] = temp_array[x]
            begin += 1


    # Merge the two resultant halves from merge_sort()
    def merge(self, bar_list, begin, end, make_bars, DELAY):
        """function to combine the two halves then color the bars
        
        Args:
            bar_list: list
            begin: far left index
            end: far right index
            make_bars: make the bars
            DELAY: time delay
        
        """

        # if the first index in array is less than last
        if begin < end:
            # the midpoint is decided
            mid = int((begin + end) // 2)
            # using the start, mid and end points to recursively pass in values
            self.merge(bar_list, begin, mid, make_bars, DELAY)
            self.merge(bar_list, mid + 1, end, make_bars, DELAY)

            # combine two halves
            self.merge_sort(bar_list, begin, mid, end, make_bars)

            # draw bars onscreen as colored 
            new_bar_list = make_bars(bar_list, ["white" if x >= begin and x < mid 
                                else "gold" if x == mid else "black" 
                                if x > mid and x <= end else "grey" 
                                for x in range(len(bar_list))])
            # time.sleep(DELAY)

        # return to grey
            self.vis_canvas.after(int(DELAY), new_bar_list)