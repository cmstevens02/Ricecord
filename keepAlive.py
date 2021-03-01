from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Graphic Design is My Passion."

def run():
  app.run(host='0.0.0.0', port = 8000)

def keepAlive(): 
  t = Thread(target=run)
  t.start()