from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

tag = PiicoDev_RFID()

string = 'Hello World!'

while True:
    result = tag.writeText(string)

    if result:
        data = tag.readText()
        print('String in tag: ' + str(data))
        break

    sleep_ms(10)
