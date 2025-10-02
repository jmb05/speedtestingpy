from cfspeedtest import CloudflareSpeedtest
import os
import csv
import datetime

def run_test():
    suite = CloudflareSpeedtest()
    results = suite.run_all()
    tests = results['tests']
    time = tests['isp'].time
    latency = tests['latency'].value
    jitter = tests['jitter'].value
    h_down = tests['100kB_down_bps'].value
    o_down = tests['1MB_down_bps'].value
    t_down = tests['10MB_down_bps'].value
    q_down = tests['25MB_down_bps'].value
    np_down = tests['90th_percentile_down_bps'].value 
    h_up = tests['100kB_up_bps'].value
    o_up = tests['1MB_up_bps'].value
    t_up = tests['10MB_up_bps'].value
    np_up = tests['90th_percentile_up_bps'].value 
    return [time, latency, jitter, h_down, o_down, t_down, q_down, h_up, o_up, t_up, np_down, np_up]

def write_data(filename, data):
    with open(filename, 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        if os.path.getsize(filename) == 0:
            writer.writerow(['time','latency','jitter','100kB_down','1MB_down','10MB_down','25MB_down','100kB_up','1MB_up','10MB_up','90th_percentile_down','90th_percentile_up'])
        writer.writerow(data) 

now = datetime.datetime.now()
print("Starting speedtest " + now.strftime("%H:%M:%S"))
date = now.strftime("%d-%m-%Y")
filename_lan = 'results_' + date + '_lan.csv'
filename_wlan = 'results_' + date + '_wlan.csv'

lan_data = run_test()
write_data(filename_lan, lan_data)
#if os.system("/bin/bash /home/pi/speedtesting/disable_eth.sh") == 0:
#    print('Disabled ethernet')
#    wlan_data = run_test()
#    if os.system("/bin/bash /home/pi/speedtesting/enable_eth.sh") == 0:
#        print('Enabled ethernet')
#    else:
#        print('Error enabling ethernet')
#    write_data(filename_wlan, wlan_data)
#else:
#    print('Error disabling ethernet')


