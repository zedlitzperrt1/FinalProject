# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:22:17 2018

@author: cluel
"""
from Prims import *
import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox, Tk

T = ({0},[])
#G = Weighted_Graph('test_graph.txt')

class GUI:
    def __init__(self, master):
        self.edge_file_name = ''
        self.master = master
        master.title("Prim's Algorithm for MST")
        self.label = Label(master, text="Click either button to select edge file.")
        self.label.pack()

        self.step = Button(master, text="Click to Iterate once",command=self.primstep)
        self.step.pack(side=tk.LEFT)
        self.finish = tk.Button(master, text="Run full cycle",command=self.primfinish)
        self.finish.pack(side=tk.RIGHT)  
 
    def primstep(self):
        if self.edge_file_name == '':
            self.edge_file_name = filedialog.askopenfilename()            
        c = Prims_step(T,self.edge_file_name,0)
        plt.draw()
        if T[0] == G.vertex_set():
            messagebox.showinfo("Total MST cost:           ", c)
    def primfinish(self):
        edge_file_name = filedialog.askopenfilename()
        c = Prims(edge_file_name,0,draw=True)
        plt.draw()
        messagebox.showinfo("Total MST cost:           ", c)

def main():
    root = tk.Tk()
    root.minsize(400,100)
    main_gui = GUI(root)
    root.mainloop() 
 
    
if __name__ == '__main__':
    main()
