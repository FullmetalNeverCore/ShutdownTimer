import subprocess
print('0:Seconds')
print('1:Minutes')
minorsec = input('Want to use minutes or seconds? ')
if minorsec == '0':
    time = input('Type the time to shutdown in seconds: ')
    subprocess.call(["shutdown", "-s", "-t", time])
elif minorsec == '1':
    time = input('Type the time to shutdown in minutes: ')
    ntime = int(time) * 60
    subprocess.call("shutdown.exe -s -t " + str(ntime))
else:
    print('Error, Press just 0 or 1')
input('Press Enter to close: ') 