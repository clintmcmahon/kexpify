import kexp
import pytz, datetime
from datetime import timedelta
import time
###
### An example script that is run every Wednesday night to pull down the latest Roadhouse show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run
    #utc_datetime = datetime.datetime.utcnow()
    # datetime(year, month, day, hour, minute, second, microsecond)

    utc_datetime = datetime.datetime(2020, 10, 30)
    start_date = utc_datetime.strftime("%Y-%m-%dT08:00:00Z")
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        
    name = "Halloween!"
    description = "The ultimate Halloween playlist. Powered by KEXP.org."

    i = 1
    while(i <= 24):
        args = [name,start_date, end_date, description]
        kexp.main(args)
        i = i + 1
        start_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        end_date = (datetime.datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
        time.sleep(15)

