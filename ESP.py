from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image



file_name='source.txt' #enter file name
hhh = 0 #used as a flag to call the right map
flag = 1


def maps(): #overlapping images but calling the right one on the top most
    if hhh == 1:
        window = Toplevel()
        window.title("Sheeshum Region")
        window.geometry("470x310")
        img1 = ImageTk.PhotoImage(Image.open("Alpine.jpeg"))
        img2 = ImageTk.PhotoImage(Image.open("Babul.jpeg"))
        img3 = ImageTk.PhotoImage(Image.open("Sheeshum.jpeg"))
        label1 = Label(window, image = img1)
        label2 = Label(window, image = img2)
        label3 = Label(window, image = img3)
        label1.place(x=0,y=0)
        label2.place(x=0,y=0)
        label3.place(x=0,y=0)
        messagebox.showinfo("Sheeshum Area","Sheeshum Area is shaded.It is between Matta and Totano Bandai and closer to Matta")
        window.mainloop()

    if hhh == 2:
        window = Toplevel()
        window.title("Babul Region")
        window.geometry("470x310")
        img1 = ImageTk.PhotoImage(Image.open("Alpine.jpeg"))
        img2 = ImageTk.PhotoImage(Image.open("Sheeshum.jpeg"))
        img3 = ImageTk.PhotoImage(Image.open("Babul.jpeg"))
        label1 = Label(window, image = img1)
        label2 = Label(window, image = img2)
        label3 = Label(window, image = img3)
        label1.place(x=0,y=0)
        label2.place(x=0,y=0)
        label3.place(x=0,y=0)
        messagebox.showinfo("Babul Area","Babul Area is between Peuchar Valley and Asharay")
        window.mainloop()

    if hhh == 3:
        window = Toplevel()
        window.title("Alpine Region")
        window.geometry("470x310")
        img1 = ImageTk.PhotoImage(Image.open("Sheeshum.jpeg"))
        img2 = ImageTk.PhotoImage(Image.open("Babul.jpeg"))
        img3 = ImageTk.PhotoImage(Image.open("Alpine.jpeg"))
        label1 = Label(window, image = img1)
        label2 = Label(window, image = img2)
        label3 = Label(window, image = img3)
        label1.place(x=0,y=0)
        label2.place(x=0,y=0)
        label3.place(x=0,y=0)
        messagebox.showinfo("Alpine Area","The Alpine region is in between Matta and Asharay but on the other side")
        window.mainloop()



def alpine(): #function to check number of trees cut and authorize how many trees to cut
    global hhh
    hhh = 3

    window_a=Toplevel()
    window_a.title('ALPINE')
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window_a, image = photo)
    label2.place(x=0,y=0)
    label1=Label(window_a,text="How many trees you want to cut?")
    label1.pack()
    entry1=Entry(window_a) #number of trees logger wants to cut
    entry1.pack()
    def get():
        text1=entry1.get()

        f=open('Alpine.txt','r') #file containg info about no. of trees
        lines=f.readlines()
        lines = "".join(map(str, lines))
        a = 2000000 #initial number of trees
        f.close()
        # lines[0] = total number of trees 
        
        y=int(lines)-int(text1)#no. of trees remaining
        x = int(lines) - 0.7*a #authorized to leave at least 70% trees


        if ((y/a)>=0.7): #tree percent > 70  
            file=open('Alpine.txt','w')
            y = str(y)
            file.writelines(y)
            file.close()
            window_a.destroy()
            maps()

            


        else: #if trees getting cut are less than 70%
            window=Tk()
            label1=Label(window,text="You are allowed to cut not more than {} number of trees".format(x))
            label1.grid(column=1, row=1)
        
        
    
    button1 = Button(window_a, text = "OK" , command = get)
    button1.pack()


