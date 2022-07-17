from tkinter import Label, Button, font, Frame, Scrollbar, RIGHT, Text, BOTH, END

from ui.screen import Screen


class ManualScreen(Screen):
    ROUTENAME = "/manual"

    def onButtonClick(self):
        self._screenManager.navigate("/")

    def initBuild(self):
        self.time = None

        self.frame = Frame(width=1000, height=800)
        self.frame.place(x=0, y=0)

        LabelInstructions = Label(text="Anleitung",
                                  master=self.frame,
                                  fg="#265B78")
        LabelInstructions["font"] = font.Font(
            family='Arial', size=70, weight='bold')
        LabelInstructions.place(anchor="center", relx=0.5, rely=0.2)

        sBarFrame = Frame(master=self.frame)
        sBarFrame.place(relx=0.1, rely=0.3, width=800, height=400)

        sBar = Scrollbar(master=sBarFrame, orient="vertical")
        sBar.pack(side=RIGHT, fill="y")

        TxtInstructions = Text(master=sBarFrame, yscrollcommand=sBar.set)
        TxtInstructions.pack(expand=0, fill=BOTH)
        TxtInstructions["font"] = font.Font(family='Arial', size=16)

        TxtInstructions.insert(END, "Das Ziel des Spiels ist das der König des Gegners\n"
                                    "so angegriffen wird, dass dieser nicht mehr verteidigt\n"
                                    "werden kann. Somit würde er im nächsten Zug geschlagen\n"
                                    "werden. Das nett man dann matt. Der König ist also die\n"
                                    "wichtigste Figur beim Schach.\n\n"

                                    "Ein Schachbrett besteht aus 64 Feldern, schwarz und weiß.\n"
                                    "Ein Spieler hat die weißen Figuren, der andere die schwarzen.\n"
                                    "Weiß beginnt das Spiel. Es wird immer abwechselnd gezogen.\n\n"

                                    "Jeder Spieler hat acht Bauern, zwei Türme, zwei Springer,\n"
                                    "zwei Läufer, eine Dame und einen König. Die Bauern können nur gerade\n"
                                    "nach vorne bewegt werden - im ersten Zug über zwei Felder,\n"
                                    "ansonsten immer nur ein Feld. Er kann eine andere Figur schlagen,\n"
                                    "wenn er schräg zu einer gegnerischen Figur steht. In diesem Fall\n"
                                    "darf er dann auch schräg ziehen.\n\n"

                                    "Die Türme können sich in gerade Linie nach vorne, hinten oder\n"
                                    "zur Seite über beliebig viele Felder bewegen.\n\n"

                                    "Der Springer bewegt sich in einer besonderen Form:\n"
                                    "Zwei Felder nach vorne und dann eins zur Seite.\n"
                                    "Diese Bewegung kann er in alle vier Richtungen machen.\n\n"

                                    "Der Läufer kann sich nur schräg, dafür über beliebig\n"
                                    "viele Felder und in alle vier Richtungen bewegen.\n\n"

                                    "Die Dame darf in alle Richtungen gerade sowie auch\n"
                                    "schräg und über beliebig viele Felder gezogen werden.\n\n"

                                    "Der König kann sich immer nur ein Feld weit bewegen,\n"
                                    "dafür in alle Richtungen.\n\n"

                                    "Steht eine gegnerische Figur in der Zugbahn einer eigenen Figur,\n"
                                    "kann diese geschlagen und somit vom Brett genommen werden.\n"
                                    "Deshalb gilt es, seine Figuren zu decken, also so zu schützen,\n"
                                    "dass man die gegnerische Figur ebenfalls schlagen kann, sollte\n"
                                    "diese eine Figur schlagen.\n\n"

                                    "Beim Schach kommt es darauf an, strategisch zu denken.\n"
                                    "Es gilt nicht nur, die gegnerischen Figuren zu schlagen.\n"
                                    "Es gilt, den gegnerischen König so in Bedrängnis zu bringen,\n"
                                    "dass dieser nicht mehr ziehen kann. Wird der König durch eine\n"
                                    "Figur direkt bedroht, nennt man dies Schach. Kann er sich nicht\n"
                                    "mehr aus der Bedrohung retten, ist er matt.\n\n"

                                    "Dabei sollte nicht vergessen werden, den eigenen König so zu schützen,\n"
                                    "dass man nicht selbst matt gesetzt wird.")
        TxtInstructions.config(state="disabled")
        sBar.config(command=TxtInstructions.yview)

        ButtonPlay = Button(text="Zum Menü",
                            master=self.frame,
                            bg="#265B78",
                            activebackground="#265B78",
                            fg="#ffffff",
                            activeforeground="#ffffff",
                            command=self.onButtonClick,
                            borderwidth=0)
        ButtonPlay["font"] = font.Font(family='Arial', size=20, weight='bold')
        ButtonPlay.place(anchor="center", relx=0.5,
                         rely=0.9, width=210, height=80)

    def clear(self):
        self.frame.destroy()
