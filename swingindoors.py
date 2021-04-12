import kexp
import pytz, datetime
from datetime import timedelta

if __name__ == '__main__':

    #This is being run at UTC Friday morning so we check and go
    #back to the day the playlist is available
    today = datetime.datetime.today().weekday()
    if today == 4: 
      
      #Go back to Thursday
      now = datetime.datetime.now() + timedelta(days=-1)
      
      #Set the time zone to west coast Seattle
      tz = pytz.timezone('America/Los_Angeles')
      datetime_pacific = now(tz)
      print("Date & Time in Seattle : ", datetime_pacific.strftime('%Y-%m-%dT%H:%M:%SZ'))
      
      #Swingin Doors starts at 7 PM Seattle time
      start_date = datetime_pacific.strftime('%Y-%m-%dT19:00:00Z')

      #Swingin Doors ends at 10 PM Seattle time
      end_date = datetime_pacific.strftime('%Y-%m-%dT22:00:00Z')

      name = "Swingin Doors on KEXP"
      description = "A playlist from the latest Swingin Doors show on KEXP Seattle. Updated every Thursday night. Support the music and donate @ KEXP.org"
      args = [name,start_date, end_date, description]
      kexp.main(args)
    else:
       print(f"Didn't run today, today is {datetime.datetime.today().weekday()}")

