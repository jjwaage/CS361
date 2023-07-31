from tkinter import *
from tkinter.font import Font
from tkmacosx import Button

root = Tk()
root.title("Guess The Word")
root.minsize(height = 750, width = 1000)
root.configure(background='white')


def start(): 
    def players():
        def name_1player():
            def length_of_word():
                name1_label.destroy()
                textbox.destroy()
                enter1_btn.destroy()
                back2_btn.destroy()

                length_label = Label(root, text = 'Select the length of word you would like to guess', font = ('Noteworthy', 45), background='white')
                length_label.pack(pady = 80)

                length1_btn = Button(root, text='4 - 6 Letters',  bg='#ffdbe9', fg = 'black', font = ('Noteworthy', 30))
                length1_btn.place(x=125, y = 300, height = 100, width = 200)

                length2_btn = Button(root, text='7 - 9 Letters',  bg='#afd5f0', fg = 'black', font = ('Noteworthy', 30))
                length2_btn.place(x=400, y = 300, height = 100, width = 200)

                length3_btn = Button(root, text='10+ Letters',  bg='#ddd5f3', fg = 'black', font = ('Noteworthy', 30))
                length3_btn.place(x=675, y = 300, height = 100, width = 200)

                def back3():
                    length_label.destroy()
                    length1_btn.destroy()
                    length2_btn.destroy()
                    length3_btn.destroy()
                    back3_btn.destroy()
                    name_1player()

                back3_btn = Button(root, text='Back',  bg='white', fg = 'black', font = ('Noteworthy', 20), command = back3)
                back3_btn.place(x=50, y = 650, height = 50, width = 100)
            
            player_label.destroy()
            one_player_btn.destroy()
            two_player_btn.destroy()
            back1_btn.destroy()

            name1_label = Label(root, text = 'Enter your name', font = ('Noteworthy', 50), background='white')
            name1_label.pack(pady = 40)

            textbox = Text(root, height = 1, width = 30, font = ('Noteworthy', 32))
            textbox.pack(pady = 60)

            enter1_btn = Button(root, text='Enter',  bg='light yellow', fg = 'black', font = ('Noteworthy', 20), command = length_of_word)
            enter1_btn.pack(pady = 20)

            def back2():
                name1_label.destroy()
                textbox.destroy()
                enter1_btn.destroy()
                back2_btn.destroy()
                players()

            back2_btn = Button(root, text='Back',  bg='white', fg = 'black', font = ('Noteworthy', 20), command = back2)
            back2_btn.place(x=50, y = 650, height = 50, width = 100)


        def name_2player():
            player_label.destroy()
            one_player_btn.destroy()
            two_player_btn.destroy()
            back1_btn.destroy()

            name1_label = Label(root, text = 'Enter Player 1\'s name', font = ('Noteworthy', 50), background='white')
            name1_label.pack(pady = 20)

            textbox = Text(root, height = 1, width = 30, font = ('Noteworthy', 32))
            textbox.pack(pady = 60)

            name2_label = Label(root, text = 'Enter Player 2\'s name', font = ('Noteworthy', 50), background='white')
            name2_label.pack(pady = 20)

            textbox2 = Text(root, height = 1, width = 30, font = ('Noteworthy', 32))
            textbox2.pack(pady = 60)

            enter1_btn = Button(root, text='Enter',  bg='light yellow', fg = 'black', font = ('Noteworthy', 20))
            enter1_btn.pack(pady = 20)

            def back3():
                name1_label.destroy()
                textbox.destroy()
                enter1_btn.destroy()
                back2_btn.destroy()
                name2_label.destroy()
                textbox2.destroy()
                players()

            back2_btn = Button(root, text='Back',  bg='white', fg = 'black', font = ('Noteworthy', 20), command = back3)
            back2_btn.place(x=50, y = 650, height = 50, width = 100)

        startlabel.destroy()
        start_btn.destroy()

        player_label = Label(root, text = 'How many players?', font = ('Noteworthy', 50), background='white')
        player_label.pack(pady = 40)

        one_player_btn = Button(root, text='One Player',  bg='light yellow', fg = 'black', font = ('Noteworthy', 30), command = name_1player)
        one_player_btn.place(x=200, y=300, height = 100, width =200)

        two_player_btn = Button(root, text='Two Players',  bg='#D1ffbd', fg = 'black', font = ('Noteworthy', 30), command = name_2player)
        two_player_btn.place(x=600, y=300, height = 100, width =200)

        def back1():
            player_label.destroy()
            one_player_btn.destroy()
            two_player_btn.destroy()
            back1_btn.destroy()
            start()

        back1_btn = Button(root, text='Back',  bg='white', fg = 'black', font = ('Noteworthy', 20), command = back1)
        back1_btn.place(x=50, y = 650, height = 50, width = 100)


    startlabel = Label(root, text = 'Guess the Word', font = ('Noteworthy', 75), background='white')
    startlabel.pack(pady = 40)

    start_btn = Button(root, text='Play',  bg='#afd5f0', fg = 'black', font = ('Noteworthy', 40), command = players, height = 100)
    start_btn.pack(pady = 250)


start()
root.mainloop()