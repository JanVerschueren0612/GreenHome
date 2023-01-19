import requests

url = "https://public.ep-online.nl/api/v3/PandEnergielabel/Adres"

headers = {
  'Authorization': 'Q0ZENzEzQzg2RkNCMTg4MzgzQzg3OTBFQTVCMUM4RTRGM0YwNjY0OTgwM0Y3NDU1QkYxNjFDQTc3MzA1NkQ4NDU1RTU0OTEzQjAyNTYyRDc5ODM4NTQ0RTk1QjNGMzQx',
  'Cookie': 'TS01ca2754=015d4243a6772bb3da8a5f78f1b22c0c7ba186ba1c22bc3f6491ffebf16e610157e542007c8af07ff5791ef6dd13050af4adbba6e0c45372d081625c6ea7f6965c0d32b41e; _gen-chocolate-chipped=!zMB6CzZW3uNuvmzxvUOWRoUeEVTDI5V9wK61GgOrCQUyQhvRB6T1dcFQ2wmQXt3R+m/z4moaKLMOfA=='
}
postcode = "2967XH"
huisnummer = "58"

params = {
    "postcode": postcode,
    "huisnummer": huisnummer
}      
response = requests.request("GET", url, headers=headers, params=params)

print(response.text)
