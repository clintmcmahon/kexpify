# encoding: utf-8

import sys
import pytz
import datetime
from datetime import timedelta
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

    for result in data['results']:
        if result['airdate'] is not None:
            airdate = datetime.datetime.strptime(result['airdate'], '%Y-%m-%dT%H:%M:%SZ')
            if start_date <= airdate <= end_date:
                if result['artist'] is not None:
                    artist = result['artist']['name']
                    track = result['track']['name'].replace("’", '').replace("'", '')
                                      
                    tracks.append({'artist': artist, 'song': track, 'airdate': airdate})
            
    return tracks    


def main(args):
    '''
    Main method
    '''
    if len(args) < 4:
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

        days_to_add = 0
        if len(args) > 4:
            days_to_add = args[4]

        #Create new Playlist object
        #Set this particular playlist properties
        #Send the playlist object into Spotify to create/update the latest
        playlist = Playlist()
        spotify = Spotify()
        playlist.name =  playlist_name
        playlist.description = playlist_description

        start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')   

        if days_to_add > 0:
            days_count = 0
            while days_count <= days_to_add:
                #Walk back for each day
                day_start = start + timedelta(days=-days_count)
                day_end = end + timedelta(days=-days_count)

                #Go to the end date and then come back
                #This is a terrible method but I have not figured out how the KEXP API really works yet
                uri = 'https://legacy-api.kexp.org/play/?limit=200&end_time=' + day_end.strftime("%Y-%m-%dT%H:%M:%SZ") + '&ordering=-airdate'
                playlist.tracks.extend(get_tracks(uri, day_start, day_end))

                days_count += 1
        else:
            #Go to the end date and then come back
            #This is a terrible method but I have not figured out how the KEXP API really works yet
            uri = 'https://legacy-api.kexp.org/play/?limit=200&end_time=' + end.strftime("%Y-%m-%dT%H:%M:%SZ") + '&ordering=-airdate'
            playlist.tracks = get_tracks(uri, start, end)
            
        playlist.tracks.sort(key=extract_time, reverse=False)
        spotify.create_playlist(playlist)

def extract_time(json):
    try:
        return json['airdate']
    except KeyError:
        return 0

if __name__ == '__main__':
     main(sys.argv[1:])