from tkinter import *
import base64

root = Tk()
root.geometry("640x320")
root.resizable(0,0)
root.title("Message Encode and Decode")

Label(root,text="Message Encode and Decode",font='arial 20 bold').pack()


private_key=StringVar()
mode=StringVar()
Result=StringVar()
Text=StringVar()
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) +ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) -ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get()=='e'):
        Result.set(Encode(private_key.get(),Text.get()))
    elif(mode.get()=='d'):
        Result.set(Decode(private_key.get(),Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root,font='arial 12 bold',text='Message').place(x=60,y=60)
Entry(root,font='arial 10',textvariable=Text,bg='ghost white').place(x=180,y=60)
Label(root,font='arial 12 bold',text='Key').place(x=60,y=90)
Entry(root,font='arial 10',textvariable=private_key,bg='ghost white').place(x=180,y=90)
Label(root,font='arial 12 bold',text='Mode').place(x=60,y=120)
Entry(root,font='arial 10',textvariable=mode,bg='ghost white').place(x=180,y=120)
Label(root,font='arial 12 bold',text='Result').place(x=60,y=200)
Entry(root,font='arial 10',textvariable=Result,bg='ghost white').place(x=180,y=200)
Button(root,font='arial 10 bold',text='Result',padx=2,bg='LightGray',command=Mode).place(x=180,y=150)
Button(root,font='arial 10 bold',text='Reset',width=6,bg='LightGray',command=Reset).place(x=240,y=150)
Button(root,font='arial 10 bold',text='Exit',width=6,bg='LightGray',command=Exit).place(x=180,y=240)
root.mainloop()
