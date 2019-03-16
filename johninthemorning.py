import kexp
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Friday afternoon to pull down the latest week of John Richard's morning show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run 
    #This script will run on Friday mornings after the show has ended
    utc_datetime = datetime.datetime.utcnow()

    #John In The Morning starts at 14:00 (2pm) UTC time
    #Go back five days
    start_date = utc_datetime.strftime("%Y-%m-%dT14:00:00Z")
    
    #John In The Morning ends at 6 UTC time
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M:%SZ")

    #Get Monday - Friday
    days_to_add = 4

    #print (start_date)
    #print (end_date)
    name = "John In The Morning on KEXP"
    description = "The past week of John Richard's morning show on KEXP Seattle. Bringing a mix of alternative rock, hip hop, electronic, roots & blues, world, jazz and more. Updated every Friday. Support music that matters @ KEXP.org"
    args = [name, start_date, end_date, description, days_to_add]
    kexp.main(args)

