import os
import shutil
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askdirectory



def is_image(path):
    ext = path.split('.')
    if ext[-1] in ['jpg','JPEG','png']:
        return True
    return False

def get_img_path():
    dir = lbl_image_dir_name['text']
    imgs = iter(os.listdir(dir))
    while True:
        img = next(imgs)
        if is_image(img):
            if dir == os.getcwd():
                return str(img)
            return dir+'/'+img
    return None
    
    
def get_img():
    path = get_img_path()
    try:
        img = ImageTk.PhotoImage(Image.open(path).resize([600,500],Image.ANTIALIAS))
    except Exception as e:
        print("exception excuted")
        img = ImageTk.PhotoImage(Image.open('default.png').resize([600,500],Image.ANTIALIAS))
    return img

def set_lbl_image():
    img = get_img()
    lbl_image.configure(image = img)
    lbl_image.image = img


def open_img_dir():
    dir = askdirectory()
    lbl_image_dir_name['text'] = dir
    set_lbl_image()


def open_main_dir():
    dir = askdirectory()
    lbl_main_dir_name['text'] = dir

global p
p=0
def create_dir():
    global p
    base = lbl_main_dir_name['text']
    dir_name = ent_dir_name.get()
    if dir_name:
        dir=base+'/'+dir_name
        try:
            os.mkdir(dir)
        except Exception as e :
            print(e)
            
    else:
        print('please enter dir name')
        return
    
    btn_move_to_dir = tk.Button(master=frm_dirs, text= 'Move to '+dir_name,
                                command= lambda m=dir_name: move_image( get_img_path(),m))
    btn_move_to_dir.grid(row=5+p,column=0,sticky='ew',padx=5,pady=5)
    p+=1

def move_image(image, dir):
    print(image,dir)
    try:
        shutil.copy(image,dir)
        shutil.move(image, 'extra')
    except Exception as e:
        os.remove(image)
        print(e)
    set_lbl_image()
    
    

fg ='white'
bg ='black'
window = tk.Tk()
window.title('Dataset Generator')

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800, weight=1)

frm_image = tk.Frame(master=window ,relief=tk.RAISED,bd=2, padx=5,pady=5)

lbl_image_name = tk.Label(master= frm_image, text='image name',bg=bg,fg=fg)
lbl_image_name.grid(row=0,column=0,sticky='ew',padx=5,pady=5)

lbl_image_dir_name = tk.Label(master= frm_image, text=os.getcwd())
lbl_image_dir_name.grid(row=1,column=0,sticky='ew',padx=5,pady=5)

btn_select_img_dir = tk.Button(master=frm_image, text= 'select images directory', command= open_img_dir)
btn_select_img_dir.grid(row=2,column=0,sticky='ew',padx=5,pady=5)

img = ImageTk.PhotoImage(Image.open('default.png').resize([600,500],Image.ANTIALIAS))
lbl_image = tk.Label(master=frm_image, image = img,width=600,height=500)
lbl_image.grid(row=3 , column=0,sticky='nsew',padx=5,pady=5)






# def handle_keypress(event):
#     if event.keysym == tk.RIGHT:
#         pass 
#     if event.keysym == tk.LEFT:
#         pass

# try:   
#     img = ImageTk.PhotoImage(Image.open(get_image()).resize([600,500]))
# except :
#     img = ImageTk.PhotoImage(Image.open('default.png'))

# Create a Label Widget to display the text or Image

# Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)





frm_dirs = tk.Frame(master=window ,relief=tk.RAISED, bd=2, padx=5,pady=5)

lbl_dirs = tk.Label(master=frm_dirs, text='click on directory to insert the image',bg=bg,fg=fg)
lbl_dirs.grid(row=0,column=0,sticky='ew', padx=5, pady=5)

lbl_main_dir_name = tk.Label(master= frm_dirs, text=os.getcwd())
lbl_main_dir_name.grid(row=1,column=0,sticky='ew',padx=5,pady=5)

btn_create_dir = tk.Button(master=frm_dirs, text= 'select main directory', command= open_main_dir)
btn_create_dir.grid(row=2,column=0,sticky='ew',padx=5,pady=5)


ent_dir_name = tk.Entry(master=frm_dirs)
ent_dir_name.grid(row=3,column=0,sticky='ew',padx=5,pady=5)

btn_create_dir = tk.Button(master=frm_dirs, text= 'Create dirs', command=create_dir)
btn_create_dir.grid(row=4,column=0,sticky='ew',padx=5,pady=5)

# def create_move_to_dir_btn():   
#     for i, dir in enumerate(os.listdir(lbl_main_dir_name['text'])):
#         if os.path.isdir(dir):
#             btn_move_to_dir = tk.Button(master=frm_dirs, text= 'Move to '+dir,command= lambda m=dir: move_image( get_img_path(),m))
#             btn_move_to_dir.grid(row=5+i,column=0,sticky='ew',padx=5,pady=5)




frm_dirs.grid(row=0, column=0,sticky='nsew')
frm_image.grid(row=0, column=1,sticky='nsew')
# frm_image.pack(fill=tk.BOTH,side=tk.LEFT, padx=30,expand=True)
# frm_dirs.pack(fill=tk.BOTH, side=tk.LEFT, padx=30)

window.mainloop()






