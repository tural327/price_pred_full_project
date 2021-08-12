from flask import Flask,render_template,request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def my_res():
  result= np.zeros(4)
  if request.form.get('l') and request.form.get('u') and request.form.get('r') and request.form.get('t'):
    result[0] = 1
    result[1] = 1
    result[2] = 1
    result[3] = 1
  elif request.form.get('l') and request.form.get('u'):
    result[0] = 1
    result[1] = 1
    result[2] = 0
    result[3] = 0
  elif request.form.get('l') and request.form.get('t'):
    result[0] = 1
    result[1] = 0
    result[2] = 0
    result[3] = 1
  elif request.form.get('l') and request.form.get('r'):
    result[0] = 1
    result[1] = 0
    result[2] = 1
    result[3] = 0
  elif request.form.get('u') and request.form.get('r'):
    result[0] = 0
    result[1] = 1
    result[2] = 1
    result[3] = 0
  elif request.form.get('u') and request.form.get('t'):
    result[0] = 0
    result[1] = 1
    result[2] = 0
    result[3] = 1
  elif request.form.get('r') and request.form.get('t'):
    result[0] = 0
    result[1] = 0
    result[2] = 1
    result[3] = 1
  elif request.form.get('l'):
    result[0] = 1
    result[1] = 0
    result[2] = 0
    result[3] = 0
  elif request.form.get('u'):
    result[0] = 0
    result[1] = 1
    result[2] = 0
    result[3] = 0
  elif request.form.get('r'):
    result[0] = 0
    result[1] = 0
    result[2] = 1
    result[3] = 0
  elif request.form.get('t'):
    result[0] = 0
    result[1] = 0
    result[2] = 0
    result[3] = 1
  elif request.form.get('l') and request.form.get('u') and request.form.get('r'):
    result[0] = 1
    result[1] = 1
    result[2] = 1
    result[3] = 0
  elif request.form.get('u') and request.form.get('r') and request.form.get('t'):
    result[0] = 0
    result[1] = 1
    result[2] = 1
    result[3] = 1
  return result
