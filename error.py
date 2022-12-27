import random
import sys
import  time
def  mengetik(s):
    for c in s + '\n':
        sys.stdout.write(s)
        sys.stdout.flush()

        time.sleep(random.random() * 0.9)

mengetik('jangan lupa mampir ke toko ya syamart & terimakasih.')
