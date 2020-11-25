from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

from chess_board import ChessBoard

tk = Tk()
tk.resizable(width=False, height=False)
tk.geometry("1000x800")


FrameInfo = Frame()
FrameInfo.place(relx=0, rely=0, width=200, height=800)

LabelRoundHeadline = Label(master=FrameInfo, text="Runde", fg="#265B78")
LabelRoundHeadline["font"] = font.Font(family='Arial', size=30, weight='bold')
LabelRoundHeadline.place(anchor="center", relx=0.5, rely=0.1)

LabelRoundNumber = Label(master=FrameInfo, text="6", fg="#265B78", bg="#ffffff")
LabelRoundNumber["font"] = font.Font(family='Arial', size=50)
LabelRoundNumber.place(anchor="center", relx=0.5, rely=0.18, width=85, height=85)

LabelColor1 = Label(master=FrameInfo, text="Es ist", fg="#265B78")
LabelColor1["font"] = font.Font(family='Arial', size=30, weight='bold')
LabelColor1.place(anchor="center", relx=0.5, rely=0.3)

LabelColor = Label(master=FrameInfo, fg="#265B78", bg="#ffffff")
LabelColor["font"] = font.Font(family='Arial', size=50)
LabelColor.place(anchor="center", relx=0.5, rely=0.38, width=85, height=85)

LabelColor2 = Label(master=FrameInfo, text="dran", fg="#265B78")
LabelColor2["font"] = font.Font(family='Arial', size=30, weight='bold')
LabelColor2.place(anchor="center", relx=0.5, rely=0.46)

arrowImage = ImageTk.PhotoImage(Image.open("IMG/arrow.png").resize((85, 85)), Image.ANTIALIAS)
ButtonBack = Button(master=FrameInfo, image=arrowImage,  borderwidth=0)
ButtonBack.place(anchor="center", relx=0.5, rely=0.78, width=85, height=85)

pauseImage = ImageTk.PhotoImage(Image.open("IMG/pause.png").resize((85, 85)), Image.ANTIALIAS)
ButtonPause = Button(master=FrameInfo, image=pauseImage, borderwidth=0)
ButtonPause.place(anchor="center", relx=0.5, rely=0.9, width=85, height=85)

FrameGrid = Frame()
FrameGrid.place(relx=0.2, rely=0, width=800, height=800)

ChessBoard(FrameGrid)




tk.mainloop()
