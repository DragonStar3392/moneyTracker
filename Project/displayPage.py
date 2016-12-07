import tkinter as tk
from tkinter import ttk
import time as tm
import os

class Display(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Display", font=("Lucida Handwriting",30, "bold"))
        label.pack(side="top", fill="x", pady=10)

        newStyle = ttk.Style()
        newStyle.configure("Newstyle.TButton",font = ('Sans','15','bold'))

        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))
        
        dtodayBttn = ttk.Button(self, text="Display today's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DToday"), style ="Newstyle.TButton")
        dtodayBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dweekBttn = ttk.Button(self, text="Display this week's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DWeek"), style ="Newstyle.TButton")
        dweekBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dmonthBttn = ttk.Button(self, text="Display this month's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DMonth"), style ="Newstyle.TButton")
        dmonthBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dyearBttn = ttk.Button(self, text="Display this year's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DYear"), style ="Newstyle.TButton")
        dyearBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)
        
        home = ttk.Button(self, text="Go back to the home page",
                           command=lambda: controller.show_frame("Home"), style ="Home.TButton")
        home.pack(fill= "both",expand = True, padx = 300, pady = 5)
        
class DToday(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
    def shows(self):
        try:
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
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]): #today
                        tk.messagebox.showinfo("Today","Today's input: "+str(line[0])+" Baht.")
                        toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                        return
        
                toRead.close()
                tk.messagebox.showerror("Error!","Today's one doesn't exist yet!")
                    
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
        
class DWeek(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
        
        self.displayed = 0
        
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                output = []
                found = False
                
                toRead = open('Payment.txt','r')
                currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                currTime = currentTime.replace(',',' ')
                currTime = currTime.replace(':',' ')
                currTime = currTime.replace('+',' ') #get info on today's date
                currTime = currTime.replace(',',' ')
                currTime = currTime.split()

                data = toRead.readlines()
                for items in range(len(data)):
                    
                    line = data[items]
                    line = line.replace(',',' ')
                    line = line.replace(':',' ')
                    line = line.replace('+',' ')
                    line = line.replace(',',' ')
                    line = line.split()
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]): #use today as reference
                        found = True #line 2 = month, 3 = date, 4 = year , ex: 50.0 Tuesday Dec 15, 2016
                        
                        if line[1] == 'Sunday': #all checks start from monday and if exists
                            output.append(data[items-6])if (items-6)>= 0 else output.append("0 Monday No input yet")#monday
                            output.append(data[items-5])if (items-5)>= 0 else output.append("0 Tuesday No input yet")#tuesday
                            output.append(data[items-4])if (items-4)>= 0 else output.append("0 Wednesday No input yet")#wednesday
                            output.append(data[items-3])if (items-3)>= 0 else output.append("0 Thursday No input yet") #thursday
                            output.append(data[items-2])if (items-2)>= 0 else output.append("0 Friday No input yet") #friday
                            output.append(data[items-1])if (items-1)>= 0 else output.append("0 Saturday No input yet")#saturday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Sunday No input yet")

                        elif line[1] == 'Saturday':
                            output.append(data[items-5])if (items-5)>= 0 else output.append("0 Monday No input yet")#monday
                            output.append(data[items-4])if (items-4)>= 0 else output.append("0 Tuesday No input yet")#tuesday
                            output.append(data[items-3])if (items-3)>= 0 else output.append("0 Wednesday No input yet")#wednesday
                            output.append(data[items-2])if (items-2)>= 0 else output.append("0 Thursday No input yet") #thursday
                            output.append(data[items-1])if (items-1)>= 0 else output.append("0 Friday No input yet") #friday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Saturday No input yet")
                            output.append("0 Sunday No input yet") #coming sunday

                        elif line[1] == 'Friday':
                            output.append(data[items-4])if (items-4)>= 0 else output.append("0 Monday No input yet")#monday
                            output.append(data[items-3])if (items-3)>= 0 else output.append("0 Tuesday No input yet")#tuesday
                            output.append(data[items-2])if (items-2)>= 0 else output.append("0 Wednesday No input yet")#wednesday
                            output.append(data[items-1])if (items-1)>= 0 else output.append("0 Thursday No input yet") #thursday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Friday No input yet")
                            output.append("0 Saturday No input yet") #coming saturday
                            output.append("0 Sunday No input yet") #coming sunday
                            
                        elif line[1] == 'Thursday':
                            output.append(data[items-3])if (items-3)>= 0 else output.append("0 Monday No input yet")#monday
                            output.append(data[items-2])if (items-2)>= 0 else output.append("0 Tuesday No input yet")#tuesday
                            output.append(data[items-1])if (items-1)>= 0 else output.append("0 Wednesday No input yet")#wednesday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Thursday No input yet")
                            output.append("0 Friday No input yet") #coming friday
                            output.append("0 Saturday No input yet") #coming saturday
                            output.append("0 Sunday No input yet") #coming sunday

                        elif line[1] == 'Wednesday':
                            output.append(data[items-2])if (items-2)>= 0 else output.append("0 Monday No input yet")#monday
                            output.append(data[items-1])if (items-1)>= 0 else output.append("0 Tuesday No input yet")#tuesday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Wednesday No input yet")
                            output.append("0 Thursday No input yet") #coming thursday
                            output.append("0 Friday No input yet") #coming friday
                            output.append("0 Saturday No input yet") #coming saturday
                            output.append("0 Sunday No input yet") #coming sunday

                        elif line[1] == 'Tuesday':
                            output.append(data[items-1])if (items-2)>= 0 else output.append("0 Monday No input yet")#monday
                            try:
                                output.append(data[items])   #today
                            except IndexError:
                                output.append("0 Tuesday No input yet")
                            output.append("0 Wednesday No input yet") #coming wednesday
                            output.append("0 Thursday No input yet") #coming thursday
                            output.append("0 Friday No input yet") #coming friday
                            output.append("0 Saturday No input yet") #coming saturday
                            output.append("0 Sunday No input yet") #coming sunday

                        elif line[1] == 'Monday':
                            try:
                                output.append(data[items]) #today
                            except IndexError:
                                output.append("0 Monday No input yet")
                            output.append("0 Tuesday No input yet") #coming tuesday
                            output.append("0 Wednesday No input yet") #coming wednesday
                            output.append("0 Thursday No input yet") #coming thursday
                            output.append("0 Friday No input yet") #coming friday
                            output.append("0 Saturday No input yet") #coming saturday
                            output.append("0 Sunday No input yet") #coming sunday
        
                toRead.close()

                topFrame = tk.Frame(self)
                topFrame.pack(fill = "both",expand = True)
                
                if found == False:
                    tk.messagebox.showerror("Error!","User haven't input anything this week yet!")
                else:
                    if self.displayed > 0:
                        tk.messagebox.showerror("Error!","What are you doing?")
                    elif self.displayed == 0:
                        sumz = 0
                        for line in output:
                            line = line.split()
                            display = tk.Label(topFrame, text = "Amount: %sBaht \tDay: %s \tDate: %s %s %s" % (line[0],line[1],line[2],line[3],line[4]),font=("NuevaStd",14))
                            display.pack(fill = "both", expand = True,padx = 1, side = "top")
                            sumz += float(line[0])

                        total = tk.Label(topFrame, text = "Total of this month is: %.2f Baht"%(sumz),font=("NuevaStd",20))
                        total.pack(fill = "both", expand = True,padx = 1, pady = 1, side = "top")
                        
                        self.displayed = 1
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")

