import urllib.request
import sys
import time
import os

year_range = range(2010,2021)
month_range = range(1,13)
day_range = range(1,32)

def download():
    for year in year_range:
        os.makedirs("./{}".format(year),exist_ok=True)
        for month in month_range:
            for day in day_range:
                if not os.path.exists(("./{}/{:04}{:02}{:02}.lzh".format(year,year,month,day))):
                    try:
                        urllib.request.urlretrieve("http://www1.mbrace.or.jp/od2/K/{:04}{:02}/k{:02}{:02}{:02}.lzh".format(year,month,(year%100),month,day),"./{}/{:04}{:02}{:02}.lzh".format(year,year,month,day))
                        print("{:04}{:02}{:02}.lzh is downloaded !".format(year,month,day))
                    except Exception as e:
                        print(e)
                        print("http://www1.mbrace.or.jp/od2/K/{:04}{:02}/k{:02}{:02}{:02}.lzh is not found.".format(year,month,(year%100),month,day))
                else:
                    print("{}{:02}{:02}.lzh is aleady exist.".format(year,month,day))
        
download()