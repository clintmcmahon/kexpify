import kexp
import pytz, datetime
from datetime import timedelta

if __name__ == '__main__':

   #This is being run at UTC Thursday morning so we check and go
    #back to the day the playlist is available
    today = datetime.datetime.today().weekday()
    if today == 0: 
      
      #Set the time zone to west coast Seattle
      tz = pytz.timezone('America/Los_Angeles')

      #Go back to Wednesday
      datetime_pacific =  datetime.datetime.now(tz) + datetime.timedelta(days=-1)
      
      #Sunday Soul starts at 6 PM Seattle time
      start_date = datetime_pacific.strftime('%Y-%m-%dT18:00:00')

      #Sunday Soul ends at 9 PM Seattle time
      end_date = datetime_pacific.strftime('%Y-%m-%dT21:00:00')

      name = "Sunday Soul on KEXP"
      description = "A playlist from the latest Sunday Soul show on KEXP Seattle. Updated every Sunday night. Support the music and donate @ KEXP.org"
      args = [name,start_date, end_date, description]
      kexp.main(args)
    else:
       print(f"Didn't run today, today is {datetime.datetime.today().weekday()}")

