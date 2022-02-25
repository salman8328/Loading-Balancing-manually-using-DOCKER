from flask import Flask
import os
import socket
import psutil

app = Flask(__name__)
@app.route("/") # binds the url to below logic
def hello():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
  
@app.route("/load")  # binds the url which ends with /load with below logic
def load():
    return str(psutil.cpu_percent())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # always listens at port 8080.
