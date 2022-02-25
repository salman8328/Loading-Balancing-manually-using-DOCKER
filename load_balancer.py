import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')  # binds url to below logic
def get_data():
    global server32,server33
    loader()
    if server32 >= server33: # logic to load balance the backend servers!
        return requests.get('http://10.0.1.36:8080').content # always needs to return str value for a webpage.
    else:
        return requests.get('http://10.0.1.35:8080').content
      
      
@app.route("/load") #binds url ending with /load with below logic
def load():
    global server32,server33
    loader()
    ll = "load of server 32 " + str(server32) + "\n" + "load of server 33 " + str(server33)
    return ll
  
def loader(): # this function effectively fnds the loads on each back end server.
    global server32,server33
    server32 = str(requests.get('http://10.0.1.35:8080/load').content) # here add as many backend servers as needed.
    server33 = str(requests.get('http://10.0.1.36:8080/load').content)
    server33 = server33.split("'")  # we need float values to compare both of them, as str(1)<str(2) is not logical we need float(1)<float(2)!
    server33 = float(server33[1])
    server32 = server32.split("'")
    server32 = float(server32[1])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
