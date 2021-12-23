import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import pygame
import os
from colour import Color
from tkinter import Tk, Label
from pathlib import Path

root = Tk()
root.title('polarity')
root.iconbitmap(r'../polarity/resources/p.ico')
root.minsize(height=540, width=960)
issues = ["Abortion", "Gun Ownership", "LGBTQ Rights", "Tax Increases", "Vaccines"]
opinions = ["Strongly Against", "Against", "Neutral", "Support", "Strongly Support"]
numberValues = {
    "Strongly Against": -2,
    "Against": -1,
    "Neutral": 0,
    "Support": 1,
    "Strongly Support": 2
}
topic = {}
opinion = {}
messages = []
messageRecieved = False



def start():
    def stream():
        try:
            image = video.get_next_data()
            frame_image = Image.fromarray(image)
            l1.config(image=frame_image)
            l1.image = frame_image
            l1.after(delay, lambda: stream())
        except:
            video.close()
            return
    f1 = Frame()
    l1 = Label(f1)
    l1.pack()
    f1.pack()

    def opinionTab(currentTopic):
        topic[0] = currentTopic
        # we need to have the code recognize the user choice for topic and then have that be stored in the "topic" variable
        frame.destroy()
        frame1 = tk.Frame(root, bg="#f7e5ea")

        frame1.place(relwidth=1, relheight=1)
        n=0

        opinionlabel = Label(frame1, text="What Are Your Opinions on "+topic[0]+":", font=("Helvetica", 20,), fg="#cf9fff", bg="#f7e5ea",)
        photo5 = PhotoImage(file=r'resources/button (1).png')
        strongAgainst = Button(root, highlightthickness=0, bd=0, image=photo5,bg="#f7e5ea",command=lambda: waitingScreen(frame1, opinions[0]))
        strongAgainst.place(x=40, y=200)

        photo2 = PhotoImage(file=r'../polarity/resources/button (2).png')
        against = Button(root, highlightthickness=0, bg="#f7e5ea",bd=0, image=photo2,
                         command=lambda: waitingScreen(frame1, opinions[1]))
        against.place(x=40 + (180 * 1), y=200)

        photo1 = PhotoImage(file=r'resources/button (3).png')
        neutral = Button(root, highlightthickness=0, bd=0, image=photo1, bg="#f7e5ea",command=lambda: waitingScreen(frame1, opinions[2]))
        neutral.place(x=40 + (180 * 2), y=200)

        photo3 = PhotoImage(file=r'resources/button (4).png')
        support = Button(root, highlightthickness=0, bd=0, bg="#f7e5ea",image=photo3,
                         command=lambda: waitingScreen(frame1, opinions[3]))
        support.place(x=40 + (180 * 3), y=200)


        photo4 = PhotoImage(file=r'resources/button (5).png')
        strongSupport = Button(root, highlightthickness=0, bd=0, bg="#f7e5ea",image=photo4,
                         command=lambda: waitingScreen(frame1, opinions[4]))
        strongSupport.place(x=40 + (180 * 4), y=200)



        opinionlabel.pack(side=TOP)
        returnToStart = Button(frame1, text="Back", padx=10, pady=5, fg="#f7e5ea", bg="#cf9fff", command=start)
        returnToStart.place(x=0, y=0)

        mainloop()



    def waitingScreen(oldFrame, currentOpinion):
        

        opinion[0] = currentOpinion
        oldFrame.destroy()

        waitingFrame = Frame(root, bg="#f7e5ea")

        waitingFrame.place(relwidth=1, relheight=1)
        waitingLabel = Label(waitingFrame, text="Pairing you with a random person...", font=('Helvetica', 25),fg="#cf9fff", bg="#f7e5ea")

        waitingLabel.pack(side=TOP)

        cancelChat = Button(waitingFrame, text="Cancel", padx=10, pady=5, fg="#f7e5ea", bg="#cf9fff",
                                  command=lambda: opinionTab(topic[0]))
        cancelChat.place(x=0, y=0)

        def changeToChat(Content):
            waitingFrame.destroy()
            createChat(Content)

        WebSocket.bindToEvent("JoinedRoomEvent", changeToChat)



    def createChat(Content):
        chatFrame = Frame(root, bg="#f7e5ea")

        chatFrame.place(relwidth=1, relheight=1)

        chatLabel = Label(chatFrame, text="Discussion", font=('Helvetica', 25),fg="#cf9fff", bg="#f7e5ea")

        chatLabel.pack(side=TOP)

        exitChat = Button(chatFrame, text="Exit", padx=10, pady=5, fg="#f7e5ea", bg="#cf9fff", command=start)
        exitChat.place(x=0, y=50)

        returnToOpinions = Button(chatFrame, text="Back", padx=10, pady=5, fg="#f7e5ea", bg="#cf9fff", command=lambda: opinionTab(topic[0]))
        returnToOpinions.place(x=0,y=0)

        enterChat = Text(chatFrame, width=75, height=5, fg="#f7e5ea", bg="#cf9fff")
        enterChat.place(relx=0.5, rely=0.5, anchor='center', x=0, y=200, width=300, height=50)

        messageDisplay = Text(chatFrame, width=75, height=20, fg="#f7e5ea", bg="#cf9fff")
        messageDisplay.place(relx=0.5, rely=0.5, anchor='center', width=300, height=350)
        messageDisplay.config(state=DISABLED)

        scrollBar = Scrollbar(chatFrame, command=messageDisplay.yview)
        scrollBar.place(relx=0.5, rely=0.5, anchor='center', x=160, y=0, height=350)

        messageDisplay.configure(yscrollcommand = scrollBar.set)

        def retrieve_input(event):
            input = enterChat.get("1.0", "end-1c")
            messages.append(input)
            enterChat.delete("1.0", END)
            
            displayMessage(len(messages) - 1, messageDisplay)

        root.bind("<Return>", retrieve_input)

        def displayMessage(index, textBox):
            messageDisplay.config(state=NORMAL)
            textBox.insert(END, "You: " + messages[index])

        def newConversation(event):
           
            waitingScreen(chatFrame, opinion[0])

        def recieveMessage(Content):
            message = Content["message"]
            sender = Content["sender"]

            messageDisplay.insert(END, sender + ": " + message)

        root.bind("<Delete>", newConversation)
       

        # def sendMessage():





    frame = tk.Frame(root, bg="#f7e5ea")

    frame.place(relwidth=1, relheight=1)
    frame.tkraise()

    polarity = PhotoImage(file=r'../polarity/resources/polarity font.png')
    logo = Label(frame, highlightthickness=0, bd=0, image=polarity, bg="#f7e5ea")
    logo.place(x=(960/2)-(431/2), rely=0)

    label1 = Label(frame, text="Current Discussion Topics:",
                   font=("Verdana", 20), fg="#cf9fff", bg="#f7e5ea")

    label1.place(relx=0.31, y=350)

    issue1 = PhotoImage(file=r'../polarity/resources/babies.png')
    abortion = Button(root, highlightthickness=0, bd=0, image=issue1, bg="#f7e5ea", command=lambda: opinionTab(issues[0]))
    abortion.place(x=(570 - (len(issues) * 150) + (1 * 195)), y=400)

    issue2 = PhotoImage(file=r'../polarity/resources/guns.png')
    guns = Button(root, highlightthickness=0, bd=0, image=issue2, bg="#f7e5ea",command=lambda: opinionTab(issues[1]))
    guns.place(x=(570 - (len(issues) * 150) + (2 * 195)), y=400)

    issue3 = PhotoImage(file=r'../polarity/resources/lgbt.png')
    lgbt = Button(root, highlightthickness=0, bd=0, image=issue3,bg="#f7e5ea", command=lambda: opinionTab(issues[2]))
    lgbt.place(x=(570 - (len(issues) * 150) + (3 * 195)), y=400)

    issue4 = PhotoImage(file=r'../polarity/resources/tax.png')
    tax = Button(root, highlightthickness=0, bd=0, image=issue4, bg="#f7e5ea",command=lambda: opinionTab(issues[3]))
    tax.place(x=(570 - (len(issues) * 150) + (4 * 195)), y=400)

    issue5 = PhotoImage(file=r'../polarity/resources/vaccines.png')
    vaccines = Button(root, highlightthickness=0, bd=0, bg="#f7e5ea",image=issue5, command=lambda: opinionTab(issues[4]))
    vaccines.place(x=(570 - (len(issues) * 150) + (5 * 195)), y=400)

    mainloop()
    #stream()

start()

root.mainloop()