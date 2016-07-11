from urllib import request, error
import datetime, sys, os, time


def getCurrentIP():
    try:
        urlRequest = request.Request("http://ip.42.pl/short")
        currentIP = request.urlopen(urlRequest).read().decode('utf-8', 'ignore')
        return currentIP
    except error.URLError:
        return 'No log entry at ' + getTime()
    except NameError:
        return 'No log entry at ' + getTime()
    

def getTime():
    logTime = str(datetime.datetime.now())
    return logTime[:16]


def fileCheck():
    if os.path.exists('ip_log5.txt'):
        return 'ip_log(latest).txt'
    if os.path.exists('ip_log4.txt'):
        return 'ip_log5.txt'
    if os.path.exists('ip_log3.txt'):
        return 'ip_log4.txt'
    if os.path.exists('ip_log2.txt'):
        return 'ip_log3.txt'
    if os.path.exists('ip_log.txt'):
        return 'ip_log2.txt'
    return 'ip_log.txt'


    
if __name__ == '__main__':
    
    changeTime = 'No Change'
    logFileName = fileCheck()
    logFile = open(logFileName, 'w+').close()
    
    try:
        logTime = sys.argv[1] # in hours
    except IndexError:
        logTime = 168   # 168 hours in a week

    try:
        logCheckTime = float(sys.argv[2]) # in minutes
    except IndexError:
        logCheckTime = 1800.0  # Check every 30 mins

    startIP = getCurrentIP()
    for x in range(0, (2 * int(logTime))):
        logFile = open(logFileName, 'a')
        currentIP = getCurrentIP()
        if currentIP.startswith('No'):
            logFile.write('Issue connecting to the internet at ' +
                          getTime() + '\n')                      
        else:
            if currentIP != startIP:
                if len(currentIP) < 16: # check if the website is only returning a 15 character ip address or the entire html text of the webpage
                    logFile.write('IP address changed at ' + getTime() +
                              ' from ' + startIP + ' to ' + currentIP + '\n')
                    if changeTime.startswith('No'):
                        changeTime = getTime()[11:] #TODO find times between changes
                        startIP = currentIP
                    else:
                        ipChangeDateTime = datetime.strptime(getTime(), "%Y-%m-%d %H:%M") - datetime.now()
                        ipChangeTime = (ipChangeDateTime.seconds) / 3600 # ip change time in hours
                        
        logFile.close()
        time.sleep(logCheckTime * 60.0) # 1800s = 30mins

    logFile = open(logFileName, 'a')
    logFile.write('Change time is ' + changeTime + '\n')
    logFile.write('Time between changes is ' + ipChangeTime)
    logFile.close()
