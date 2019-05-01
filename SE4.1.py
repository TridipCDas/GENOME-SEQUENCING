import mysql.connector
from tkinter import *
from tkinter import filedialog
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="gene1"
);

root=Tk();
#base_folder = os.path.dirname(__file__)
root.geometry("600x500");
'''path = os.path.join(base_folder, '‪Asset.gif')
filename = PhotoImage(file = path);
back = Label(root, image=filename);
back.place(x=0, y=0, relwidth=1, relheight=1)
'''
mycursor = db.cursor();
count = 0;
current = 2;
#Main
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



#Database
def insertSequence(sequence,info,lines):

    loc = info.split(':')[1].split(' ')[0].replace("-","..");

    if ',' in loc:
        return;

    if loc[0] == 'c':
        num = loc.split('..');
        temp = []
        temp.append(num[1]);
        temp.append('..');
        temp.append(num[0][1:]);
        loc = ''.join(temp);

    for line in lines:
        print(loc + ' ' + line.split('\t')[0])
        if loc == line.split('\t')[0]:
            print('dOOO\n')
            temp = line.split('\t');
            global count;
            count += 1;
            '''sql = "INSERT INTO Gene1 (Slno, Info, Gene, CountA, CountT, CountG, CountC, Length, GplusC, Location, Strand, LengthD, PID, GeneD, Synonym, Code, COG, Product) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(count, info, sequence, sequence.count("A"), sequence.count("T"), sequence.count("G"), sequence.count("C"), len(sequence), ((sequence.count("G") + sequence.count("C"))*100)/(sequence.count("A") + sequence.count("T") + (sequence.count("G") + sequence.count("C"))), temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8]);
            mycursor.execute(sql,val)
            db.commit()'''
            return;


#Checking for errors in the sequences
def checkSequence(sequence):
    temp = 1;
    for check in sequence:
        for part in check:
            if part!="A" and part!="T" and part!="G" and part!="C":
                #print('Not a fasta file!!')
                temp = 0;
                #quit();
    if temp == 1:
        status(0);
    else:
        status(1);


#Writing to a File
def writeFile(sequence,fw,info):
    fw.write('{0:<10}{1:^100}{2:^70}\n'.format('Sl. No','Information','Gene Sequence'));
    #print('Writing to a file!!!\n')
    i=0
    j=1
    #op=""
    for i in range(0,len(sequence)):
        #op=str(j),info[i],sequence[i]
        sl=str(j)+'.'
        fw.write('{0:10}{1:100}{2:}\n'.format(sl,info[i],sequence[i]))
        j=j+1;
    #print('Writing Done!!!')

def called(filename):
    temp=0;
    fd=open(filename,"r")
    fw=open("output.txt","w")
    fo=open("GeneDetails.txt","r")
    reader1=fd.read(1);
    global current
    lines = fo.read().split('\n');

    reader = fo.readline();
    reader = fo.readline();
    reader = fo.readline();

    if(reader1!='>'):
        #print("Not A Fasta File!!");
        status(1);
        #quit();
    else:
        fd.seek(0,0);
        reader=fd.read();

        text=[]
        text=reader.split('>')

        text[0:]=text[1:]
        info=[]
        sequence=[]

        for x in text:
            part1=[]
            part2=[]
            if "\n\n" in x:
                #print("Not A Fasta File!!")
                temp=1;
                status(1);
                #quit();
            count=0;
            for ch in x:
                if ch!='\n' and count==0:
                    part1.append(ch);
                if ch=='\n':
                    count+=1
                    continue;
                if count!=0:
                    part2.append(ch);
            s1=''.join(part1)
            s2=''.join(part2)
            info.append(s1)
            sequence.append(s2)

            current += 1
            insertSequence(s2,s1,lines[current:]);

        if temp == 0:
            checkSequence(sequence);
            #status(2);
            writeFile(sequence,fw,info)
            #status(3);


def mfileopen():
    root.file=filedialog.askopenfile();
    label=Label(text=root.file.name);
    label.pack();
    print(root.file.name);
    called(root.file.name);


label = Label(text="Gene File Validator\n",font="Times").pack();
button = Button(text="open file",bg="#bacff2",activebackground="#a8abdd",width=30,command=mfileopen).pack();
root.mainloop();
