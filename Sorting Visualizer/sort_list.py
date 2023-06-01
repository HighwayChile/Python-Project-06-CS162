"""Module that creates a sortlist class that has many attributes

    Richard Sapp
    05/30/2023

    This class sorts a list of integers

"""

# import modules
import random
import time

# class to create and sort list
class SortList:
    """A class to create a list and sort it
    
    Attributes:
        root: root of the window
        vis_canvas: canvas for the visualization
        bar_count: this refers to the scale slider. included for completeness
        list_length: integer that is a placeholder at the default of 20 int
        range_first: this establishes the minimum size of the number
        range_last: establishes max size of the numbers in the list
        bar_list: list of the numbers, starts empty
        bar_color: list of bar colors, starts empty
        current_speed: is passed in when the class object is called

    """

    def __init__(self, root, vis_canvas, current_speed, bar_count):
        """Initialization of the SortList class instance"""

        self.root = root
        self.vis_canvas = vis_canvas
        self.bar_count = bar_count
        # DO NOT CHANGE THE NEXT 3 VALUES, OR CODE MAY BREAK (ONLY THE GUI)
        self.list_length = 20
        self.range_first = 1
        self.range_last = 99
        self.bar_list = []
        self.bar_color = []
        # this sets the passed in current speed as self.current_speed
        self.current_speed = current_speed


    def create_new_list(self):
        """create a list of random integers, then add them to 
        bar_list as elements one by one
        
        """

        # starts empty, because I want it to start fresh every time
        self.bar_list = []
        for i in range(0, self.list_length):
            # this loop creates each element by creating a 
            # random int for each element in range of list
            bar_height = random.randint(self.range_first, self.range_last)
            self.bar_list.append(bar_height)

        # set length attribute to new length
        self.list_length = len(self.bar_list) 
        # all bars are grey
        bar_color = ["grey"] * self.list_length  
        # make_bars draws the bars on vis_canvas
        self.make_bars(bar_color)


    def make_bars(self, bar_color):
        """this method actually draws the bars on the canvas (vis_canvas)
        
        Args:
            bar_color(list): list of colors for each bar in the bar_list
        
        """

        # delete all bars (refresh the screen)
        self.vis_canvas.delete("all")
        # local variable "length" is the length of the bar_list attr
        length = len(self.bar_list)
        # this is not the literal width of the canvas, it is essentially 
        # creating padding
        vis_canvas_width = 580
        # make bar method from Norah Wang, altered slightly
        SHAPE_WIDTH = (vis_canvas_width / length)
        SHAPE_GAP = 4.3
        MAX_HEIGHT = 175
        X_OFFSET = 5
        Y_OFFSET = 1
        # local variable to normalize height of bars
        bar_height = [i / max(self.bar_list) for i in self.bar_list]

        # for each index in the range of the list
        for i in range(length):
            # this is a vector relationship to draw rectangles in the GUI
            # we have covered this a lot already
            x1 = i * SHAPE_WIDTH + SHAPE_GAP + X_OFFSET
            y1 = MAX_HEIGHT - bar_height[i] * 150
            x2 = (i + 1) * SHAPE_WIDTH + X_OFFSET
            y2 = MAX_HEIGHT + Y_OFFSET

            # create_rectangle() is what ACTUALLY draws on the screen, 
            # using the former variables as inputs.
            self.vis_canvas.create_rectangle(x1, y1, x2, y2, 
                                             fill=bar_color[i])
            
            # this sets the spacing for the numbers at the bottoms 
            # of the bars
            x_text = (SHAPE_WIDTH) * i + (X_OFFSET * 3.2)
            y_text = MAX_HEIGHT + Y_OFFSET + 7

            # This ACTUALLY draws the numbers onscreen 
            # - should I change the cont? To what?
            self.vis_canvas.create_text(x_text, y_text, 
                                        text=f"{self.bar_list[i]}")
        
        # update refreshes the canvas with the bars onscreen
        self.vis_canvas.update()


    def select_sort(self):
        """ Selection sort method. Contains the aritmetic 
        needed to sort selection-style.
        
        """

        # for each index in that range
        for i in range(len(self.bar_list)):
            # each i is the new min_index
            min_index = i
            # next in the list is what we will compare min_index to
            for j in range(i + 1, len(self.bar_list)):
                # if the min_index is larger than the next bar in the 
                # list, then j is the new min_index
                if self.bar_list[min_index] > self.bar_list[j]:
                    min_index = j
            # This is what actually swaps the bar values
            self.bar_list[i], self.bar_list[min_index] = self.bar_list[
                min_index], self.bar_list[i]
            # this is what draws those values onscreen 
            # by calling the make_bars method
            # also colors the bars.
            self.make_bars(["gold" if x == i else "black" 
                                     if x == min_index else "grey"
                                     for x in range(len(self.bar_list))])
            # update refreshes the screen
            self.root.update()
            # I decided to use time for a delay for two reasons: One is 
            # because the tutor, Connor, thought I should, and because 
            # I was having a lot of trouble using after() while also 
            # asking for information from the slider.
            time.sleep(self.set_speed())


    def bubble_sort(self):
        """Bubbles sort method. Contains the arithmetic needed to 
        sort bubble-style
        
        """

        # start for loop that is using the bar_list attribute
        for i in range(len(self.bar_list)):
            # each index begins as not swapped
            swapped = False
            # moves through list from left index of the unsorted portion, 
            # to the right
            for j in range(len(self.bar_list) - i - 1):
                # if the value at index j is greater than that value, swap
                if self.bar_list[j] >= self.bar_list[j + 1]:
                    self.bar_list[j], self.bar_list[j + 1] = self.bar_list[
                        j + 1], self.bar_list[j]
                    # change swapped to True to eliminate that element 
                    # from the sorting
                    swapped = True
                # update root
                self.root.update()
                # draw bars onscreen
                self.make_bars(["gold" if x <= j else "black" if x == j+1     
                                     else "grey" for x in range(len(
                    self.bar_list))])
                # delay set in set_speed
                time.sleep(self.set_speed())
            # if none are left stop iterating
            if not swapped:
                break


    def merge_sort(self, begin=None, end=None):
        """Merge sort method that has the arithmetic to sort merge-style
        
        Args:
            begin(int): the first index in list
            end(int): last index in list
            mid(int): established inside a conditional using floor division

        """

        # had to include this to initialize because the list begins as None
        if begin is None and end is None:
            begin = 0
            end = self.list_length - 1

        # if the leftmost number is smaller than the rightmost
        if begin < end:
            # midpoint is established
            mid = (begin + end) // 2
            # values are sent to the start again
            self.merge_sort(begin, mid)
            self.merge_sort(mid + 1, end)
            # then values are sent to the next function, merge()
            self.merge(begin, mid, end)


    def merge(self, begin, mid, end):
        """Merge the two lists passed in by merge_sort

        Args:
            begin(int): first index of list
            mid(int): mid point of indeces
            end(int): last index of list

        """

        # etablisht the left and right halves
        left_half = self.bar_list[begin:mid+1]
        right_half = self.bar_list[mid+1:end+1]
        temp_array = []
        # setting both i and j to 0 so they both start from the left side
        i = j = 0

        # while i is not at or past the end of left, 
        # and same with j for right
        while i < len(left_half) and j < len(right_half):
            # if the value at that index is less than 
            # index in right half, append
            if left_half[i] <= right_half[j]:
                temp_array.append(left_half[i])
                i += 1
            # else add it to the right side
            else:
                temp_array.append(right_half[j])
                j += 1

        # this puts the list called left half on the left side
        temp_array.extend(left_half[i:])
        # this extends the list with the right half
        temp_array.extend(right_half[j:])
        # bar_list is set to be temp array
        self.bar_list[begin:end+1] = temp_array

        # set the bar colors during merge sort
        bar_color = ["white" if x >= begin and x < mid else "gold" 
                     if x == mid else "black" if x > mid and x <= end 
                     else "grey" for x in range(len(self.bar_list))]
        # make bars here
        self.make_bars(bar_color)
        self.root.update()\
        # delay
        time.sleep(self.set_speed())


    def get_slider_value(self):
        """get current value of slider"""

        # sets variable num_bars
        num_bars = self.list_length.get()
        return num_bars


    def set_speed(self):
        """Get the selected speed from combobox
        
        Returns: 
            float: duration of delay in seconds
        
        """

        # dictionary that assigns each menu option to a set speed
        speed_menu = {"Dead": 2.0, 
                      "Sluggish": 1.0, 
                      "Slow": 0.5, 
                      "Medium": 0.25, 
                      "Fast": 0.1, 
                      "Hyper": 0.01, 
                      "Ludicrous": 0.0005}
        # this gets the current speed attribute
        selected_speed = self.current_speed.get()
        # returns the respective speed. If speed is not found, 
        # default is 0.25 seconds "medium" 
        return speed_menu.get(selected_speed, 0.25)