"""This is the main module to call all the functions when the user 
wants them called

Richard Sapp
05/30/2023

This initializes the window and the canvases and the buttons and 
the sliders and the combobox

"""

# import modules
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from sort_list import SortList



def jumble_bars():
    """function to jumble the bars onscreen"""

    vis_canvas.delete("all")
    sort_list.create_new_list()
    sort_list.make_bars(["grey" for x in range(len(sort_list.bar_list))])
    sort_list.set_speed()


def select_sort_activate():
    """function to select sort the bars on button click"""

    sort_list.select_sort()
    sort_list.make_bars(["grey" for x in range(len(sort_list.bar_list))])


def bubble_sort_activate():
    """function to bubble sort the bars on button click"""

    sort_list.bubble_sort()
    sort_list.make_bars(["grey" for x in range(len(sort_list.bar_list))])


def merge_sort_activate():
    """function to merge sort on button click"""

    sort_list.merge_sort()
    sort_list.make_bars(["grey" for x in range(len(sort_list.bar_list))])

def get_slider_value(event):
    """function to interpret slider value and make it into the list length 
    in sort_list"""

    sort_list.list_length = bar_count.get()
    # sort_list.create_new_list() # this line allows the slider to change 
    # # number of bars instantly. I don't think I like it.


# initializing window with two canvases
root = Tk()
root.title("Parsin' Lists")
root.geometry("800x600+200+200")
root.tk.call("wm", "iconphoto", root._w, 
             PhotoImage(file="yellow_tomatoes.png"))
root.anchor("nw")
root.resizable(0, 0)

# stringvar that is connected to speed_menu combobox
current_speed = StringVar()
# list of string options
speed_list = ["Dead", 
              "Sluggish", 
              "Slow", 
              "Medium", 
              "Fast", 
              "Hyper", 
              "Ludicrous"]

# two canvases. BG is the black background, vis_canvas is the orage foreground
bg_canvas = Canvas(root, width=796, height=596, bg="black")
vis_canvas = Canvas(root, width=594, height=200, bg="darkgoldenrod3")

# initializing the combobox and label for the speed shoice dropdown menu
speed_label = Label(bg_canvas, text="Choose Speed:", bg="black", 
                    fg="lightgrey", width=12)
speed_label.place(x=95, y=435)
speed_menu = ttk.Combobox(bg_canvas, textvariable=current_speed, 
                          values=speed_list, height=10, width=20)
speed_menu.place(x=190, y=435)
# default speed at index 3
speed_menu.current(3)

# slider that controls bar count
bar_count = Scale(root, label="Number of Bars",font=13, width=25, 
                  length=332, from_=2, to_=42, orient=HORIZONTAL, 
                  bg="black", fg="lightgrey")
bar_count.place(x=100, y=350)
# default 20 bars
bar_count.set(20)
# buttonrelease is the event that allows the get_slider_value to 
# update instantly
bar_count.bind("<ButtonRelease>", get_slider_value)

# initializing the buttons
jumble_button = Button(bg_canvas, text="JUMBLE", height=2, 
                       width=10, font=("courier", 30, "bold"), 
                       command=jumble_bars)
select_sort_button = Button(bg_canvas, text="SELECTION", height=1, 
                            width=10, font=("courier", 16, "bold"), 
                            command=select_sort_activate)
bubble_sort_button = Button(bg_canvas, text="BUBBLE", height=1, 
                            width=7, font=("courier", 16, "bold"), 
                            command=bubble_sort_activate)
merge_sort_button = Button(bg_canvas, text="MERGE", height=1, 
                           width=6, font=("courier", 16, "bold"), 
                           command=merge_sort_activate)

# placing canvases
bg_canvas.place(x=0, y=0)
vis_canvas.place(x=100, y=90)

# placing buttons
jumble_button.place(x=448, y=300)
select_sort_button.place(x=100, y=300)
bubble_sort_button.place(x=245, y=300)
merge_sort_button.place(x=350, y=300)

# call main
if __name__ == "__main__":
    # instance of SortList class
    sort_list = SortList(root, vis_canvas, current_speed, bar_count)
    # new list to begin the whole process
    sort_list.create_new_list()
    # mainloop
    root.mainloop()
