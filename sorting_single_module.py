"""sorting_algorithm.py

Richard Sapp

05/26/2023

This is a program to create a list of 20 integers and sort them in 3 ways:
selction sort, merge sort, and bubble sort. Uses tkinter GUI to show the
searches.

"""


# ---------------------------------------------------------------------------------------------------------------------------------------------

# WORKS WITHOUT TIME MODULE

# ---------------------------------------------------------------------------------------------------------------------------------------------


# NOTE Crashes when user tries to interact while running in slow mode
# NOTE Bars slowly move down (number is counting down in selection sort) (would like instant)(selection sort)
# NOTE adjust font size if you have to, to make the numbers stay in center
# NOTE pandas library, matplotlib library

# importing needed/wanted modules
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import random

# initialize main window
root= Tk()
root.title("Parsin' Lists!")
root.tk.call("wm", "iconphoto", root._w, 
             PhotoImage(file= "yellow_tomatoes.png"))
root.geometry("800x600+200+200")
root.anchor("nw")
root.resizable(0,0)

# empty list to begin building list of bar sizes
bar_list = []


# CREATE LIST OF RANDOM INTS
def create_new_list():
    """creates list of 20 integers and sets bar_list as that list"""

    # takes the empty list "bar_list"
    global list_length
    global bar_list

    # SET SIZE OF LIST TO BE SORTED
    list_length = get_slider_value()
    range_first = 1
    range_last = 99

    # sets bar list to empty
    bar_list = []


    # makes the list of bars
    for i in range(0, list_length):
        bar_height = random.randint(range_first, range_last)
        bar_list.append(bar_height)

    # call make_bars to draw the bars on the screen
    make_bars(bar_list, ["grey" for x in range(len(bar_list))])


# DRAW THE BARS
def make_bars(bar_list, bar_color):
    # list_length is imported for mutability of shape width. 
    # if list length is shorter, shape is wider
    global list_length
    # clear bars that are on screen
    vis_canvas.delete("all")
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
        vis_canvas.create_rectangle(x1, y1, x2, y2, fill= bar_color[i])
        
        # text placement under the bars
        x_text = (SHAPE_WIDTH) * i + (X_OFFSET*2)
        y_text = MAX_HEIGHT + Y_OFFSET + 7
        # this is the line that writes the numbers on the vis_canvas
        vis_canvas.create_text(x_text, y_text, text= f"{bar_list[i]}")
    # update_idletasks can be used in tkinter to redraw the widgets without calling callbacks
    # so this updates the values when I call for make_bars later
    root.update_idletasks()
    # return temp_array


# resets the bars to a NEW random list
def jumble_bars():
    vis_canvas.delete("all")
    create_new_list()


# SET THE SPEED
def set_speed():
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

    # this is the part of the function that actually changes the speed using get()
    # these are all the speed option
    # using slow speeds for bubble can cause crash if user interacts during sort
    if speed_menu.get() == "Dead":
        return dead
    if speed_menu.get() == "Sluggish":
        return sluggish
    if speed_menu.get() == "Slow":
        return slow
    if speed_menu.get() == "Medium":
        return medium
    if speed_menu.get() == "Fast":
        return fast
    if speed_menu.get() == "Hyper":
        return hyper
    if speed_menu.get() == "Ludicrous":
        return ludicrous


# Base function for select sort ################################################################# THE BARS AND NUMBERS COUNT DOWN, WANT IT INSTANT
def select_sort():
    """this is the function that handles the selection sort"""

    # delay so we can see what is happening
    DELAY = set_speed()
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
                # is iterated through ########################################################## COLORS ARE WRONG, DO NOT SWAP AND SHOULD SHOW MORE CLEARLY WHAT HAPPENS
                new_bar_list = make_bars(bar_list, ["gold" if x == j else "black" 
                                     if x == j + 1 else "grey"
                                     for x in range(length)])
                # time to use delay
                vis_canvas.after(int(DELAY), new_bar_list)



