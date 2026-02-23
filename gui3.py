import tkinter as  tk

def show_name():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

#create window
root =tk.Tk()
root.title("Name Input")
root.geometry("400x250")
root.configure(bg="lightblue")

#title
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 14))
result_label.pack(pady=20)

#entry box
tk.Label(root, text="Enter your name:", bg="lightblue", font=("Arial", 14)).pack(pady=20)

#submit button
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

tk.Button(root,text ="Submit", command=show_name, font=("Arial", 14)).pack(pady=10)

#result labeel

result_label = tk.Label(root,text="", bg="lightblue", font=("Arial", 14),fg="green")
result_label.pack(pady=20)

root.mainloop()