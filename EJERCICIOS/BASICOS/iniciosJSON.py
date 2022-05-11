import json

citricos=["limon","naranja","pomelo","lima"]

citricosJSON=json.dumps(citricos)

print("Json de citricos",citricosJSON)

listacitricos= json.loads(citricosJSON)

print(listacitricos)