def babul(): #function to check number of trees cut and authorize how many trees to cut
    global hhh
    hhh = 2

    window_b=Toplevel()
    window_b.title('BABUL')
    picture = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window_b, image = picture)
    label2.place(x=0,y=0)
    label1=Label(window_b,text="How many trees you want to cut?")
    label1.pack()
    entry1=Entry(window_b) #number of trees logger wants to cut
    entry1.pack()
    def get():
        text1=entry1.get()


        f=open('Babul.txt','r') #file containg info about no. of trees
        lines=f.readlines()
        lines = "".join(map(str, lines))
        a = 30000000 #initial number of trees
        f.close()
        # lines[0] = total number of trees 
        
        y=int(lines)-int(text1)#no. of trees remaining
        x = int(lines) - 0.7*a #authorized to leave at least 70% trees


        if ((y/a)>=0.7): #tree percent > 70  
            file=open('Babul.txt','w')
            y = str(y)
            file.writelines(y)
            file.close()
            window_b.destroy()
            maps()
            

        else:
            window=Tk()
            label1=Label(window,text="You are allowed to cut not more than {} number of trees".format(x))
            label1.grid(column=1, row=1)
        
        
    
    button1 = Button(window_b, text = "OK" , command = get)
    button1.pack()


def sheeshum(): #function to check number of trees cut and authorize how many trees to cut
    global hhh
    hhh = 1

    window_s=Toplevel()
    window_s.title('SHEESHUM')
    picture = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window_s, image = picture)
    label2.place(x=0,y=0)
    label1=Label(window_s,text="How many trees you want to cut?")
    label1.pack()
    entry1=Entry(window_s) #number of trees logger wants to cut
    entry1.pack()
    def get():
        text1=entry1.get()

        f=open('Sheeshum.txt','r') #file containg info about no. of trees
        lines=f.readlines()
        lines = "".join(map(str, lines))
        a = 40000000 #initial number of trees
        f.close()
        # lines[0] = total number of trees 
        
        y=int(lines)-int(text1)#no. of trees remaining
        x = int(lines) - 0.7*a #authorized to leave at least 70% trees

        if ((y/a)>=0.7): #tree percent > 70  
            file=open('Sheeshum.txt','w')
            y = str(y)
            file.writelines(y)
            file.close()

            window_s.destroy()
            maps()
            

            

        else:
            window=Tk()
            label1=Label(window,text="You are allowed to cut not more than {} number of trees".format(x))
            label1.grid(column=1, row=1)
        
        
    
    button1 = Button(window_s, text = "OK" , command = get)
    button1.pack()

def tree_select():#function to select type of tree to be cut
    window=Tk()
    window.title('Team Trees')
    window.geometry('350x100')
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = ttk.Label(window, image = photo)
    label2.place(x=0,y=0)
    label1=ttk.Label(window,text="What type of trees you want to cut?",background="Lavender")
    label1.grid(column=1, row=1)

    button1=Button(window,text="Alpine",command=alpine)#enter command
    button1.config(fg='white',bg='green4')
    button1.place(x=20,y=40,width=80)

    button2=Button(window,text="Babul",command=babul)#enter command
    button2.config(fg='white',bg='Olivedrab4')
    button2.place(x=100,y=40,width=80)

    button3=Button(window,text="Sheeshum",command=sheeshum)#enter command
    button3.config(fg='white',bg='Olivedrab2')
    button3.place(x=180,y=40,width=80)

    window.mainloop()




def replantalpine(): #function if trees have been replanted
    window = Toplevel()
    window.title("Alpine Trees Replaned")
    window.geometry("200x200")
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window, image = photo)
    label2.place(x=0,y=0)
    label1 = Label(window, text="Number of trees replanted")
    label1.pack()
    entry1 = Entry(window)
    entry1.pack()
    
    def replant_alpine(): #the command function
        file = open("Alpine.txt","r")
        lines = file.readlines()
        file.close()
        lines = "".join(map(str, lines))
        text = entry1.get()
        def replace():
            nonlocal text
            nonlocal lines
            new_trees = int(text) + int(lines)
            new_trees = str(new_trees)
            file1 = open("Alpine.txt","w")
            file1.write(new_trees)
            file1.close()
        replace()
        window.destroy()
    button1 = Button(window, text="OK",command = replant_alpine)
    button1.pack()
    window.mainloop


def replantbabul(): #function if trees have been replanted
    window = Toplevel()
    window.title("Babul Trees Replaned")
    window.geometry("200x200")
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window, image = photo)
    label2.place(x=0,y=0)
    label1 = Label(window, text="Number of trees replanted")
    label1.pack()
    def replant_babul(): #the comand function 
        file = open("Babul.txt","r")
        lines = file.readlines()
        file.close()
        lines = "".join(map(str, lines))
        text = entry1.get()
        def replace():
            nonlocal text
            nonlocal lines
            new_trees = int(text) + int(lines)
            new_trees = str(new_trees)
            file1 = open("Babul.txt","w")
            file1.write(new_trees)
            file1.close()
        replace()
        window.destroy()
    entry1 = Entry(window)
    entry1.pack()
    button1 = Button(window, text="OK",command = replant_babul)
    button1.pack()



