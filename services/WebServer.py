from flask import Flask, render_template, redirect, url_for, request, send_file
from MySQLHelper import setConfig, getConfig
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('index.html', cameraStatus = int(getConfig('camera_record')), accelerometerStatus = int(getConfig('accelerometer_record')))

@app.route("/setCamera")
def setCamera():
    status = request.args.get('status', default = 0)
    setConfig('camera_record', status) 
    return redirect(url_for('index'))
    

@app.route("/setAccelerometer")
def setAccelerometer():
    status = request.args.get('status', default = 0)
    setConfig('accelerometer_record', status) 
    return redirect(url_for('index'))

@app.route("/getLastCamera")
def getLastCamera():
    sortedFiles = sorted(os.listdir('camera'))
    return send_file("camera/" + sortedFiles[-1])


def main():
    # Debug False karena conflict dengan camera open cv
    app.run(host='0.0.0.0', port=8000, debug=False)
