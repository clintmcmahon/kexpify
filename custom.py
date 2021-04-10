import kexp
import pytz, datetime
from datetime import timedelta

if __name__ == '__main__':

  
    #Seattle time
    start_date = '2020-11-04T05:00:00'

    #Seattle time
    end_date = '2020-11-04T23:59:00'
    
    name = "KEXP Election Day"
    description = "An election day playlist powered by KEXP.org"
    args = [name,start_date, end_date, description]
    kexp.main(args)

