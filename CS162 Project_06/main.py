from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import random

# import make_list
import sort_list
from sort_list import Sort_List
bar_list = []



root = Tk()
root.title("Parsin' Lists!")
# root.call("wm", "iconphoto", root._w, PhotoImage(file= "yellow_tomatoes.png"))
root.geometry("800x600+200+200")
# root.anchor("nw")
root.resizable(0,0)

bg_canvas = Canvas(root, width= 796, height= 596, bg= "black")
# placing the background windows
bg_canvas.place(x= 0, y= 0)


# create StringVar with which I can change speed
current_speed = StringVar()
# speed_list = ["Dead", "Sluggish", "Slow", "Medium", "Fast", "Hyper", "Ludicrous"]
speed_list = ["Slow", "Medium", "Fast", "Hyper", "Ludicrous"]
# creating label to tel user where the speed menu is, then placing that menu and label
speed_label = Label(bg_canvas, text= "Choose Speed:", bg= "black", fg= "lightgrey", width= 12)
speed_label.place(x= 100, y= 440)


# I TRIED MOVING THE FOLLOWING LINES TO SORT TO TRY AND AVOID CIRCULAR IMPORT
# speed_menu = ttk.Combobox(bg_canvas, textvariable= current_speed, 
#                         values= speed_list, height= 10, width= 20)########################################################### height of dropdown menu changes, not the visual height. How change color of combobox bg?
# speed_menu.place(x= 192, y= 440)
# # setting the default choice to medium
# speed_menu.current(3)





        # THESE ARE TEH FUNCTINS CALLED BY BUTTONS!
def merge_sort_activate():
    """function to call the merge_sort function at the click of a button"""
    DELAY = Sort_List.set_speed()
    Sort_List.merge(bar_list, 0, len(bar_list)-1, Sort_List.make_bars, DELAY)


def select_sort_activate():
    """function to call select dort after click"""
    # print(bar_list)
    Sort_List.select_sort()
    Sort_List.make_bars(bar_list, ["grey" for x in range(len(bar_list))])


def bubble_sort_activate():
    """function to call bubble_sort on click"""
    Sort_List.bubble_sort()
    Sort_List.make_bars(bar_list, ["grey" for x in range(len(bar_list))])

# function to get value from slider and return that value
def get_slider_value():
    value = Sort_List.bar_count.get()
    return value

def jumble_bars():
    Sort_List.create_new_list()




# adding slider
bar_count = Scale(root, label= "Number of Bars", length= 332, from_= 2, to_= 42, orient= HORIZONTAL, bg= "black", fg= "lightgrey")
bar_count.place(x= 100, y= 355)
bar_count.set(20)



# initializing the buttons
jumble_button = Button(bg_canvas, text= "JUMBLE", height= 3, width= 15, 
                    font= ("courier", 20, "bold"), command= jumble_bars)
select_sort_button = Button(bg_canvas, text= "SELECTION", height= 1, width= 10, 
                    font= ("courier", 16, "bold"), command= select_sort_activate)
bubble_sort_button = Button(bg_canvas, text= "BUBBLE", height= 1, width= 7, 
                    font= ("courier", 16, "bold"), command= bubble_sort_activate)
merge_sort_button = Button(bg_canvas, text= "MERGE", height= 1, width= 6, 
                    font= ("courier", 16, "bold"), command= merge_sort_activate)
    

    # initializing the buttons
jumble_button = Button(bg_canvas, text= "JUMBLE", height= 3, width= 15, 
                    font= ("courier", 20, "bold"))
select_sort_button = Button(bg_canvas, text= "SELECTION", height= 1, width= 10, 
                    font= ("courier", 16, "bold"))
bubble_sort_button = Button(bg_canvas, text= "BUBBLE", height= 1, width= 7, 
                    font= ("courier", 16, "bold"))
merge_sort_button = Button(bg_canvas, text= "MERGE", height= 1, width= 6, 
                    font= ("courier", 16, "bold"))



# placing the buttons
jumble_button.place(x= 449, y= 300)
select_sort_button.place(x= 100, y= 300)
bubble_sort_button.place(x= 245, y= 300)
merge_sort_button.place(x= 350, y= 300)


# make_list.create_new_list()
# 
Sort_List.__init__(Sort_List.create_new_list, root) ##################################################### we are onto something here
# Sort_List.make_bars(root, Sort_List.create_new_list, "grey")#(Sort_List.create_new_list, root, Sort_List.make_bars)
# Sort_List.create_new_list()
root.mainloop()




# CALLING MAIN THIS WAY MAKES TWO WINDOWS OPEN
# if __name__ == "__main__":

#     # included this to populate list when user opens the app
#     Sort_List.create_new_list

#     root.mainloop()
