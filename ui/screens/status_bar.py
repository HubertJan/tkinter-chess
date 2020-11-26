from tkinter import Frame, Label, font, Button
from PIL import ImageTk, Image


class StatusBar(Frame):
    def __init__(self, master):
        super().__init__(master)
        LabelRoundHeadline = Label(
            master=self, text="Runde", fg="#265B78")

        LabelRoundHeadline["font"] = font.Font(
            family='Arial', size=30, weight='bold')
        LabelRoundHeadline.place(anchor="center", relx=0.5, rely=0.1)

        LabelRoundNumber = Label(master=self, text="6",
                                 fg="#265B78", bg="#ffffff")
        LabelRoundNumber["font"] = font.Font(family='Arial', size=50)
        LabelRoundNumber.place(anchor="center", relx=0.5,
                               rely=0.18, width=85, height=85)

        LabelColor1 = Label(master=self, text="Es ist", fg="#265B78")
        LabelColor1["font"] = font.Font(family='Arial', size=30, weight='bold')
        LabelColor1.place(anchor="center", relx=0.5, rely=0.3)

        LabelColor = Label(master=self, fg="#265B78", bg="#ffffff")
        LabelColor["font"] = font.Font(family='Arial', size=50)
        LabelColor.place(anchor="center", relx=0.5,
                         rely=0.38, width=85, height=85)

        LabelColor2 = Label(master=self, text="dran", fg="#265B78")
        LabelColor2["font"] = font.Font(family='Arial', size=30, weight='bold')
        LabelColor2.place(anchor="center", relx=0.5, rely=0.46)


        self.arrowImage = ImageTk.PhotoImage(Image.open("IMG/arrow.png").resize((85, 85)), Image.ANTIALIAS)
        ButtonBack = Button(master=self, image=self.arrowImage,  borderwidth=0)
        ButtonBack.place(anchor="center", relx=0.5, rely=0.78, width=85, height=85)
        
        self.pauseImage = ImageTk.PhotoImage(Image.open("IMG/pause.png").resize((85, 85)), Image.ANTIALIAS)
        ButtonPause = Button(master=self, image=self.pauseImage, borderwidth=0)
        ButtonPause.place(anchor="center", relx=0.5, rely=0.9, width=85, height=85)
