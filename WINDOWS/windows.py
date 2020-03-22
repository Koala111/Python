
# coding: utf-8

# In[13]:


import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable = var, bg = 'green', 
             font = ('Arial', 12), width = 15, height = 2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
    
    
b = tk.Button(window, text = 'hit me', width = 15, height = 2,
             command = hit_me)
b.pack()
window.mainloop()


# In[18]:


import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

e = tk.Entry(window, show = None)
e.pack()
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)
    
b1 = tk.Button(window, text = 'insert point', width = 15, height = 2,
             command = insert_point)
b1.pack()

b2 = tk.Button(window, text = 'insert end', command = insert_end)
b2.pack()
t = tk.Text(window, height = 2)
t.pack()

window.mainloop()


# In[22]:


# 列表
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

var1 = tk.StringVar()

l = tk.Label(window, bg = 'yellow', width = 4, textvariable = var1)
l.pack()
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

    
b1 = tk.Button(window, text = 'print selection', width = 15, height = 2,
             command = print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,3,44))
lb = tk.Listbox(window, listvariable = var2)
list_items = [1,23,23,243]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()


window.mainloop()


# In[33]:


# radiobutton 单选
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

var = tk.StringVar()

l = tk.Label(window, bg = 'red', width = 50, text = 'empty')
l.pack()

def print_selection():
    l.config(text = 'you have selected:' + var.get())
    
r1 = tk.Radiobutton(window, text = 'Option A', variable = var, 
                   value = 'A', command = print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text = 'Option B', variable = var, 
                   value = 'B', command = print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text = 'Option C', variable = var, 
                   value = 'C', command = print_selection)
r3.pack()

window.mainloop()


# In[35]:


# scole
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

l = tk.Label(window, bg = 'red', width = 50, text = '0')
l.pack()

def print_selection(v):
    l.config(text = 'you have selected:' + v)
    
s = tk.Scale(window, label = 'try me', from_ = 5, to = 11, 
             orient = tk.HORIZONTAL, length = 200, showvalue = 0,
             tickinterval = 3, resolution = 0.01, 
             command = print_selection)
s.pack()

window.mainloop()


# In[36]:


# 复选按钮
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

l = tk.Label(window, bg = 'red', width = 50, text = 'empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text = 'Python', variable = var1, 
                    onvalue = 1, offvalue = 0, command = print_selection)
c2 = tk.Checkbutton(window, text = 'C++', variable = var2, 
                    onvalue = 1, offvalue = 0, command = print_selection)
c1.pack()
c2.pack()
window.mainloop()


# In[43]:


# 画布
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

canvas = tk.Canvas(window, bg = 'blue', height = 100, width = 200)


image_file = tk.PhotoImage(file='C:\\ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image = image_file)

line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形

def move_it():
    canvas.move(rect, 0, 2)
    
canvas.pack()
b = tk.Button(window, text = 'move', command = move_it)

window.mainloop()


# In[1]:


import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

l = tk.Label(window, text = '', bg = 'yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text = 'Do' +str(counter))
    counter += 1
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New', command = do_job)
filemenu.add_command(label = 'Open', command = do_job)
filemenu.add_command(label = 'Save', command = do_job)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = window.quit)

editmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Cut', command = do_job)
editmenu.add_command(label = 'Copy', command = do_job)
editmenu.add_command(label = 'Parse', command = do_job)

submenu = tk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`

window.config(menu = menubar)
window.mainloop()


# In[1]:


# Frame
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

###定义一个`label`显示`on the window`
tk.Label(window, text='on the window').pack()

###在`window`上创建一个`frame`
frm = tk.Frame(window)
frm.pack()

###在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`

frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)

###这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
frm_l.pack(side='left')
frm_r.pack(side='right')

###这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
tk.Label(frm_l, text='on the frm_l1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
tk.Label(frm_l, text='on the frm_l2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
tk.Label(frm_r, text='on the frm_r1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`

window.mainloop()


# In[6]:


# 弹窗
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='',message='')#提示信息对话窗
#     tk.messagebox.showwarning()#提出警告对话窗
#     tk.messagebox.showerror()#提出错误对话窗
#     tk.messagebox.askquestion()#询问选择对话窗

    
tk.Button(window, text = 'hit me', command = hit_me).pack()

window.mainloop()


# In[14]:


# 放置部件
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

# method 1
'''
tk.Label(window, text='1').pack(side='top')#上
tk.Label(window, text='1').pack(side='bottom')#下
tk.Label(window, text='1').pack(side='left')#左
tk.Label(window, text='1').pack(side='right')#右



# method 2
for i in range(4):
    for j in range(4):
        tk.Label(window, text = 1).grid(row = i, column = j,
                                       padx=10, pady=10 )
''' 
# method3
tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()


# In[24]:


# login example


import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='c:/ins.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                               'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()

