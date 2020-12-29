from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

root = Tk()
root.title("Python & PostgreSQL")


def save_new_student(name, age, address):
    conect = psycopg2.connect(
        dbname="brxnvo1ptztruj5dlu6u",
        user="uvw2ekjvwszt9gfmxhk1",
        password="TEoA8uaYA1LJaRLMcw4u",
        host="brxnvo1ptztruj5dlu6u-postgresql.services.clever-cloud.com",
        port="5432",
    )
    cursor = conect.cursor()
    query = '''INSERT INTO students(name, age, address) VALUES (%s,%s,%s)'''
    cursor.execute(query, (name, age, address))
    print("Data Saved")
    conect.commit()
    conect.close()
    display_student()


def display_student():
    conect = psycopg2.connect(
        dbname="brxnvo1ptztruj5dlu6u",
        user="uvw2ekjvwszt9gfmxhk1",
        password="TEoA8uaYA1LJaRLMcw4u",
        host="brxnvo1ptztruj5dlu6u-postgresql.services.clever-cloud.com",
        port="5432",
    )
    cursor = conect.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox = Listbox(frame, height=20, width=5)
    listbox.grid(row=10, columnspan=4, stick=W+E)

    for x in row:
        listbox.insert(END, x)

    conect.commit()
    conect.close()


def search(id):
    conect = psycopg2.connect(
        dbname="brxnvo1ptztruj5dlu6u",
        user="uvw2ekjvwszt9gfmxhk1",
        password="TEoA8uaYA1LJaRLMcw4u",
        host="brxnvo1ptztruj5dlu6u-postgresql.services.clever-cloud.com",
        port="5432",
    )
    cursor = conect.cursor()
    query = '''SELECT * FROM students WHERE id=%s'''
    cursor.execute(query, (id))
    row = cursor.fetchone()
    search_result(row)
    for x in row:
        listbox.insert(END, x)
    conect.commit()
    conect.close()


def search_result(row):
    listbox = Listbox(frame, height=1, width=20)
    listbox.grid(row=9, columnspan=4, stick=W+E)
    listbox.insert(END, row)


# Canvas
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a student')
label.grid(row=0, column=1)

# Input Nombre
label = Label(frame, text='Name')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Input Edad
label = Label(frame, text='Age')
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Input Direccion
label = Label(frame, text='Adress')
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text='Save', command=lambda: save_new_student(
    entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1, sticky=W+E)

label = Label(frame, text='Search data')
label.grid(row=5, column=1)

label = Label(frame, text='Search by ID')
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text='Search', command=lambda: search(id_search.get()))
button.grid(row=6, column=2, sticky=W+E)


display_student()

root.mainloop()
