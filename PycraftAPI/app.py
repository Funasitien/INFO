from dreamlogger import *
from flask import Flask, render_template, redirect, request, flash, send_file
import random
import string
import requests
import io

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

debug_mode(True)
app = Flask(__name__)
app.secret_key = get_random_string(12)

http_proxy  = "http://guilhem.canis:Panda0404@172.16.0.253:3128"
https_proxy = "http://guilhem.canis:Panda0404@172.16.0.253:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

@app.route('/skin/<username>')
def getuserskin(username):
    uuid = requests.get(url=f"https://minecraft-api.com/api/uuid/{username}", proxies=proxies).content
    uuid = str(uuid)[2:-1]
    r = requests.get(url=f"https://crafatar.com/skins/{uuid}", proxies=proxies)
    if r.status_code == 200:
        # Create a BytesIO object from the response content
        image_data = io.BytesIO(r.content)
        # Send the image data as a file
        return send_file(image_data, mimetype='image/gif')
    else:
        print(r.status_code)
        print(r.content)
        # Handle the case where the request failed
        with open('steve.png', 'rb') as f:
            dummy_image_data = io.BytesIO(f.read())
        return send_file(dummy_image_data, mimetype='image/png')
    
@app.route('/cape/<username>')
def getusercape(username):
    uuid = requests.get(url=f"https://minecraft-api.com/api/uuid/{username}", proxies=proxies).content
    uuid = str(uuid)[2:-1]
    r = requests.get(url=f"https://crafatar.com/capes/{uuid}", proxies=proxies)
    if r.status_code == 200:
        # Create a BytesIO object from the response content
        image_data = io.BytesIO(r.content)
        # Send the image data as a file
        return send_file(image_data, mimetype='image/gif')
    else:
        print(r.status_code)
        print(r.content)
        # Handle the case where the request failed
        with open('cape.png', 'rb') as f:
            dummy_image_data = io.BytesIO(f.read())
        return send_file(dummy_image_data, mimetype='image/png')
    
app.run(port=5001)