def replantsheeshum(): #function if trees have been replanted
    window = Toplevel()
    window.title("Sheeshum Trees Replaned")
    window.geometry("200x200")
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window, image = photo)
    label2.place(x=0,y=0)
    label1 = Label(window, text="Number of trees replanted")
    label1.pack()
    def replant_sheeshum(): #the command function
        file = open("Sheeshum.txt","r")
        lines = file.readlines()
        file.close()
        lines = "".join(map(str, lines))
        text1 = entry1.get()
        def replace():
            nonlocal text1
            nonlocal lines
            new_trees = int(text1) + int(lines)
            new_trees = str(new_trees)
            file1 = open("Sheeshum.txt","w")
            file1.write(new_trees)
            file1.close()
        replace()
        window.destroy()
    entry1 = Entry(window)
    entry1.pack()
    button1 = Button(window, text="OK",command = replant_sheeshum)
    button1.pack()
    window.mainloop

def tree_select1(): #function of window in which the user tells which type has been replanted
    window=Toplevel()
    window.title('Trees Replanted')
    window.geometry('350x100')
    photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
    label2 = Label(window, image = photo)
    label2.place(x=0,y=0)
    label1=Label(window,text="What type of trees you just replanted?")
    label1.grid(column=1, row=1)

    button1=Button(window,text="Alpine",command=replantalpine)#enter command
    button1.config(fg='white',bg='green4')
    button1.place(x=20,y=40,width=80)

    button2=Button(window,text="Babul",command=replantbabul)#enter command
    button2.config(fg='white',bg='Olivedrab4')
    button2.place(x=100,y=40,width=80)

    button3=Button(window,text="Sheeshum",command=replantsheeshum)#enter command
    button3.config(fg='white',bg='Olivedrab2')
    button3.place(x=180,y=40,width=80)

    window.mainloop()
    
def search(text): #function to search if logger is liscenced
    f=open(file_name,'r')
    l=f.readlines()
    f.close()
    global flag


    if text+"\n" in l:
        window.destroy()
        tree_select()#add function name of window for further procedure
    else:
        messagebox.showinfo("Wrong Registration Number","Please Enter Registartion Number Again")
    return flag

def add(r):# to append liscence number to a file
    f=open(file_name,'a')
    f.writelines(r+'\n')#adding newly issued lisc number in database
    f.close()


def lisc_no(): #to generate a  liscence number
    f=open(file_name,'r')
    lines=f.readlines()
    f.close()
    number=len(lines)
    lisc_number=str(1000000+number)
    add(lisc_number)
    return lisc_number
    

def signupwindow(): #open window in which liscence number is regenerated
    window2=Toplevel()
    window2.title("Hello")
    window2.geometry("200x200")
    x=lisc_no()
    label1=Label(window2,text="Your Registration Number is {}".format(x))
    label1.pack()
    button=Button(window2,text="Sign In",command=window2.destroy)
    button.pack()

def getregno():
    text=entry1.get()
    search(text)


window=Tk()
window.title("Team Trees")
window.geometry("330x330")
photo = ImageTk.PhotoImage(Image.open("Trees.jpg"))
label2 = Label(window, image = photo)
label2.place(x=0,y=0)

entry1=Entry(window)
entry1.grid(column=3, row=1)
label1=ttk.Label(window,text="Registration Number", background="Lavender")
label1.grid(column=2, row=1)


button1=ttk.Button(window,text="Sign In",command=getregno)
button2=ttk.Button(window,text="Sign Up",command=signupwindow)
button3=ttk.Button(window,text="Quit",command=window.destroy)
button4=ttk.Button(window,text="Replantation",command=tree_select1)
button1.place(x=130,y=70,width=80)
button2.place(x=240,y=70,width=80)
button3.place(x=140,y=130,width=60)
button4.place(x=20,y=70,width=80)

window.mainloop()

