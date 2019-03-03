import kexp
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Friday night to pull down the latest Swingin' Doors show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run
    utc_datetime = datetime.datetime.utcnow()

    #Swingin doors starts at 2 UTC time
    start_date = utc_datetime.strftime("%Y-%m-%dT02:00:00Z")

    #Swingin doors ends at 5 UTC time
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")

    name = "Swingin Doors On KEXP"
    description = "Don Slack's latest Swingin' Doors show on KEXP Seattle. Dedicated to a wide range of country sounds and styles, from honky tonk and western swing to alternative country and bluegrass. Updated every Thursday. Support the music and donate @ KEXP.org"
    args = [name,start_date, end_date, description]
    kexp.main(args)

