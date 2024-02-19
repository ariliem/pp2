import json
f = open('sample-data.json')
data = json.load(f)
f.close()

m = []

for i in data['imdata']:
    x = i['l1PhysIf']['attributes']
    m.append([x['dn'], x['descr'], x['speed'], x['mtu']])

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in m:
    print(f'{i[0]}         {i[1]}                     {i[2]}   {i[3]}')