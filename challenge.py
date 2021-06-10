import json
import pandas as pd 

def testing(file):
    json_file=open(file)
    data = json.load(json_file)
    count=0
    for i in data:
        Index = i["WeightKg"] / (i["HeightCm"]/100.0)**2
        BMI=float("{0:.2f}".format(Index))
        i.update([("BMI",BMI)])
        if BMI == 18.4 and BMI<=24.9:
            i.update([('BMI Category', "Underweight"),("Health risk","Malnutrition risk")] )
        elif BMI <= 29.9:
            i.update([('BMI Category', "Normal weight"),("Health risk","Low risk")] )
        elif BMI <= 34.9:
            i.update([('BMI Category', "Overweight"),("Health risk","Enhanced risk")] )
            count = count+1;
        elif BMI <= 39.9:
            i.update([('BMI Category', "Moderately obese"),("Health risk","Medium risk")] )
        elif BMI == 40:
            i.update([('BMI Category', "Severely obese"),("Health risk","High risk")] )
        else:
            i.update([('BMI Category', "Very severely obese"),("Health risk","Very high risk")] )
    df = pd.DataFrame(data) 
    return("Overweight persons:"+ str(count))






