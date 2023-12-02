# ----------------------------------------   *** Password Generator ***   ---------------------------------------------
import tkinter as tk
import tkinter.ttk as ttk
import random


class PasswordGeneratorApp:
    def __init__(self, master=None):
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(background="#000000", pady=20, width=200)
        toplevel1.geometry("320x340")
        self.entry_box = ttk.Entry(toplevel1)       
        self.entry_box.configure(
            font=("Arial CE", 12),
            state='disabled', justify='center')     
        self.entry_box.grid(column=1, padx=25, pady=15, row=1, sticky="ew")
        self.gen_button = ttk.Button(toplevel1)
        self.gen_button.configure(text='Generate Password')
        self.gen_button.grid(column=1, ipady=2, pady=20, row=2)
        self.gen_button.configure(command=self.gen_pass)
        self.reset_button = ttk.Button(toplevel1)
        self.reset_button.configure(text='Reset')
        self.reset_button.grid(column=1, ipadx=16, ipady=2, pady=20, row=4)
        self.reset_button.configure(command=self.reset_all)
        label1 = ttk.Label(toplevel1)
        label1.configure(
            background="#000000",
            font="{Arial} 13 {}",
            foreground="#5b5bff",
            text='PASSWORD GENERATOR')
        label1.grid(column=1, row=0)        
        self.copy_button = ttk.Button(toplevel1)
        self.copy_button.configure(text='Copy to clipboard')
        self.copy_button.grid(column=1, ipadx=1, ipady=2, pady=20, row=3)
        self.copy_button.configure(command=self.copy_text)
                       
        toplevel1.columnconfigure(1, weight=1)
    
        self.mainwindow = toplevel1
        
        
    # copy text to clipboard           
    def copy_text(self):
        self.entry_box.clipboard_clear()
        if self.entry_box.get():
            self.entry_box.clipboard_append(self.entry_box.get())
               
    def run(self):
        self.mainwindow.mainloop()
        
        
    # generate password
    def gen_pass(self):
        self.entry_box.delete(0, tk.END)
        
        self.entry_box.grid(column=1, padx=25, pady=15, row=1, sticky="ew") 
        password = []
        check = 0
        while len(password) < 22:
            let_sym = [8, 'c', 3,'?', '_', 'g', 'R', 2, '*', 9, 'b', 4, '@', 5, 'p', '_', 6 ,'@', 7, 'z', '!', 9, '$', 3, 'x', '_', '@', 'P', 6, '@', 'T', '&', 3, 6, '$', '_',  'S', 'H', '$', 'k', 7, '$']        
            pick = random.choice(let_sym)
            check += 1
            if check == 1 and pick == '_':
                check = 0
                continue
            else:
                password.append(pick)
                if len(password) == 22:
                    result = ''.join(map(str, password))
                    self.entry_box.configure(state='active')
                    self.entry_box.insert(0,result)
                    self.entry_box.grid(column=1, padx=25, pady=15, row=1, sticky="ew")
    # clear all                                   
    def reset_all(self):       
        self.entry_box.delete(0, tk.END)
        self.entry_box.grid(column=1, padx=25, pady=15, row=1, sticky="ew")
        self.entry_box.configure(state='disabled')
        self.entry_box.clipboard_clear()


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()