# Base function for bubble sort
def bubble_sort():
    """this is the function that handles the bubble sort"""

    # using set_speed func to set DELAY
    DELAY = set_speed()
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
                
                new_bar_list = make_bars(bar_list, ["gold" if x <= j else "black" if x == j+1      ############################### FIXED COLORS
                                     else "white" for x in range(length)])
                
                vis_canvas.after(int(DELAY), new_bar_list)


# Merge
def merge_sort(bar_list, begin, mid, end, make_bars):
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
def merge(bar_list, begin, end, make_bars, DELAY):
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
        merge(bar_list, begin, mid, make_bars, DELAY)
        merge(bar_list, mid + 1, end, make_bars, DELAY)

        # combine two halves
        merge_sort(bar_list, begin, mid, end, make_bars)

        # draw bars onscreen as colored 
        new_bar_list = make_bars(bar_list, ["white" if x >= begin and x < mid 
                             else "gold" if x == mid else "black" 
                             if x > mid and x <= end else "grey" 
                             for x in range(len(bar_list))])
        # time.sleep(DELAY)

    # return to grey
        vis_canvas.after(int(DELAY), new_bar_list)


# THESE ARE TEH FUNCTINS CALLED BY BUTTONS!
def merge_sort_activate():
    """function to call the merge_sort function at the click of a button"""
    DELAY = set_speed()
    merge(bar_list, 0, len(bar_list)-1, make_bars, DELAY)


def select_sort_activate():
    """function to call select dort after click"""
    select_sort()
    make_bars(bar_list, ["grey" for x in range(len(bar_list))])


def bubble_sort_activate():
    """function to call bubble_sort on click"""
    bubble_sort()
    make_bars(bar_list, ["grey" for x in range(len(bar_list))])

# function to get value from slider and return that value
def get_slider_value():
    value = bar_count.get()
    return value


# Initializing windows, visual and background
bg_canvas = Canvas(root, width= 796, height= 596, bg= "black")
vis_canvas = Canvas(root, width= 594, height= 200, bg= "darkgoldenrod3")

# adding slider
bar_count = Scale(root, label= "Number of Bars", length= 332, from_= 2, to_= 42, orient= HORIZONTAL, bg= "black", fg= "lightgrey")
bar_count.place(x= 100, y= 355)
bar_count.set(20)

# create StringVar with which I can change speed
current_speed = StringVar()
speed_list = ["Dead", "Sluggish", "Slow", "Medium", "Fast", "Hyper", "Ludicrous"]
# creating label to tel user where the speed menu is, then placing that menu and label
speed_label = Label(bg_canvas, text= "Choose Speed:", bg= "black", fg= "lightgrey", width= 12)
speed_label.place(x= 100, y= 440)
speed_menu = ttk.Combobox(bg_canvas, textvariable= current_speed, 
                          values= speed_list, height= 10, width= 20)########################################################### height of dropdown menu changes, not the visual height. How change color of combobox bg?
speed_menu.place(x= 192, y= 440)
# setting the default choice to medium
speed_menu.current(3)

# initializing the buttons
jumble_button = Button(bg_canvas, text= "JUMBLE", height= 3, width= 15, 
                       font= ("courier", 20, "bold"), command= jumble_bars)
select_sort_button = Button(bg_canvas, text= "SELECTION", height= 1, width= 10, 
                       font= ("courier", 16, "bold"), command= select_sort_activate)
bubble_sort_button = Button(bg_canvas, text= "BUBBLE", height= 1, width= 7, 
                       font= ("courier", 16, "bold"), command= bubble_sort_activate)
merge_sort_button = Button(bg_canvas, text= "MERGE", height= 1, width= 6, 
                       font= ("courier", 16, "bold"), command= merge_sort_activate)

# placing the visual and background windows
bg_canvas.place(x= 0, y= 0)
vis_canvas.place(x= 100, y= 90)

# placing the buttons
jumble_button.place(x= 449, y= 300)
select_sort_button.place(x= 100, y= 300)
bubble_sort_button.place(x= 245, y= 300)
merge_sort_button.place(x= 350, y= 300)


# calling main/ mainloop
if __name__ == "__main__":

    # included this to populate list when user opens the app
    create_new_list()

    root.mainloop()
































