import tkinter as tk
import random

def generate_duties():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random.shuffle(a)

    b = int(entry_sem.get())
    d = int(entry_exams_per_day.get())
    f = int(entry_invigilator_1_class.get())
    g = int(entry_invigilator_2_class.get())
    h = int(entry_invigilator_3_class.get())

    e = b // d
    if b % 2 != 0:
        e = e + 1

    t = 0
    x1 = 0
    z1 = len(a)

    result_text.delete(1.0, tk.END)  

    for i in range(e):
        du = []
        du1 = []
        du2 = []
        ex = []
        random.shuffle(a)

        for m in range(d):
            du = []
            du1 = []
            du2 = []
            ex = []
            random.shuffle(a)

            if t == b:
                continue
            t = t + 1

            for j in range(f):
                du.append(a[x1])
                x1 = x1 + 1
                if x1 == z1:
                    random.shuffle(a)
                    x1 = 0

            for k in range(f):
                result_text.insert(tk.END, f"Duty for class {k+1} on day {i+1} and exam {m+1} is {du[k]}\n")

            for j in range(g):
                for p in range(2):
                    ex.append(a[x1])
                    x1 = x1 + 1
                    if x1 == z1:
                        random.shuffle(a)
                        x1 = 0
                du1.append(ex)
                ex = []

            for k in range(g):
                result_text.insert(tk.END, f"Duty for class {k+1} on day {i+1} and exam {m+1} is {du1[k]}\n")

            for j in range(h):
                for p in range(3):
                    ex.append(a[x1])
                    x1 = x1 + 1
                    if x1 == z1:
                        random.shuffle(a)
                        x1 = 0
                du2.append(ex)
                ex = []

            for k in range(h):
                result_text.insert(tk.END, f"Duty for class {k+1} on day {i+1} and exam {m+1} is {du2[k]}\n")

root = tk.Tk()
root.title("Exam Duty Generator")


input_frame = tk.Frame(root)
input_frame.pack()

label_sem = tk.Label(input_frame, text="Total no of exams for sem:")
label_sem.grid(row=0, column=0)
entry_sem = tk.Entry(input_frame)
entry_sem.grid(row=0, column=1)

label_exams_per_day = tk.Label(input_frame, text="No of exams per day:")
label_exams_per_day.grid(row=1, column=0)
entry_exams_per_day = tk.Entry(input_frame)
entry_exams_per_day.grid(row=1, column=1)

label_invigilator_1_class = tk.Label(input_frame, text="No of classes needing 1 invigilator:")
label_invigilator_1_class.grid(row=2, column=0)
entry_invigilator_1_class = tk.Entry(input_frame)
entry_invigilator_1_class.grid(row=2, column=1)

label_invigilator_2_class = tk.Label(input_frame, text="No of classes needing 2 invigilators:")
label_invigilator_2_class.grid(row=3, column=0)
entry_invigilator_2_class = tk.Entry(input_frame)
entry_invigilator_2_class.grid(row=3, column=1)

label_invigilator_3_class = tk.Label(input_frame, text="No of classes needing 3 invigilators:")
label_invigilator_3_class.grid(row=4, column=0)
entry_invigilator_3_class = tk.Entry(input_frame)
entry_invigilator_3_class.grid(row=4, column=1)


generate_button = tk.Button(root, text="Generate Duties", command=generate_duties)
generate_button.pack()


result_text = tk.Text(root, height=70, width=70)
result_text.pack(pady=10)  

root.mainloop()
