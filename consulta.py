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