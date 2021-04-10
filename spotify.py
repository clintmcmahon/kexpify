#! /usr/bin/env python3
# encoding: utf-8

import config
import spotipy
import spotipy.util as util

class Spotify(object):
    '''
    Spotify class connects up to the Spotify API via Spotipy
    '''
    def __init__(self):
        self.username = config.SPOTIFY_USERNAME
        self.app_client_secret = config.SPOTIFY_CLIENT_SECRET
        self.app_client_id = config.SPOTIFY_CLIENT_ID
        self.scope = config.SPOTIFY_SCOPE
        self.redirect_uri = config.SPOTIFY_REDIRECT_URI
        self.token = util.prompt_for_user_token(self.username,self.scope,client_id=self.app_client_id,client_secret=self.app_client_secret,redirect_uri=self.redirect_uri)
        self.spotify = spotipy.Spotify(auth=self.token)
        self.spotify.trace = False

    def create_playlist(self, playlist):
        '''
        Creates a Spotify playlist
        '''
        playlist_name = playlist.name
        playlist_description = playlist.description
        playlist_id = 0
        my_playlists = self.spotify.current_user_playlists()
        
        for i, my_playlist in enumerate(my_playlists['items']):
            if(playlist_name.lower() == my_playlist['name'].lower()):
                playlist_id = my_playlist['id']
                self.spotify.user_playlist_change_details(user=self.username, playlist_id=playlist_id, description=playlist_description)
                print('Using existing playlist', playlist_name)
                #print('Deleting existing tracks from playlist', playlist_name)
                #self.remove_tracks(playlist_id)
                break
        
        if playlist_id == 0:
            new_playlist = self.spotify.user_playlist_create(self.username, playlist_name, public=True, description=playlist_description)
            playlist_id = new_playlist['id']
            print('Created new playlist', playlist_name)
        
        print ('Building new playlist with id:', playlist_id)
        for track in playlist.tracks:
            artist = track.artist
            track = track.title
            self.add_track(artist, track, playlist_id)

        return playlist_id

    def add_track(self, artist, track, playlist_id):
        '''
        Adds a track to the specified Spotify playlist
        '''
        if self.token:
            q = 'artist:'+ artist + ' track:' + track
            print('Searching ', artist, '-', track)
            result = self.spotify.search(q, limit=1, offset=0, type='track', market=None)
           
            if result['tracks']['total'] > 0:
                uri = result['tracks']['items'][0]['uri']
                tracks = [
                    uri
                ]
                try:
                    add_results = self.spotify.user_playlist_add_tracks(self.username, playlist_id, tracks)
                    if add_results is None:
                        print('Unable to add track', track, 'by', artist)
                    else:
                        print('Successfully added track', track, 'by', artist)
                except self.ScrapeError as exception:
                    print(exception.args)
            else:
                print ("Unable to find", track, "by", artist)
        return None

    def remove_tracks(self, playlist_id):
        '''
        Remove tracks from the specified playlist_id parameter
        '''
        results = self.read_playlist(playlist_id)
        tracks = results['items']
        
        while results['next']:
            results = self.spotify.next(results)
            tracks.extend(results['items'])

        for track in tracks:
            #track_ids.append(track["track"]["id"])
            self.spotify.user_playlist_remove_all_occurrences_of_tracks(self.username, playlist_id, [track["track"]["id"]])

    def read_playlist(self, playlist_id):
        '''
        Returns a playlist defined by the playlist_id parameter
        '''
        return self.spotify.user_playlist_tracks(self.username, playlist_id)
    

    class ScrapeError(Exception):
        '''
        Passes errors
        '''
        pass