import tkinter as tk
from tkinter import ttk
import time as tm
import os

class Modify(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Modify", font=("Lucida Handwriting",30, "bold"))
        label.pack(side="top", fill="x", pady=10)
        
        firstStyle = ttk.Style()
        firstStyle.configure("First.TButton",font = ('Sans','15','bold'))

        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))
        
        inputBttn = ttk.Button(self, text="Input the money?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("InputFees"), style ="First.TButton")
        inputBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        changeBttn = ttk.Button(self, text="Change today's input?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("ModifyFees"), style ="First.TButton")
        changeBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)
        
        home = ttk.Button(self, text="Go back to the home page",
                           command=lambda: controller.show_frame("Home"), style ="Home.TButton")
        home.pack(fill= "both",expand = True, padx = 300, pady = 5)

class InputFees(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        topFrame.pack(fill = "both",expand = True)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        entryName = tk.Label(topFrame, text = "Enter the amount: ",font=("NuevaStd",20))
        entryName.pack(fill = "both", expand = True,padx = 1, pady = 1, side = "left")

        self.amount = tk.StringVar()
        entry = tk.Entry(topFrame,textvariable = self.amount, justify = "left",width = 50,font=("NuevaStd",15))
        entry.pack(fill = 'both',expand = True ,padx = 5,pady = 5)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(fill = "both",expand = True)

        inputMoney = ttk.Button(bottomFrame, text = "Press to confirm amount of deposit",
                                command = lambda: self.inputFile(),style = "Home.TButton")
        inputMoney.pack(fill="x",expand = True, padx =250, pady = 1,side="top")
        
        home = ttk.Button(bottomFrame, text="To previous page",
                           command=lambda: controller.show_frame("Modify"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 1,side = "bottom")
        
    def inputFile(self):
        answer = tk.messagebox.askyesno("Confirm","Are you sure?")
        if answer == True:
            try:
                try:
                    x = float(self.amount.get())
                except ValueError:
                    tk.messagebox.showerror("Error!","Invalid input!")
                    return
                if(x>1000000):
                    tk.messagebox.showerror("AmountError!","More than a million!")
                    return
                elif(x<-1000000):
                    tk.messagebox.showerror("AmountError!","Less than negative million!")
                    return
                
                if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                    toRead = open('Payment.txt','r')
                    currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                    currTime = currentTime.replace(',',' ')
                    currTime = currTime.replace(':',' ')
                    currTime = currTime.replace('+',' ') #get info on today's date
                    currTime = currTime.replace(',',' ')
                    currTime = currTime.split()

                    data = toRead.readlines()
                    for line in data:
                        
                        line = line.replace(',',' ')
                        line = line.replace(':',' ')
                        line = line.replace('+',' ')
                        line = line.replace(',',' ')
                        line = line.split()
                        
                        if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]):
                            tk.messagebox.showerror("Error!","Today's chance is done!")
                            toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                            return
        
                    toRead.close()

                    toWrite = open('Payment.txt','a')
                    currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    toWrite.write(str(self.amount.get())+" "+currentTime+"\n")
                    toWrite.close()
                    
                else: #empty file
                    toWrite = open('Payment.txt','a')
                    currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    toWrite.write(str(self.amount.get())+" "+currentTime+"\n")
                    toWrite.close()
                   
            except OSError: #file doesn't exist
                tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
        else:
            return

class ModifyFees(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        topFrame.pack(fill = "both",expand = True)

        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        entryName = tk.Label(topFrame, text = "Enter to change amount: ",font=("NuevaStd",20))
        entryName.pack(fill = "both", expand = True,padx = 1, pady = 1, side = "left")

        self.amount = tk.StringVar()
        entry = tk.Entry(topFrame,textvariable = self.amount, justify = "left",width = 50,font=("NuevaStd",15))
        entry.pack(fill = 'both',expand = True ,padx = 5,pady = 5)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(fill = "both",expand = True)

        inputMoney = ttk.Button(bottomFrame, text = "Press to change",
                                command = lambda: self.inputFile(),style = "Home.TButton")
        inputMoney.pack(fill="x",expand = True, padx =250, pady = 1,side="top")
        
        home = ttk.Button(bottomFrame, text="To previous page",
                           command=lambda: controller.show_frame("Modify"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 1,side = "bottom")
        
    def inputFile(self):
        answer = tk.messagebox.askyesno("Confirm","Are you sure?")
        if answer == True:
            try:
                try:
                    x = float(self.amount.get())
                except ValueError:
                    tk.messagebox.showerror("Error!","Invalid input!")
                    return
                if(x>1000000):
                    tk.messagebox.showerror("AmountError!","More than a million!")
                    return
                elif(x<-1000000):
                    tk.messagebox.showerror("AmountError!","Less than negative million!")
                    return
                
                if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                    
                    toRead = open('Payment.txt','r')
                    toWrite = open('PaymentTemp.txt','w')
                    currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                    currTime = currentTime.replace(',',' ')
                    currTime = currTime.replace(':',' ')
                    currTime = currTime.replace('+',' ') #get info on today's date
                    currTime = currTime.replace(',',' ')
                    currTime = currTime.split()

                    data = toRead.readlines()
                    for line in data:

                        temp = line
                        temp = temp.replace(',',' ')
                        temp = temp.replace(':',' ')
                        temp = temp.replace('+',' ')
                        temp = temp.replace(',',' ')
                        temp = temp.split()
                        
                        if(currTime[1] == temp[2] and currTime[2] == temp[3] and currTime[3] and temp[4]): #found
                            toWrite.write(str(self.amount.get())+" "+currentTime+"\n")
                        else:
                            toWrite.write(line)
                            
                    toRead.close()
                    toWrite.close()#curr(1 is month, 2 is date, 3 is year),temp(2 is month, 3 is date, 4 is year)

                    os.remove('Payment.txt')
                    os.rename('PaymentTemp.txt','Payment.txt')
                    
                else: #empty file
                    tk.messagebox.showerror("Error!","Unable to open file cause file is empty!")
                   
            except OSError: #file doesn't exist
                tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")

        else:
            return
