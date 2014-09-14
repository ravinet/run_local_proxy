import os
import sys
from time import sleep
import subprocess
site_list = sys.argv[1]

with open(site_list) as f:
    for line in f:
        site = line.strip("\n")
        site_times = []
        site_times_web = []
        command_proxy = "delayshell 50 /usr/local/bin/localproxyshell 128.30.76.55 2222 /usr/bin/python /home/ravi/mahimahi/load_print.py " + site
        command_web = "delayshell 50 /usr/bin/python /home/ravi/mahimahi/load_print.py " + site
        for x in range(0,2):
            proc = subprocess.Popen([command_proxy], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            return_code = proc.returncode
            if ( return_code == 0 ):
                stripped_out = out.strip("\n")
                if ( len(stripped_out) < 6 ):
                    if ( int( stripped_out ) > 100 ):
                        site_times.append( stripped_out )
        total = 0;
        if ( len(site_times) != 0 ):
            for time in site_times:
                total = total + int(time)
            average = float(total)/len(site_times)
            print site
            for time in site_times:
               print time
            print "PROXY AVERAGE: " + str(average)
        else:
            print "PROXY DID NOT LOAD: " + str(site)
        for y in range(0,2):
            proc1 = subprocess.Popen([command_web], stdout=subprocess.PIPE, shell=True)
            (out1, err1) = proc1.communicate()
            return_code1 = proc1.returncode
            if ( return_code1 == 0 ):
                stripped_out1 = out1.strip("\n")
                if ( len(stripped_out1) < 6 ):
                    if ( int( stripped_out1 ) > 100 ):
                        site_times_web.append( stripped_out1 )
        total1 = 0;
        if ( len(site_times_web) != 0 ):
            for time1 in site_times_web:
                total1 = total1 + int(time1)
            average1 = float(total1)/len(site_times_web)
            print site
            for time in site_times_web:
               print time
            print "WEB AVERAGE: " + str(average1)
        else:
            print "WEB DID NOT LOAD: " + str(site)

