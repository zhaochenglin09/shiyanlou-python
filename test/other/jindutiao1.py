import time
import sys
n = 10
for i in range(5):
    time.sleep(0.3)
    sys.stdout.write('\r')
    sys.stdout.write(str(i)*(n-i))
    sys.stdout.flush()
sys.stdout.write('\n')

