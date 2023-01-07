import tkinter as tk

class calc:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('calculator')
        self.root.geometry('500x600')
        self.textbox=tk.Text(self.root,font=('Arial',18),height=3)
        self.textbox.pack(padx=10,pady=20)
        self.buttons()
        


        self.root.mainloop()


    def clicked(self,val):
        self.textbox.insert('insert',val)


    def clear(self):
        self.textbox.delete('1.0','end')
    def clicked_brackets(self):
        self.clicked('(')
        self.clicked(')')
        self.textbox.mark_set('insert','end-2c')
    def evaluate_and_clear(self):
        try:
            calcstr=self.textbox.get('1.0','end')
            if 'x' in calcstr:
                calcstr=calcstr.replace('x','*')
            ans=eval(calcstr)
            self.textbox.delete('1.0','end')
            self.textbox.insert(tk.END,ans)

        except:
            self.clear()
    def CE(self):
        self.textbox.delete("end-2c", 'end')



    def buttons(self):
        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)
        buttonframe.columnconfigure(4, weight=1)
        self.checkval=tk.StringVar()
        # top row buttons
        self.btn7 = tk.Button(buttonframe, text='7', font=('Arial', 18),command=lambda: self.clicked(7))
        self.btn7.grid(row=0, column=0, sticky='news')
        self.btn8 = tk.Button(buttonframe, text='8', font=('Arial', 18),command=lambda: self.clicked(8))
        self.btn8.grid(row=0, column=1, sticky='news')
        self.btn9 = tk.Button(buttonframe, text='9', font=('Arial', 18),command=lambda: self.clicked(9))
        self.btn9.grid(row=0, column=2, sticky='news')
        self.div = tk.Button(buttonframe, text='/', font=('Arial', 18),command=lambda: self.clicked('/'))
        self.div.grid(row=0, column=3, sticky='news')
        #second row buttons
        self.btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18),command=lambda: self.clicked(4))
        self.btn4.grid(row=1, column=0, sticky='news')
        self.btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18),command=lambda: self.clicked(5))
        self.btn5.grid(row=1, column=1, sticky='news')
        self.btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18),command=lambda: self.clicked(6))
        self.btn6.grid(row=1, column=2, sticky='news')
        self.mult = tk.Button(buttonframe, text='x', font=('Arial', 18),command=lambda: self.clicked('x'))
        self.mult.grid(row=1, column=3, sticky='news')
        #third row buttons
        self.btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18),command=lambda: self.clicked(1))
        self.btn1.grid(row=2, column=0, sticky='news')
        self.btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18),command=lambda: self.clicked(2))
        self.btn2.grid(row=2, column=1, sticky='news')
        self.btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18),command=lambda: self.clicked(3))
        self.btn3.grid(row=2, column=2, sticky='news')
        self.minus = tk.Button(buttonframe, text='-', font=('Arial', 18),command=lambda: self.clicked('-'))
        self.minus.grid(row=2, column=3, sticky='news')
        #bottom buttons
        self.decimal = tk.Button(buttonframe, text='.', font=('Arial', 18),command=lambda: self.clicked('.'))
        self.decimal.grid(row=3, column=0, sticky='news')
        self.btn0 = tk.Button(buttonframe, text='0', font=('Arial', 18),command=lambda: self.clicked(0))
        self.btn0.grid(row=3, column=1, sticky='news')
        self.equals = tk.Button(buttonframe, text='=', font=('Arial', 18),command=lambda:self.evaluate_and_clear())
        self.equals.grid(row=3, column=2, sticky='news')
        self.plus = tk.Button(buttonframe, text='+', font=('Arial', 18),command=lambda: self.clicked('+'))
        self.plus.grid(row=3, column=3, sticky='news')

        self.brack1 = tk.Button(buttonframe, text='( )', font=('Arial', 18), command=lambda: self.clicked_brackets())
        self.brack1.grid(row=4, column=1, sticky='news')

        self.ce = tk.Button(buttonframe, text='CE', font=('Arial', 18),command=lambda: self.CE())
        self.ce.grid(row=0, column=4, sticky='news')
        buttonframe.pack(fill='both')

calc()
