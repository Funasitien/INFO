from dreamlogger import *
from function import *
from flask import Flask, render_template, redirect, request, flash
import json
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

debug_mode(True)
app = Flask(__name__)
app.secret_key = get_random_string(12)

@app.route('/')
def index():
    return redirect('/candidats')

@app.route('/candidats')
def candidat():
    candidat = []
    file = open("candidat.txt", 'r')
    for line in file.readlines():
        candidat.append(line.replace('\n', ''))
        
    file.close()
    debug(candidat)
    return render_template('candidat.html', candidats=candidat)


@app.route('/vote/<voted>')
def vote(voted):
    if is_candidate(voted):
        # Opening JSON file
        f = open('vote.json', 'r+')
        # Reading from json file
        data = f.read()
        f.close()
        f = open('vote.json', 'w+')
        json_object = json.loads(data)
        debug(json_object)
        json_object[voted] = json_object[voted] + 1
        f.truncate(0)
        json.dump(json_object, f, indent=4)
        f.close()
        json_save(json_object)
        

        flash(f'Vous avez voté avec succès pour {voted}', 'success')
        return redirect('/candidats')
    
    return f"Le candidat {voted} n'existe pas", 400

@app.route('/admin/')
def admin():
    f = open('vote.json', 'r+')
    data = f.read()
    json_object = json.loads(data)
    return render_template('admin.html', result=json_object)

@app.route('/admin/reset')
def reset():
    if request.args.get('sure', '') == "true":
        candidat = []
        file = open("candidat.txt", 'r')
        for line in file.readlines():
            candidat.append(line.replace('\n', ''))
        
        data = {}
        for name in candidat:
            data[name] = 0
        
        f = open('vote.json', 'w+')
        json.dump(data, f, indent=4)
        flash(f'Les votes ont été réinitialisés.', 'error')
        return redirect('/admin')
    return "<h2><a href='/admin/reset?sure=true'>T'es sur mon pote ?</a></h2>"     

if __name__ == '__main__':
    app.run(debug=True)