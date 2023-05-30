# Sorting List Class

## 1. self.bar_list

### line 124 - selection_sort(self)

```

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

```

Good : DELAY = self.set_speed() 
I recommend using self more, using variable and methods insize of the object is much easier

(Could DELAY be someting that is a variable inside of this class? If it is only ever called here then yes)

Change : length = len(bar_list)
The function does not have an input of bar_list, it does not have any mention of it. This function
as no view outsite of itself so it has no clue what you are talking about here. I recommend initializing
a self.bar_list, so you can pass bar_list between functions easier, otherwise you need an input here.

### line 151

### line 172 - Merge sort has bar_list

## 2. set_speed

### variables?

```
# seven DELAY options
dead = 10000
sluggish = 750
slow = 500
medium = 250
fast = 100
hyper = 50
ludicrous = 1
```

Currently does nothing, I believe you intend to change this later on, you could have a self.delay variable that is
known to other functions, and check to see if changes have happened in other functions.

## 3. making bars

### global list_length

```
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
```

"global list_length"

In creating functions inside of classes, you either want them to directly change things in the class
such as setting the variable self.hearts = 2 rather than self.hearts = 3, or the function will return 
a value after making calculations for that value such as return self.x - input_variable. When creating these 
global variables, keep in mind that you're inside of a class right now, when creating a global variable it has to 
be unique and may create further complications. I believe right now you have your sort_alogrithm object instance 
and now you're calling a functions that will create an entirely new variable in the file you created this object in. 
I believe you would rather have a temporary variable of list_length or have a global variable only to the class which 
is similar to how a variable self.list_length would behave.

### self variables

"vis_canvas_width = 580"

Make sure that you call self when using variables that are designed in the object's scope. You have no 
variables passed in that are vis_canvas_width. SCOPE is a very important concept to master when using class's.

## 4. temporary variables

```
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
```

You're globals have the same issues as above. Make sure you understand that every single variable created inside
of this function is temporary unless you either return or create a self.variable_name for it. 
