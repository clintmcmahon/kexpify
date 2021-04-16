import kexp
import pytz, datetime
from datetime import timedelta

if __name__ == '__main__':
    #Seattle time
    start_date = '2020-12-25T05:00:00'

    #Seattle time
    end_date = '2020-12-25T23:59:00'
    
    name = "KEXP Christmas"
    description = "A Christmas playlist powered by KEXP.org"
    args = [name,start_date, end_date, description]
    kexp.main(args)

