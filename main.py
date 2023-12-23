import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App by Demilade")

        self.tasks = []

        # Entry and Add button
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Mark as Completed and Remove buttons
        mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        mark_completed_button.grid(row=2, column=0, padx=10, pady=10)
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            completed_task = f"{task} (Completed)"
            self.task_listbox.delete(index)
            self.task_listbox.insert(tk.END, completed_task)
            self.tasks[index] = completed_task
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
