#listas operativos


import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      os_name = [y['name'] for y in x['os_image']]  
  print(",".join(map(str,os_name)))
else:
  print("Request failed with %s" % r.content)

## Asigna imagen según sistema operativo seleccionado

import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      image_url = [y['image_url'] for y in x['os_image'] if y['name'] == "@@{OS}@@"]  
  print(",".join(map(str,image_url)))
else:
  print("Request failed with %s" % r.content)


#qt version

import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      qt_version = [y['qt']['version'] for y in x['os_image'] if y['name'] == "@@{OS}@@"]  
  print(",".join(map(str,qt_version)))
else:
  print("Request failed with %s" % r.content)

#qt script url

import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      script_url = [y['qt']['script_url'] for y in x['os_image'] if y['name'] == "@@{OS}@@"]  
  print(",".join(map(str,script_url)))
else:
  print("Request failed with %s" % r.content)

#compiler

import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      compiler_name = [y['name'] for y in x['compilers']]  
  print(",".join(map(str,compiler_name)))
else:
  print("Request failed with %s" % r.content)

#compiler script url

import requests

r = requests.get("https://raw.githubusercontent.com/reymanreyman/scripts-navan/master/matrix.json")
if r.ok:
  resp = json.loads(r.content)
  for x in resp:
    if x['app_name'] == "@@{APPLICATION}@@":
      compiler_name = [y['name'] for y in x['compilers']]  
  print(",".join(map(str,compiler_name)))
else:
  print("Request failed with %s" % r.content)


