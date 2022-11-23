import time
import datetime

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

start = datetime.datetime.now()
start_timestamp = start.strftime(TIMESTAMP_FORMAT)

print("Started workflow: {}".format(start_timestamp))

time.sleep(300)

end = datetime.datetime.now()
end_timestamp = end.strftime(TIMESTAMP_FORMAT)

print("Ended workflow: {}".format(end_timestamp))