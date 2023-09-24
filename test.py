from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

tag = PiicoDev_RFID()

string = 'Hello World!'

while True:
    data = tag.readText()
    print('Tag String: ' + str(data))

    sleep_ms(10)
