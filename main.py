# encoding: utf-8

import sys
import pytz
import datetime
from spotify import Spotify
from playlist import Playlist
import json
import requests

def get_tracks(uri, start_date, end_date):
    '''
    Takes the playlist uri and returns the tracks played
    '''
    tracks = []
            
    response = requests.get(uri)
    data = response.json()
    start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')
    
    for result in data['results']:
        if result['airdate'] is not None:
            airdate = datetime.datetime.strptime(result['airdate'], '%Y-%m-%dT%H:%M:%SZ')
            if start <= airdate <= end:
                if result['artist'] is not None:
                    artist = result['artist']['name']
                    track = result['track']['name'].replace("’", '').replace("'", '')
                    print (artist, '-', track)
                
                    tracks.append({'artist': artist, 'song': track})
            
    return tracks    


def main():
    '''
    Main method
    '''

    if len(sys.argv) < 4:
        print ("Please provide the necessary parameters ie main.py [playlist_name] [start_date] [end_date] [playlist_description]")
    else:
        #The name of the playlist you want to use in Spotify
        #If this playlist does not exist a new one with this name will be created
        #If this playlist exists it will be used
        playlist_name = sys.argv[1]
        
        #The start date time of the tracks you want to return. 
        #The KEXP API is in UTC format so make this date must be in the UTC format and timezone
        #Example: 2019-02-15T02:00:00Z
        start_date = sys.argv[2]

        #The end date time of the tracks you want to return. 
        #The KEXP API is in UTC format so make this date must be in the UTC format and timezone
        #Example: 2019-02-15T05:00:00Z
        end_date = sys.argv[3]

        #The description of the playlist you want to appear in Spotify
        playlist_description = sys.argv[4]

        #Go to the end date and then come back
        #This is a terrible method but I have not figured out how the KEXP API really works yet
        uri = 'https://legacy-api.kexp.org/play/?limit=200&end_time=' + end_date + '&ordering=-airdate'

        #Create new Playlist object
        #Set this particular playlist properties
        #Send the playlist object into Spotify to create/update the latest
        playlist = Playlist()
        spotify = Spotify()
        playlist.name =  playlist_name
        playlist.description = playlist_description
        playlist.tracks = get_tracks(uri, start_date, end_date)
        spotify.create_playlist(playlist)

if __name__ == '__main__':
    main()