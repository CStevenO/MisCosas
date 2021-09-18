"""import json
dic = {}
dic["Hola"] = "como estas"

with open("data.json","w") as fp:
    json.dump(dic,fp)

dic["como"] = "12312"

with open("data.json","w") as fp:
    json.dump(dic,fp)"""

from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()

print(now.date())
now = str(now)
now = now[now.index(" ")+1:].split(":")
hora = float(now[0]) + float(now[1])/60 + float(now[2])/3600
print(hora)


"""#Three lines to make our compiler able to draw:

import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt



x = ["APPLES", "BANANAS","peras"]
y = [400, 350,45]

plt.bar(x, y)
plt.savefig("prueba2.jpg")
plt.show()

"""
