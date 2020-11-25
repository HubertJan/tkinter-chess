from tkinter import Frame, Button

class ChessBoard(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.place(relx=0.05, rely=0.025, width=768, height=768)
        # 1. COLUMN

        Button1x1 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button1x1.grid(row=0, column=0)

        Button2x1 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button2x1.grid(row=1, column=0)

        Button3x1 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button3x1.grid(row=2, column=0)

        Button4x1 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button4x1.grid(row=3, column=0)

        Button5x1 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button5x1.grid(row=4, column=0)

        Button6x1 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button6x1.grid(row=5, column=0)

        Button7x1 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button7x1.grid(row=6, column=0)

        Button8x1 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button8x1.grid(row=7, column=0)

        # 2. COLUMN

        Button1x2 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button1x2.grid(row=0, column=1)

        Button2x2 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button2x2.grid(row=1, column=1)

        Button3x2 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button3x2.grid(row=2, column=1)

        Button4x2 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button4x2.grid(row=3, column=1)

        Button5x2 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button5x2.grid(row=4, column=1)

        Button6x2 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button6x2.grid(row=5, column=1)

        Button7x2 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button7x2.grid(row=6, column=1)

        Button8x2 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button8x2.grid(row=7, column=1)

        # 3. COLUMN

        Button1x3 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button1x3.grid(row=0, column=2)

        Button2x3 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button2x3.grid(row=1, column=2)

        Button3x3 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button3x3.grid(row=2, column=2)

        Button4x3 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button4x3.grid(row=3, column=2)

        Button5x3 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button5x3.grid(row=4, column=2)

        Button6x3 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button6x3.grid(row=5, column=2)

        Button7x3 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button7x3.grid(row=6, column=2)

        Button8x3 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button8x3.grid(row=7, column=2)

        # 4. COLUMN

        Button1x4 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button1x4.grid(row=0, column=3)

        Button2x4 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button2x4.grid(row=1, column=3)

        Button3x4 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button3x4.grid(row=2, column=3)

        Button4x4 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button4x4.grid(row=3, column=3)

        Button5x4 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button5x4.grid(row=4, column=3)

        Button6x4 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button6x4.grid(row=5, column=3)

        Button7x4 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button7x4.grid(row=6, column=3)

        Button8x4 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button8x4.grid(row=7, column=3)

        # 5. COLUMN

        Button1x5 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button1x5.grid(row=0, column=4)

        Button2x5 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button2x5.grid(row=1, column=4)

        Button3x5 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button3x5.grid(row=2, column=4)

        Button4x5 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button4x5.grid(row=3, column=4)

        Button5x5 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button5x5.grid(row=4, column=4)

        Button6x5 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button6x5.grid(row=5, column=4)

        Button7x5 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button7x5.grid(row=6, column=4)

        Button8x5 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button8x5.grid(row=7, column=4)

        # 6. COLUMN

        Button1x6 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button1x6.grid(row=0, column=5)

        Button2x6 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button2x6.grid(row=1, column=5)

        Button3x6 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button3x6.grid(row=2, column=5)

        Button4x6 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button4x6.grid(row=3, column=5)

        Button5x6 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button5x6.grid(row=4, column=5)

        Button6x6 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button6x6.grid(row=5, column=5)

        Button7x6 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button7x6.grid(row=6, column=5)

        Button8x6 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button8x6.grid(row=7, column=5)

        # 7. COLUMN

        Button1x7 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button1x7.grid(row=0, column=6)

        Button2x7 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button2x7.grid(row=1, column=6)

        Button3x7 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button3x7.grid(row=2, column=6)

        Button4x7 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button4x7.grid(row=3, column=6)

        Button5x7 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button5x7.grid(row=4, column=6)

        Button6x7 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button6x7.grid(row=5, column=6)

        Button7x7 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button7x7.grid(row=6, column=6)

        Button8x7 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button8x7.grid(row=7, column=6)

        # 8. COLUMN

        Button1x8 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button1x8.grid(row=0, column=7)

        Button2x8 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button2x8.grid(row=1, column=7)

        Button3x8 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button3x8.grid(row=2, column=7)

        Button4x8 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button4x8.grid(row=3, column=7)

        Button5x8 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button5x8.grid(row=4, column=7)

        Button6x8 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button6x8.grid(row=5, column=7)

        Button7x8 = Button(master=self, bg="#417D9E",
                           activebackground="#417D9E", borderwidth=0, width=12, height=6)
        Button7x8.grid(row=6, column=7)

        Button8x8 = Button(master=self, bg="#90D4E9",
                           activebackground="#90D4E9", borderwidth=0, width=12, height=6)
        Button8x8.grid(row=7, column=7)

