import tkinter as tk

root = tk.Tk()
root.title("My Window")
root.geometry("1000x800")

cell_1 = tk.Text()
cell_1.config(height = 10 ,width=1)
cell_1.grid(row=0,column= 0, sticky="nsew")
# cell_1.columnconfigure(0, weight=1)

inner_grid = tk.Frame()
inner_grid.grid(row=1, column=0, sticky="nsew")

for i in range(2):
    for j in range(2):
        inner_cell = tk.Button(inner_grid, text="{}, {}".format(i, j))
        inner_cell.grid(row=i, column=j, sticky="nsew")

for i in range(2):
    inner_grid.columnconfigure(i, weight=1)
for i in range(2):
    inner_grid.rowconfigure(i, weight=1)

for i in range(1):
    root.columnconfigure(0, weight=1 )
for i in range(2):
    root.rowconfigure(i, weight=1)

root.rowconfigure(0 , minsize=10)
print(root.rowconfigure(0)["minsize"])

root.mainloop()
