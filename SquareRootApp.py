import tkinter as tk
from functools import partial

#To Find Out Square Root
def call_convert(rlabell,  inputn):
    temp = inputn.get()
    sq=float(float(temp)**0.5)
    rlabelll.config(text = "Square Root Is %.1f" % sq)
    return
#-----------------------------------------------------------------------
root = tk.Tk()
#Setting Geometry Of Tk Window
root.geometry('300x100')
root['bg']="sky blue"
root.title('Square Root Finder')

#Layout Widgets
root.grid_columnconfigure(1,weight=2)
root.grid_rowconfigure(1,weight=2)
inputNumber = tk.StringVar()
var = tk.StringVar()

#Label & Entry Field
input_label=tk.Label(root,text="Enter The Number")
input_entry=tk.Entry(root,textvariable=inputNumber)
input_label.grid(row=1)
input_label.grid(row=1,column=1)

result_label=tk.Label(root)
result_label.grid(row=2,columnspan=3)

#Button Widget
call_convert=partial(call_convert,result_label,inputNumber)
result_button=tk.Button(root,text="Find The Square Root",bg="red",command=call_convert)
result_button.grid(row=3,columnspan=3)

root.mainloop()
