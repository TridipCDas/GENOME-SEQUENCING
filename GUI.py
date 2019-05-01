from tkinter import *
from tkinter import filedialog
import se1

root=Tk();
root.geometry("600x500");
filename = PhotoImage(file = "‪E:\\SE\\Asset.gif");
back = Label(root, image=filename);
back.place(x=0, y=0, relwidth=1, relheight=1)


def mfileopen():
    root.file=filedialog.askopenfile();
    label=Label(text=root.file.name);
    label.pack();
    print(root.file.name);
    se1.called(root.file.name);

def status(num):
    if num == 0:
        result="\nYes It Is A Fasta File";
    elif num == 1:
        result="\nNo It Is Not A Fasta File";
    elif num == 2:
        result="\nWriting The Output Into Another File........";
    else:
        result="\nCompleted Writing!!!";

    label=Label(text=result).pack();



#filename = PhotoImage(file = "E:\\SE1\\dna-strand.gif")
#back = Label(root, image=filename)
#back.image = filename;
#back.place(x=0,y=0);

label = Label(text="Gene File Validator\n",font="Times").pack();
button = Button(text="open file",bg="#bacff2",activebackground="#a8abdd",width=30,command=mfileopen).pack();
root.mainloop();
