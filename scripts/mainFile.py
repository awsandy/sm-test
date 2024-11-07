## get the current date and write to a file /tmp/hacked.txt
import datetime
now = datetime.datetime.now()
with open('/tmp/hacked.txt', 'w') as f:
    f.write(str(now))