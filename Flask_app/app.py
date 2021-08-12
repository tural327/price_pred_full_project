from flask import Flask,render_template,request
from chbox import my_res
import numpy as np
import pandas as pd
import pickle
loaded_model = pickle.load(open("prices_model.pickle", 'rb'))
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def Calculate():
  bmi =""
  bath = []
  smok = []
  A_C = []
  wifi_tv = np.zeros(3)
  wifi_tv1 = wifi_tv.tolist()
  hyd = np.zeros(4)
  hyd1 = hyd.tolist()
  type_home = np.zeros(4)
  type_home1 = type_home.tolist()
  z = np.zeros(4)
  j = z.tolist()
  car_park = []
  pet_fr = []
  bmi=""
  if request.method=="POST" and "size" in request.form and "Hydro" in request.form:
    hyd = np.zeros(4)
    if request.form.get("Hydro") =="All Utilities Included":
      hyd[0] = 1
    elif request.form.get("Hydro") =="Water Included":
      hyd[2] = 1
    elif request.form.get("Hydro") =="Not Included":
      hyd[1] = 1
    elif request.form.get("Hydro") =="Water and Heat Included":
      hyd[3] = 1
    if request.form.get("wifi")=="Cable / TV, Internet":
      wifi_tv[0] = 1
    elif request.form.get("wifi")=="Internet":
      wifi_tv[1] = 1
    elif request.form.get("wifi")=="Not Included":
      wifi_tv[2] = 1
    bed = np.zeros(4)
    if request.form.get("Bedrooms")=="single room":
      bed[0] = 1
    elif request.form.get("Bedrooms")=="2 rooms":
      bed[1] = 1
    elif request.form.get("Bedrooms")=="3 rooms":
      bed[2] = 1
    elif request.form.get("Bedrooms")=="Bachelor/Studio":
      bed[3] = 1
    if request.form.get("Bathrooms")=="1":
      bath.append(0)
    elif request.form.get("Bathrooms")=="1+":
      bath.append(1)
    if request.form.get("parking")=="One or more..":
      car_park.append(0)
    elif request.form.get("parking")=="No":
      car_park.append(1)
    if request.form.get("pet_yesno")=="Yes":
      pet_fr.append(0)
    if request.form.get("pet_yesno")=="No":
      pet_fr.append(1)
    if request.form.get("smoke_yesno")=="Yes":
      smok.append(0)
    elif request.form.get("smoke_yesno")=="No":
      smok.append(1)
    if request.form.get("ACyesno")=="Yes":
      A_C.append(0)
    if request.form.get("ACyesno")=="No":
      A_C.append(1)
    if request.form.get("hometype")=="Apartment":
      type_home[0] = 1
    elif request.form.get("hometype")=="Basement":
        type_home[1] = 1
    elif request.form.get("hometype")=="Condo":
        type_home[2] = 1
    elif request.form.get("hometype")=="House":
        type_home[3] = 1
    sz = float(request.form.get("size"))
    z = my_res()
    j = z.tolist()
  
    bmi = smok + A_C + pet_fr + car_park + [sz] + z.tolist() + bath +type_home.tolist() + bed.tolist()+wifi_tv.tolist() +hyd.tolist()
    my_y = pd.DataFrame(bmi).T
    bmi1 = loaded_model.predict(my_y)


    

  return render_template("index.html",bmi = bmi1)

if __name__=="__main__":
  app.run()