class DMonth(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        bottomFrame = tk.Frame(self)
        bottomFrame.pack(fill = "both",expand = True)
        
        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))
        
        show = ttk.Button(bottomFrame, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))
        
        home = ttk.Button(bottomFrame, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)

        self.displayed = 0
        
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                output = []
                found = False
                
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
                        
                    if(currTime[1] == line[2]): #this month
                        output.append((str(line[0])+" "+str(line[2])+" "+str(line[3])+" "+str(line[4]))) #keep data line[1-3] and line[0]
                        found = True #line 0 is money, 2 = month, 3 = date, 4 = year
        
                toRead.close()

                topFrame = tk.Frame(self)
                topFrame.pack(fill = "both",expand = True)
                
                if found == False:
                    tk.messagebox.showerror("Error!","User haven't input anything this month yet!")
                else:
                    if self.displayed > 0:
                        tk.messagebox.showerror("Error!","What are you doing?")
                    elif self.displayed == 0:
                        sumz = 0
                        for line in output:
                            line = line.split()
                            display = tk.Label(topFrame, text = "Amount: %s Baht \tDate: %s %s, %s" % (line[0],line[1],line[2],line[3]),font=("NuevaStd",14))
                            display.pack(fill = "both", expand = True,padx = 1, side = "top")
                            sumz += float(line[0])

                        total = tk.Label(topFrame, text = "Total of this month is: %.2f Baht"%(sumz),font=("NuevaStd",20))
                        total.pack(fill = "both", expand = True,padx = 1, pady = 1, side = "top")
                        
                        self.displayed = 1
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
                
class DYear(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(fill = "both",expand = True)
        
        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))
        
        show = ttk.Button(bottomFrame, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))
        
        home = ttk.Button(bottomFrame, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)

        self.displayed = 0
        
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                output = []
                found = False
                
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
                        
                    if(currTime[3] == line[4]): #this year
                        output.append((str(line[0])+" "+str(line[2])+" "+str(line[3])+" "+str(line[4]))) #keep data line[2-4] and line[0]
                        found = True #line 0 is money, 2 = month, 3 = date, 4 = year, 1 is the day ex: Monday, Tuesday...
        
                toRead.close()

                topFrame = tk.Frame(self)
                topFrame.pack(fill = "both",expand = True)
                
                if found == False:
                    tk.messagebox.showerror("Error!","User haven't input anything this year yet!")
                else:
                    if self.displayed > 0:
                        tk.messagebox.showerror("Error!","What are you doing?")
                    elif self.displayed == 0:
                        sumz = 0
                        for line in output:
                            line = line.split()
                            display = tk.Label(topFrame, text = "Amount: %s Baht \tDate: %s %s, %s" % (line[0],line[1],line[2],line[3]),font=("NuevaStd",14))
                            display.pack(fill = "both", expand = True,padx = 1, side = "top")
                            sumz += float(line[0])

                        total = tk.Label(topFrame, text = "Total of this year is: %.2f Baht"%(sumz),font=("NuevaStd",20))
                        total.pack(fill = "both", expand = True,padx = 1, pady = 1, side = "top")
                        
                        self.displayed = 1
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
