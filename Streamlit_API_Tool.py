import streamlit as st
import requests
from datetime import datetime
import re

# Set the title of the app
st.title('Find your energy label with ease!')

# Set the subtitle of the app
st.write('Get the energy performance of your house with our simple and easy-to-use tool. Enter your address and get the energy label, expiration date, type of house and house area. ')

# Add a link to the official website of the Dutch government
st.write("For more information about the energy label, visit the official website of the Dutch government: https://www.rijksoverheid.nl/onderwerpen/energielabel-woningen-en-gebouwen/energielabel-woning")

# Set the URL of the API - documentation: https://public.ep-online.nl/swagger/index.html 
url = "https://public.ep-online.nl/api/v3/PandEnergielabel/Adres"
headers = {
  'Authorization': 'Q0ZENzEzQzg2RkNCMTg4MzgzQzg3OTBFQTVCMUM4RTRGM0YwNjY0OTgwM0Y3NDU1QkYxNjFDQTc3MzA1NkQ4NDU1RTU0OTEzQjAyNTYyRDc5ODM4NTQ0RTk1QjNGMzQx',
  'Cookie': 'TS01ca2754=015d4243a6772bb3da8a5f78f1b22c0c7ba186ba1c22bc3f6491ffebf16e610157e542007c8af07ff5791ef6dd13050af4adbba6e0c45372d081625c6ea7f6965c0d32b41e; _gen-chocolate-chipped=!zMB6CzZW3uNuvmzxvUOWRoUeEVTDI5V9wK61GgOrCQUyQhvRB6T1dcFQ2wmQXt3R+m/z4moaKLMOfA=='
}

# Add input boxes for "postcode" and "huisnummer"
postcode = st.text_input('Postal code:')
huisnummer = st.text_input('House number:')
huisletter = st.text_input('House letter (optional):')
huisnummertoevoeging = st.text_input('House number addition (optional):')
detailaanduiding = st.text_input('Additional details (optional):')

# Create the params dictionary with the required parameters
params = {
    "postcode": postcode,
    "huisnummer": huisnummer
}

# Add the optional parameters to the params dictionary if they are not empty
if huisletter and re.match("^[a-zA-Z]{1}$",huisletter):
    params["huisletter"] = huisletter
if huisnummertoevoeging and re.match("^[a-zA-Z0-9]{4}$",huisnummertoevoeging):
    params["huisnummertoevoeging"] = huisnummertoevoeging
if detailaanduiding:
    params["detailaanduiding"] = detailaanduiding

# Check the format of the optional parameters
valid_huisletter = True
valid_huisnummertoevoeging = True
if huisletter:
    if not re.match("^[a-zA-Z]{1}$",huisletter):
        st.error("House letter format is invalid, you can't use special characters")
        valid_huisletter = False
if huisnummertoevoeging:
    if not re.match("^[a-zA-Z0-9]{4}$",huisnummertoevoeging):
        st.error("House number addition format is invalid, it should be max 4 characters long")
        valid_huisnummertoevoeging = False

# Send the GET request with the params dictionary
if st.button('Submit'):
    response = requests.request("GET", url, headers=headers, params=params)
    data = response.json()
    if type(data) == list:
        data = data[0]
    if data.get('labelLetter') is None:
        st.error("Energy label not available for this address")
        st.write("You can request a energy label at a certified energy performance company on this site: https://platform.centraalregistertechniek.nl/Vakbedrijven/Zoeken?t=Energie-advies")
    else:
        label_letter = data.get('labelLetter')
        valid_until = data.get('metingGeldigTot')
        valid_until = datetime.strptime(valid_until, "%Y-%m-%dT%H:%M:%S")
        valid_until = valid_until.strftime("%d/%m/%Y")
        building_type = data.get('gebouwtype')
        if 'gebruiksoppervlakte' in data:
            building_area = data.get('gebruiksoppervlakte')
        else:
            building_area = "not available"
    # Write the output
        st.write(f"Your energy label is: {label_letter}")
        st.write(f"Your label is valid until {valid_until}.")
        st.write(f"Your house type is: {building_type}")
        if building_area:
            st.write(f"Your house area is: {building_area} m2")
        else:
            st.write("Your house area is not available")


