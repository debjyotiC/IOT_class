import urllib2
import json
import time

READ_API_KEY = 'HEY8K2J4IGVZIZ9J'
CHANNEL_ID = 475657


# get data from cloud
def get_data():
    connt_speak = urllib2.urlopen(
        "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (CHANNEL_ID, READ_API_KEY))
    response = connt_speak.read()
    data = json.loads(response)
    temp = data['field1']
    updated_at = data['created_at']
    data_str = "The sensor val:" + temp + " Last updated at:" + updated_at
    print data_str


def main():
    while True:
        get_data()
        time.sleep(10)


if __name__ == '__main__':
    main()
