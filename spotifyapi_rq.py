import requests
import csv

CLIENT_ID = "7b9317210acf4470956359dee4b09397"
CLIENT_SECRET = "0586e0cbe37f4655b96919fa84a75ed1"
AUTH_URL = 'https://accounts.spotify.com/api/token'

#POST
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

BASE_URL = "https://api.spotify.com/v1/"

# get tracks
playlist_id = "0CvNL96KydqsQ4wUakBvob"
SONGS_ENDPOINT = "playlists/" + playlist_id + "/tracks"

request = requests.get(BASE_URL + SONGS_ENDPOINT, headers=headers).json()

SONGS = {}
for i in range(len(request["items"])):
    SONGS[request["items"][i]["track"]["name"]] = request["items"][i]["track"]["uri"][14:]

# track info

ANALYSIS_ENDPOINT = "audio-analysis/"


print(["name", "num_samples", "duration", "sample_md5", "offset_seconds", "window_seconds", "analysis_sample_rate", "analysis_channels", "end_of_fade_in", "start_of_fade_out", "loudness", "tempo", "tempo_confidence", "time_signature", "time_signature_confidence", "key", "key_confidence", "mode", "mode_confidence", "code_version", "echoprint_version", "synch_version", "rhythm_version"])
for song in SONGS:

    request = requests.get(BASE_URL + ANALYSIS_ENDPOINT + SONGS[song], headers=headers).json()
    data = [song]
    for item in request["track"]:
        
        if "string" not in item:
            data.append(request["track"][item])
    print(data)




