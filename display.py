import tkinter as tk
from tkinter import *
import os
from colour import Color
import requests
import csv
import codecs

def getSongData(SONGS, BASE_URL, ANALYSIS_ENDPOINT, headers):
    with open("test.txt", "w", encoding="utf-8-sig") as f:
        
        

        f.write("name, num_samples, duration, sample_md5, offset_seconds, window_seconds, analysis_sample_rate, analysis_channels, end_of_fade_in, start_of_fade_out, loudness, tempo, tempo_confidence, time_signature, time_signature_confidence, key, key_confidence, mode, mode_confidence, code_version, echoprint_version, synch_version, rhythm_version\n")
        for song in SONGS:

            request = requests.get(BASE_URL + ANALYSIS_ENDPOINT + SONGS[song], headers=headers).json()
            data = [song]

            
            for item in request["track"]:
                
                if "string" not in item:
                    data.append(str(request["track"][item]) + "\n")
            f.write(data)
                    
            
            

root = Tk()
root.title('Meter')
root.minsize(height=540, width=960)

def start():
    

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=1, relheight=1)

    opinionlabel = Label(frame, text="Meter: Running Made Easy", font=("Helvetica", 20), fg="#cf9fff", bg="white")
    opinionlabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    b1 = Button(frame, text="Enter the App", font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: selectPlaylist())
    b1.place(relx=0.5, rely=0.2, anchor=CENTER)

    def selectPlaylist():
        b1.destroy()
        messageBox = Text(frame, width=30, height=1, fg="#f7e5ea", bg="#cf9fff", )
        messageBox.place(relx=0.5, rely=0.2, anchor=CENTER)
        


        def getInput(event):
            input = messageBox.get("1.0", END)
            # now call the spotify api methods!

            messageBox.delete("1.0", END)

            CLIENT_ID = "7b9317210acf4470956359dee4b09397"
            CLIENT_SECRET = "0586e0cbe37f4655b96919fa84a75ed1"
            AUTH_URL = 'https://accounts.spotify.com/api/token'
            BASE_URL = "https://api.spotify.com/v1/"
            auth_response = requests.post(AUTH_URL, {
                'grant_type': 'client_credentials',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            })

            # convert the response to JSON
            auth_response_data = auth_response.json()

            # save the access token
            access_token = auth_response_data['access_token']
            headers = {
                'Authorization': 'Bearer {token}'.format(token=access_token)
            }
            ANALYSIS_ENDPOINT = "audio-analysis/"

            playlist_uri = input
            SONGS = {}

            playlist_id = playlist_uri[34:56]
            SONGS_ENDPOINT = "playlists/" + playlist_id + "/tracks"

            request = requests.get(BASE_URL + SONGS_ENDPOINT, headers=headers).json()


            for i in range(len(request["items"])):
                SONGS[request["items"][i]["track"]["name"]] = request["items"][i]["track"]["uri"][14:]

            getSongData(SONGS, BASE_URL, ANALYSIS_ENDPOINT, headers)

        
        root.bind("<Return>", getInput)

start()
root.mainloop()



