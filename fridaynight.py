import kexp
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Friday night to pull down the latest Friday Night with Michele Myers show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run
    utc_datetime = datetime.datetime.utcnow()

    #Friday Night starts at 2 UTC time
    start_date = utc_datetime.strftime("%Y-%m-%dT02:00:00Z")

    #Friday Night ends at 5 UTC time
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")

    name = "Friday Night With DJ Michele Myers On KEXP"
    description = "Michele Myer's latest Friday Night on KEXP Seattle. Spinning dance-worthy sets of electronic, soul, R&B, hip hop, rock and more. Updated every Friday night. Support the music, donate now @ KEXP.org"
    args = [name,start_date, end_date, description]
    kexp.main(args)

