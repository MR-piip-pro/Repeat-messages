import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
import time
import threading

# تحقق من صلاحيات الروت
def check_root():
    if os.geteuid() != 0:
        messagebox.showerror("Error", """       You must run this                               
        program as root.          """)
        sys.exit(1)

# استدعاء الدالة للتحقق
check_root()

import keyboard  # مكتبة للضغط على الأزرار

# إعداد النافذة
na = tk.Tk()
na.title("AUUOSL")
na.geometry('600x800+350+70')
na.wm_resizable(False, False)

# تعيين الألوان
color1 = "#005f87"
color2 = "#00afaf"
color_Black = "#000000"
color_White = "#FFFFFF"
color_MidnightBlue = "#191970"

# تغيير خلفية النافذة
na.configure(bg=color_Black)

# إعداد النمط باستخدام ttk.Style
style = ttk.Style()
style.configure('Custom.TMenubutton', background=color_MidnightBlue, foreground=color_White, font=("System", 12))
style.map('Custom.TMenubutton',
          background=[('active', color1)],
          foreground=[('active', color_White)])

# إضافة تسمية ترحيبية
label = tk.Label(na, text="Welcome to the humble tool", font=("System", 30), bg=color_Black, fg=color_White)
label.pack(pady=10)

label = tk.Label(na, text="Please enter the message to type", font=("System", 12), bg=color_MidnightBlue, fg=color_White)
label.place(x=190, y=150)

entrye = tk.Text(na, height=5, width=44, bg=color_MidnightBlue, fg=color_White)
entrye.place(x=130, y=180)

label = tk.Label(na, text="Please enter the number of messages you want to send:", font=("System", 12), bg=color_MidnightBlue, fg=color_White)
label.place(x=125, y=300)

# حاوية لعناصر الإدخال والقائمة المنسدلة
frame1 = tk.Frame(na, bg=color_Black)
frame1.place(x=180, y=350)

# إدخال النص
entry1 = tk.Entry(frame1, width=25, bg=color_MidnightBlue, fg=color_White)
entry1.grid(row=0, column=0, padx=5)

# قائمة الخيارات
options1 = ["1", "5", "10", "15", "20", "30", "40", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "2000", "4000", "6000", "8000", "10000", "20000", "50000", "100000", "500000", "1000000"]
selected_option1 = tk.StringVar()
selected_option1.set(options1[0])

# دالة لتحديث محتوى الـ entry الأول
def update_entry1(*args):
    entry1.delete(0, tk.END)
    entry1.insert(0, selected_option1.get())

selected_option1.trace('w', update_entry1)
dropdown1 = ttk.OptionMenu(frame1, selected_option1, *options1)
dropdown1.config(style='Custom.TMenubutton')
dropdown1.grid(row=0, column=1)

# إدخال النص للمدة الزمنية
label = tk.Label(na, text="Please enter the time interval between each message:", font=("System", 12), bg=color_MidnightBlue, fg=color_White)
label.place(x=130, y=390)

frame2 = tk.Frame(na, bg=color_Black)
frame2.place(x=180, y=440)

entry2 = tk.Entry(frame2, width=25, bg=color_MidnightBlue, fg=color_White)
entry2.grid(row=0, column=0, padx=5)

options2 = ["1", "0.1", "0.01", "0.001", "0.0001", "0.00001", "0.000001", "0.0000001", "0.00000001"]
selected_option2 = tk.StringVar()
selected_option2.set(options2[0])

def update_entry2(*args):
    entry2.delete(0, tk.END)
    entry2.insert(0, selected_option2.get())

selected_option2.trace('w', update_entry2)
dropdown2 = ttk.OptionMenu(frame2, selected_option2, *options2)
dropdown2.config(style='Custom.TMenubutton')
dropdown2.grid(row=0, column=1)

# إدخال النص للمدة الزمنية
label = tk.Label(na, text="Please enter the duration to wait before you start typing:", font=("System", 12), bg=color_MidnightBlue, fg=color_White)
label.place(x=125, y=490)

frame3 = tk.Frame(na, bg=color_Black)
frame3.place(x=180, y=540)

entry3 = tk.Entry(frame3, width=25, bg=color_MidnightBlue, fg=color_White)
entry3.grid(row=0, column=0, padx=5)

options3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
selected_option3 = tk.StringVar()
selected_option3.set(options3[0])

def update_entry3(*args):
    entry3.delete(0, tk.END)
    entry3.insert(0, selected_option3.get())

selected_option3.trace('w', update_entry3)
dropdown3 = ttk.OptionMenu(frame3, selected_option3, *options3)
dropdown3.config(style='Custom.TMenubutton')
dropdown3.grid(row=0, column=1)

# دالة إرسال الرسائل
def send_messages():
    message = entrye.get("1.0", tk.END).strip()
    num_times = int(entry1.get())
    interval_seconds = float(entry2.get())
    tim = float(entry3.get())

    def type_message():
        time.sleep(tim)
        for i in range(num_times):
            keyboard.write(message)
            keyboard.press_and_release("enter")
            time.sleep(interval_seconds)
            print(f"Message {i + 1}/{num_times} sent")

    threading.Thread(target=type_message).start()

# زر لبدء إرسال الرسائل
button = tk.Button(na, text="اضغط هنا", width=38, bg=color_MidnightBlue, fg=color_White, command=send_messages)
button.place(x=150, y=600)

# تشغيل الحلقة الرئيسية
na.mainloop()
