import Adafruit_DHT as dht
from flask import Flask

portNumber=81 #PORT THAT WILL BE USED 

app = Flask(__name__)
 
@app.route("/temp/")     #this  indicates the url, so this means server/temp/
def returntemp():
    h,t = dht.read_retry(dht.DHT22,4)    #Reads temp (and humidity)
    temp = (t*9)/5+32                    # Converts C to F
    tempf = str(temp)[:4]                # Converts number to string and trunca$
    return tempf
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=portNumber, debug=True)

