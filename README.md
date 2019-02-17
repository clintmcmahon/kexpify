# KEXPify

KEXPify is a Python library that hits the KEXP Legacy API to create a Spotify playlist for a given period in time.

### Prerequisites

Python3 (Python2 will require a couple code changes)

[Spotify account](https://www.spotify.com/us/signup/)

[Spotify API Credentials](https://developer.spotify.com/my-applications/#!/)


Spotipy
```
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
```

Requests
```
pip3 install requests
```

### Installing

Clone this repository

```
git clone https://github.com/clintmcmahon/kexpify
```

Change directory to kexpify

```
cd kexpify
```

Create a local_config.py file and populate with your values. Your file should look like this

```
#encoding: utf-8

SPOTIFY_USERNAME = [your Spotify username]
SPOTIFY_CLIENT_SECRET = [your Spotify API Client Secret]
SPOTIFY_CLIENT_ID = [your Spotify API Client ID]
SPOTIFY_SCOPE = 'playlist-modify-public playlist-modify-private playlist-read-collaborative'
SPOTIFY_REDIRECT_URI = 'http://localhost'
```

Run the code
```
python3 kexp.py [playlist_name] [start_date] [end_date] [playlist_description]
```
A browser window will automatically open where you will authenticate with Spotify. After you've given access to your Spotify account the browser will redirect to a http://localhost url. Copy the localhost url and paste it into the command line. You'll only need to do this once, the code will create a cache authentication file on your local machine.

After you've authenticated the program will use those cached credentials to read the playlist in your Spotify account, then either create a new playlist or delete the contents of the existing playlist before adding the latest tracks from the API.

## Built With

* [Spotify](http://www.spotify.com)
* [KEXP Seattle](http://kexp.org/donate)
* [Spotipy](https://github.com/plamere/spotipy)

## Acknowledgments

* KEXP Seattle - [Support Music That Matters - Donate today!](https://kexp.org/donate)
