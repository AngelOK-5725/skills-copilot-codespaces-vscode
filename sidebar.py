from tkinter import *
from PIL import Image, ImageTk

SIDE_BAR_COLOR = 'green'

window = Tk()
window.minsize(500, 600)
# --------f----------------------------------------------
def swicht_ind(ind, frame):
    ind_home.config(bg= SIDE_BAR_COLOR)
    ind_product.config(bg= SIDE_BAR_COLOR)
    ind_setting.config(bg= SIDE_BAR_COLOR)

    ind.config(bg= 'white')
    frame()

def max_animi():
    current_width = side_bar.winfo_width()
    if current_width < 200:
        current_width += 10
        side_bar.config(width= current_width)
        window.after(ms= 10, func = max_animi)

def mini_animi():
    current_width = side_bar.winfo_width()
    if current_width != 50:
        current_width -= 10
        side_bar.config(width= current_width)
        window.after(ms= 10,func= mini_animi)
def max_side():
    max_animi()
    side_bar.config(width= 200)
    menu_button.config(image= i_close)
    menu_button.config(command= mini_side)

    

def mini_side():
    mini_animi()
    side_bar.config(width= 50)
    menu_button.config(image= i_menu)
    menu_button.config(command= max_side)


# ------------------------------------------------------
img_menu = Image.open('./tkinder_apps/sidebar_project/menu.png')
img_menu = img_menu.resize((40, 30), Image.BICUBIC)
i_menu = ImageTk.PhotoImage(img_menu)


img_home = Image.open('./tkinder_apps/sidebar_project/home.png')
img_home = img_home.resize((40, 30), Image.BICUBIC)
i_home = ImageTk.PhotoImage(img_home)


img_product = Image.open('./tkinder_apps/sidebar_project/product.png')
img_product = img_product.resize((35, 30), Image.BICUBIC)
i_product = ImageTk.PhotoImage(img_product)


img_setting = Image.open('./tkinder_apps/sidebar_project/setting.png')
img_setting = img_setting.resize((35, 30), Image.BICUBIC)
i_setting = ImageTk.PhotoImage(img_setting)


img_close = Image.open('./tkinder_apps/sidebar_project/close.png')
img_close = img_close.resize((30, 30), Image.BICUBIC)
i_close = ImageTk.PhotoImage(img_close)
# ------------------------------------------------------
def home_page():
    home_frame = Frame(full_frame)
    home_frame.place(relheight= 1.0, relwidth= 1.0, x= 50)

    text_b = Label(home_frame, text= 'Home page', font=('Bold', 20))
    text_b.place(x= 0, y= 200)

def product_page():
    product_frame = Frame(full_frame)
    product_frame.place(relheight= 1.0, relwidth= 1.0, x= 50)

    text_b = Label(product_frame, text= 'Product page', font=('Bold', 20))
    text_b.place(x= 0, y= 200)

def setting_page():
    setting_frame = Frame(full_frame)
    setting_frame.place(relheight= 1.0, relwidth= 1.0, x= 50)

    text_b = Label(setting_frame, text= 'Setting page', font=('Bold', 20))
    text_b.place(x= 0, y= 200)

# ------------------------------------------------------
full_frame = Frame(window)
full_frame.place(relheight= 1.0, relwidth= 1.0, x= 50)



# ------------------------------------------------------
side_bar = Frame(window, bg= SIDE_BAR_COLOR, width= 50)
side_bar.pack(side= LEFT, fill= Y, padx= 5, pady= 5)

# -----------Buttons-------------------------------------------
menu_button = Button(side_bar, image=i_menu, bg=SIDE_BAR_COLOR,
                     bd=0, activebackground=SIDE_BAR_COLOR, command= max_side)
menu_button.place(x= 4, y= 10)

home_button = Button(side_bar, image=i_home, bg=SIDE_BAR_COLOR,
                     bd=0, activebackground=SIDE_BAR_COLOR, command=lambda: swicht_ind(ind_home, home_page))
home_button.place(x= 4, y= 100)

product_button = Button(side_bar, image=i_product, bg=SIDE_BAR_COLOR,
                        bd=0, activebackground=SIDE_BAR_COLOR, command=lambda: swicht_ind(ind_product, product_page))
product_button.place(x= 4, y= 150)

setting_button = Button(side_bar, image=i_setting, bg=SIDE_BAR_COLOR,
                        bd=0, activebackground=SIDE_BAR_COLOR, command=lambda: swicht_ind(ind_setting, setting_page))
setting_button.place(x= 4, y= 200)

close_button = Button(side_bar, image=i_close, bg=SIDE_BAR_COLOR,
                      bd=0, activebackground=SIDE_BAR_COLOR, command=lambda: print('close'))
# --------indicators of Buttons----------------------------------------------

ind_home = Label(side_bar, bg= 'white')
ind_home.place(x= 1, y= 100, width=2, height= 30)

ind_product = Label(side_bar, bg= SIDE_BAR_COLOR)
ind_product.place(x= 1, y= 150, width=2, height= 30)

ind_setting = Label(side_bar, bg= SIDE_BAR_COLOR)
ind_setting.place(x= 1, y= 200, width=2, height= 30)

# -----------label-------------------------------------------
home_label = Label(side_bar,text= 'Home Page', bg = SIDE_BAR_COLOR, font=('Bold', 16), fg= 'white')
home_label.place(x= 50, y= 100)
home_label.bind('<Button-1>', lambda e: swicht_ind(ind= ind_home))

product_label = Label(side_bar,text= 'Product', bg = SIDE_BAR_COLOR, font=('Bold', 16), fg= 'white')
product_label.place(x= 50, y= 150)
product_label.bind('<Button-1>', lambda e: swicht_ind(ind= ind_product))


setting_label = Label(side_bar,text= 'Setting', bg = SIDE_BAR_COLOR, font=('Bold', 16), fg= 'white')
setting_label.place(x= 50, y= 200)
setting_label.bind('<Button-1>', lambda e: swicht_ind(ind= ind_setting))


# ------------------------------------------------------
window.mainloop()