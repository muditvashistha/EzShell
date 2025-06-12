import os
import tkinter as tk

root=tk.Tk()
root.title("EzShell")
root.geometry("680x600")
root.resizable(False, False)
root.iconbitmap("conch-shell.ico")





left_frame = tk.Frame(root, width=200, bg="#44475a")
left_frame.pack(side="left", fill="y")


right_frame = tk.Frame(root, bg="#282a36")
right_frame.pack(side="right", expand=True, fill="both")

def ls():
    for clear in right_frame.winfo_children():
        clear.destroy()

    f=os.listdir('.')
    for i in f:

        if os.path.isfile(i):

            row = tk.Frame(right_frame, bg="#282a36")
            row.pack(fill="x", padx=10, anchor="nw")

           
            file_label = tk.Label(row, text=i, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            file_label.pack(side="left", expand=True, fill="x")


def ls_sizes():
    for clear in right_frame.winfo_children():
        clear.destroy()

    f=os.listdir('.')
    for i in f:

        if os.path.isfile(i):
            sizes=str(os.path.getsize(i)) + " bytes"

            row = tk.Frame(right_frame, bg="#282a36")
            row.pack(fill="x", padx=10, anchor="nw")

           
            file_label = tk.Label(row, text=i, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            file_label.pack(side="left", expand=True, fill="x")
            
            size_label = tk.Label(row, text=sizes, bg="#282a36", fg="#50fa7b", font=6, anchor="e")
            size_label.pack(side="right")


def pwd():
    for clear in right_frame.winfo_children():
        clear.destroy() 

    directory=str(os.getcwd())  
    current=tk.Frame(right_frame,bg="#282a36")
    current.pack(fill="x",anchor="nw",padx=10)

    directory_label = tk.Label(current, text=directory, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
    directory_label.pack(side="left", expand=True, fill="x")

def echo():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="enter the message")
    instruct.pack(pady=5)
    def show():
        message=entry.get()
        text_block=tk.Frame(right_frame,bg="#282a36")
        text_block.pack(fill="x",anchor="nw",padx=10)

        message_label = tk.Label(text_block, text=message, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
        message_label.pack(side="left", expand=True, fill="x")
        entry.destroy()
        submit_button.destroy()
        instruct.destroy()
    submit_button=tk.Button(text="Submit",width=5,command=show)
    submit_button.pack(pady=10)



def cat():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="Enter file name")
    instruct.pack(pady=5)
    def file_name():
        
        file=entry.get()
        text_block=tk.Frame(right_frame,bg="#282a36")
        text_block.pack(fill="x",anchor="nw",padx=10)

        directory=os.listdir('.')
        if file+".txt" in directory and os.path.isfile(file+".txt"):
            f=open(file+".txt",'r')
            content=f.read()

            message_label = tk.Label(text_block, text=content, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            message_label.pack(side="left", expand=True, fill="x")
            entry.destroy()
            submit_button.destroy()
            instruct.destroy()
        else:
            error=f"cat: {file+".txt"}: No Such file or directory!"
            message_label = tk.Label(text_block, text=error, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            message_label.pack(side="left", expand=True, fill="x")
            entry.destroy()
            submit_button.destroy()
            instruct.destroy()
    submit_button=tk.Button(text="Read file contents",width=15,command=file_name)
    submit_button.pack(pady=10)


def mkdir():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="Enter folder name")
    instruct.pack(pady=5)
    def make_dir():
        directory_name=entry.get()
        directory=os.listdir('.')
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            current=tk.Frame(right_frame,bg="#282a36")
            current.pack(fill="x",anchor="nw",padx=10)

            directory_label = tk.Label(current, text=f"mkdir: cannot create directory ‘{directory_name}’: File exists", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            directory_label.pack(side="left", expand=True, fill="x")
        except PermissionError:
            current=tk.Frame(right_frame,bg="#282a36")
            current.pack(fill="x",anchor="nw",padx=10)

            directory_label = tk.Label(current, text=f"Permission denied: Unable to create '{directory_name}'.", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            directory_label.pack(side="left", expand=True, fill="x")
            
        except Exception as e:
            current=tk.Frame(right_frame,bg="#282a36")
            current.pack(fill="x",anchor="nw",padx=10)

            directory_label = tk.Label(current, text=f"An error occurred: {e}", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            directory_label.pack(side="left", expand=True, fill="x")
                 


        entry.destroy()
        submit_button.destroy()
        instruct.destroy()
    submit_button=tk.Button(text="Submit",width=5,command=make_dir)
    submit_button.pack(pady=10)
    

def rm():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="Enter file name")
    instruct.pack(pady=5)
    def remove_file():
        message=entry.get()
        directory=os.listdir('.')
        if message in directory and os.path.isfile(message) and os.path.exists(message):
            os.remove(message)
            current=tk.Frame(right_frame,bg="#282a36")
            current.pack(fill="x",anchor="nw",padx=10)

            directory_label = tk.Label(current, text="hello!", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            directory_label.pack(side="left", expand=True, fill="x")
        else:
            current=tk.Frame(right_frame,bg="#282a36")
            current.pack(fill="x",anchor="nw",padx=10)

            directory_label = tk.Label(current, text=f"rm: '{message}' No such file or directory .", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
            directory_label.pack(side="left", expand=True, fill="x")


        

        
        entry.destroy()
        submit_button.destroy()
        instruct.destroy()
        
    submit_button=tk.Button(text="Submit",width=5,command=remove_file)
    submit_button.pack(pady=10)
    
def cd():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="Mention path")
    instruct.pack(pady=5)
    def change_directory():
        path=entry.get()
        if os.path.exists(path) and os.path.isdir(path):
            os.chdir(path)
            output=f"Changed to: {os.getcwd()}"
        else:
            output=f"cd: {path}: No such file or directory"

        text_block=tk.Frame(right_frame,bg="#282a36")
        text_block.pack(fill="x",anchor="nw",padx=10)

        message_label = tk.Label(text_block, text=output, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
        message_label.pack(side="left", expand=True, fill="x")
        entry.destroy()
        submit_button.destroy()
        instruct.destroy()
    submit_button=tk.Button(text="Submit",width=5,command=change_directory)
    submit_button.pack(pady=10)


def clear():
    for f in right_frame.winfo_children():
        f.destroy()

def touch():
    for clear in right_frame.winfo_children():
        clear.destroy()
    entry=tk.Entry(root,width=30)
    entry.pack(pady=20)
    instruct=tk.Label(root,text="Enter the file name with extension")
    instruct.pack(pady=5)
    def create_file():
        file_name=entry.get()
        if file_name in os.listdir('.') and os.path.isfile(file_name):
            os.utime(file_name)
        else:
            try:
                with open(file_name,'w') as fp:
                    pass
            except FileNotFoundError:
                text_block=tk.Frame(right_frame,bg="#282a36")
                text_block.pack(fill="x",anchor="nw",padx=10)

                message_label = tk.Label(text_block, text=f"touch: {file_name}: No such file or directory", bg="#282a36", fg="#50fa7b", font=6, anchor="w")
                message_label.pack(side="left", expand=True, fill="x")
        
        

        entry.destroy()
        submit_button.destroy()
        instruct.destroy()
    submit_button=tk.Button(text="Submit",width=5,command=create_file)
    submit_button.pack(pady=10)

def toggle_text():
    for clear in right_frame.winfo_children():
        clear.destroy()

    command_descriptions = {
   "ls": "Lists all files and folders in the current directory",
   "ls-l": "Shows detailed file information including permissions, size, and date modified", 
   "pwd": "Displays the full path of your current working directory",
   "echo": "Prints text or variables to the screen",
   "cat": "Shows the contents of a file on the screen",
   "mkdir": "Creates a new empty directory/folder",
   "rm": "Deletes files or directories permanently",
   "cd": "Changes your current directory to a different location",
   "clear": "Clears all text from the terminal screen",
   "touch": "Creates a new empty file or updates file timestamps"
}
    
    all_descriptions = "\n\n".join(f"{cmd}->{desc}" for cmd, desc in command_descriptions.items())
    current_text = button.cget("text")
    if current_text == "TRY":
        button.config(text="LEARN")
        button.config(bg="#50fa7b")
        row = tk.Frame(right_frame, bg="#282a36")
        row.pack(fill="x", padx=10, anchor="nw")

           
        file_label = tk.Label(row, text=all_descriptions, bg="#282a36", fg="#50fa7b", font=6, anchor="w")
        file_label.pack(side="left", expand=True, fill="x")
    else:
        button.config(text="TRY")
        button.config(bg="#ff79c6")
        for f in right_frame.winfo_children():
            f.destroy()

    
            
    

tk.Button(left_frame, text="ls",command=ls,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="ls-l",command=ls_sizes,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="pwd",command=pwd,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="echo",command=echo,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="cat",command=cat,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="mkdir",command=mkdir,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="rm",command=rm,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="cd",command=cd,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="clear",command=clear,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
tk.Button(left_frame, text="touch",command=touch,width=10,bg="#44475a",fg="white",borderwidth=5).pack(pady=10)
button=tk.Button(left_frame, text="TRY",command=toggle_text,width=10,bg="#ff79c6",fg="white",borderwidth=5)
button.pack(pady=15)


root.mainloop()

