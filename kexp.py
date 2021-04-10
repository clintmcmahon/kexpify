# encoding: utf-8

import sys
import pytz
import datetime
from datetime import timedelta
from spotify import Spotify
from playlist import Playlist
import json
import requests
from track import Track

def get_tracks(uri, start_date, end_date):
    '''
    Takes the playlist uri and returns the tracks played
    '''
    tracks = []
    response = requests.get(uri)
    data = response.json()
    print(uri)
    for result in data['results']:
        if 'artist' in result:
            artist = result['artist']
            song = result['song']
            airdate = result['airdate']
            tracks.append({'artist': artist, 'song': song, 'airdate': airdate})
    return tracks    

def main(args):
    '''
    Main method
    '''
    if len(args) < 3:
        print ("Please provide the necessary parameters ie kexp.py [playlist_name] [start_date] [end_date] [playlist_description]")
    else:
        #The name of the playlist you want to use in Spotify
        #If this playlist does not exist a new one with this name will be created
        #If this playlist exists it will be used
        playlist_name = args[0]
        
        #The start date time of the tracks you want to return. 
        #The KEXP API is in UTC format so make this date must be in the UTC format and timezone
        #Example: 2019-02-15T02:00:00Z
        start_date = args[1]

        #The end date time of the tracks you want to return. 
        #The KEXP API is in UTC format so make this date must be in the UTC format and timezone
        #Example: 2019-02-15T05:00:00Z
        end_date = args[2]

        #The description of the playlist you want to appear in Spotify
        playlist_description = args[3]

        #Create new Playlist object
        #Set this particular playlist properties
        #Send the playlist object into Spotify to create/update the latest
        playlist = Playlist()
        spotify = Spotify()
        playlist.name =  playlist_name
        playlist.description = playlist_description

        temp_tracks = []
        uri = f'https://api.kexp.org/v2/plays/?airdate_after={start_date}&airdate_before={end_date}&album=&album_exact=&artist=&artist_exact=&exclude_airbreaks=&has_comment=&host_ids=&label=&label_exact=&limit=2000&ordering=airdate&recording_id=&show_ids=&song=&song_exact='
        temp_tracks = get_tracks(uri, start_date, end_date)
        for temp_track in temp_tracks:
            if not any(x.airdate == temp_track['airdate'] for x in playlist.tracks):
                track = Track()
                track.artist = temp_track['artist']
                track.title = temp_track['song']
                track.airdate = temp_track['airdate']
                playlist.tracks.append(track)
    
        playlist.tracks.sort(key=extract_time, reverse=False)
        spotify.create_playlist(playlist)

def extract_time(json):
    try:
        return json.airdate
    except KeyError:
        return 0

if __name__ == '__main__':
     main(sys.argv[1:])