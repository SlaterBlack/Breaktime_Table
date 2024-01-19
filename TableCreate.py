import tkinter  as tk
from tkinter import ttk

teamNames = []
teamTimes = []
teamDep = []
LARGE_FONT= ("Verdana", 12)

class OWApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Slater's Officeworks App")

        self.geometry("900x600")
        self.resizable(0,0)
        container = tk.Frame(self,width=900,height=600)
        container.pack(side="top", fill="both", expand = True)

        self.frames = {}
        frame = BreakSheet(container)
        self.frames[BreakSheet] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        ttk.Button(container, text="Exit", command= self.destroy,width=50).grid(row=1,column=0,sticky="n")

class BreakSheet(tk.Frame):
    
    def __init__(self, parent):

        def PrintTable():
            #table code here
            print("table printed")

        def addTeam():
            #add team code here
            print("Team added")

        tk.Frame.__init__(self, parent)
        #   Setting Grid sizes
        colCount = 5
        rowCount= 6
        for col in range(colCount):
            self.grid_rowconfigure(col,minsize=40, weight=1)
        for row in range(rowCount):
            self.grid_columnconfigure(row,minsize=150, weight=1)

        #   Header
        ttk.Label(self, text="Break Sheet Maker", font=LARGE_FONT).grid(row=0,column=3)

        #   Team Name input
        name = tk.StringVar()
        ttk.Label(self, text="Name", font=LARGE_FONT).grid(row=1,column=1,sticky="nsew")
        tk.Entry(self).grid(row=2, column=1,sticky="nw")
        
        #   StartTime input
        ttk.Label(self, text="Start Time", font=LARGE_FONT).grid(row=1,column=2,sticky="nsew")
        startTimeFrame = tk.Frame(self,width = 50, relief="raised")
        startTimeFrame.grid(row =2, column=2, sticky="nsew")
        tk.Spinbox(startTimeFrame,from_=0, to=12,width=5).grid(row=0, column=0)
        tk.Spinbox(startTimeFrame,values=[0,30],width=5).grid(row=0, column=1)
        tk.Spinbox(startTimeFrame,values=["am","pm"],width=5).grid(row=0, column=2)

        #   EndTime input
        ttk.Label(self, text="End Time", font=LARGE_FONT).grid(row=1,column=3,sticky="nsew")
        endTimeFrame = tk.Frame(self,width = 50, relief="raised")
        endTimeFrame.grid(row =2, column=3, sticky="nsew")
        tk.Spinbox(endTimeFrame,from_=0, to=12,width=5).grid(row=0, column=0)
        tk.Spinbox(endTimeFrame,values=[0,30],width=5).grid(row=0, column=1)
        tk.Spinbox(endTimeFrame,values=["am","pm"],width=5).grid(row=0, column=2)

        #   Department input
        ttk.Label(self, text="Department", font=LARGE_FONT).grid(row=1,column=4)
        DepFrame = tk.Frame(self,width = 50, relief="raised")
        DepFrame.grid(row =2, column=4, sticky="nsew")
        tk.Spinbox(DepFrame,values=["POS/PG","P&C","Service"]).grid(row=0, column=0)

        # Main Table display

        #   Footer
        ttk.Button(self,text = "Add team member",command= addTeam).grid(row=5,column=2,sticky="nsew")
        ttk.Button(self, text="Create Table",command= PrintTable).grid(row=5,column=3,sticky="nsew")

        

app = OWApp()
app.mainloop()