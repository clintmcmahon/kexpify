import kexp
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Wednesday night to pull down the latest Roadhouse show from KEXP
###
if __name__ == '__main__':
    #Get the date this is being run
    #This is being run at central time on Wednesday night
    today = datetime.datetime.today().weekday()
    if today == 2: 
      
      #Set the time zone to west coast Seattle
      tz = pytz.timezone('America/Los_Angeles')
      datetime_pacific = datetime.datetime.now(tz)
      print("Date & Time in Seattle : ", 
        datetime_pacific.strftime('%Y-%m-%dT%H:%M:%SZ'))
      
      #Roadhouse starts at 7 PM Seattle time
      start_date = datetime_pacific.strftime('%Y-%m-%dT19:00:00Z')

      #Roudhouse ends at 10 PM Seattle time
      end_date = datetime_pacific.strftime('%Y-%m-%dT22:00:00Z')

      name = "The Roadhouse on KEXP"
      description = "A playlist from the latest Roadhouse show on KEXP Seattle. Updated every Wednesday night. Support the music and donate @ KEXP.org"
      args = [name,start_date, end_date, description]
      kexp.main(args)
    else:
       print(f"Didn't run today, today is {datetime.datetime.today().weekday()}")

