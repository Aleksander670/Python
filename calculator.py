from tkinter import *

def input_into_entry(symbol):
    textbox.insert(END, symbol)

def clear_textbox():
    textbox.delete(0, END)

def substract_textbox():
    textbox.delete(textbox.index(END)-1)

def count(): 
    text = textbox.get()
    try:
        result = eval(text)
        clear_textbox()
        input_into_entry(str(result))
    except Exception as e:
        clear_textbox()
        input_into_entry("Error")

window = Tk()
window.title("Калькулятор");
window.geometry('340x480');

textbox = Entry(window, font=('', 42))
textbox.pack(fill=X, padx=5, pady=5)

textbox.bind("<Key>", lambda e: "break")

buttons = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', '*'],
    ['7', '8', '9', '-'],
    ['.', '0', '=', '+']
]

for i in range(4):   
    for j in range(4):   
        btn_text = buttons[i][j]   
        if btn_text == '=':
            btn = Button(window, bg='black', fg='white', text=btn_text, width=5, height=2, command=count)
        else:
            btn = Button(window, bg='black', fg='white', text=btn_text, width=5, height=2, command=lambda symbol=btn_text: input_into_entry(symbol))    
             
        btn.place(x=5 + j * 82, y=66 + i * 82, width=82, height=82)  

substract_button = Button(window, bg='black', fg='white', text='<-', width=20, height=2, command = substract_textbox)  
substract_button.place(x=5, y=66 + 4 * 82, width=251, height=82)  

clear_button = Button(window, bg='black', fg='white', text='C', width=20, height=2, command = clear_textbox)  
clear_button.place(x=251, y=66 + 4 * 82, width=82, height=82)  

    
window.mainloop();


    
