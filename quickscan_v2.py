import streamlit as st
import requests
from datetime import datetime
import re

# Set the title of the app
st.title('Quick Scan :house:')

# Give a discription of the tool
st.subheader("Make a positive impact on the environment and save money with our sustainable home improvement scan.")
st.subheader("Powered by GreenHome")

"---"
# Set the header of the tool
st.header("Let's get started! :bulb: ")
st.header('Find your energy label with ease!')

# Give a discription of the energy label
st.subheader('Enter your address and get your energy label, expiration date, type of house and house area. ')

# Add a expander to explain this step in the quick scan tool
with st.expander("See explanation of the energy label"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

st.info('You can also choose to upload your energy label to add to the quick scan', icon="ℹ️")

# Create a file uploader widget
uploaded_file = st.file_uploader("upload your energy label here", type=["png", "jpg", "jpeg", "pdf"])

# Show the image if a file was uploaded
if uploaded_file is not None:
    st.image(uploaded_file, caption="Your energy label", use_column_width=True)

# Set the URL of the API - documentation: https://public.ep-online.nl/swagger/index.html 
url = "https://public.ep-online.nl/api/v3/PandEnergielabel/Adres"
headers = {
  'Authorization': 'Q0ZENzEzQzg2RkNCMTg4MzgzQzg3OTBFQTVCMUM4RTRGM0YwNjY0OTgwM0Y3NDU1QkYxNjFDQTc3MzA1NkQ4NDU1RTU0OTEzQjAyNTYyRDc5ODM4NTQ0RTk1QjNGMzQx',
  'Cookie': 'TS01ca2754=015d4243a6772bb3da8a5f78f1b22c0c7ba186ba1c22bc3f6491ffebf16e610157e542007c8af07ff5791ef6dd13050af4adbba6e0c45372d081625c6ea7f6965c0d32b41e; _gen-chocolate-chipped=!zMB6CzZW3uNuvmzxvUOWRoUeEVTDI5V9wK61GgOrCQUyQhvRB6T1dcFQ2wmQXt3R+m/z4moaKLMOfA=='
}

# Add input boxes for "postcode" and "huisnummer"
postcode = st.text_input('Postal code:')
if not postcode:
    st.error("Postal code is required")
huisnummer = st.text_input('House number:')
if not huisnummer:
    st.error("House number is required")
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

# Check if the required parameters are not empty and the optional parameters are valid
if postcode and huisnummer and valid_huisletter and valid_huisnummertoevoeging:
    st.success("You can go to the next step")

# Set up the year of built select box
year_of_built = st.selectbox("Select the year of built:", ["Till 1919", "1920-1945", "1946-1964", "1965-1974", "1975-1991", "1992-2005", "2006-2014", "2015-now"])
# Display the selected year of built
st.write("You have selected year of built:", year_of_built)

# Create a dictionary of options for each selectbox based on the "year of built" selection
options = {
    "Till 1919": {
        "wall_insulation": ["None"],
        "floor_insulation": ["None"],
        "flat_roof_insulation": ["None"],
        "slanted_roof_insulation": ["None"],
        "window_type_living": ["Single-glazing"],
        "window_type_bedrooms": ["Single-glazing"],
        "heating_system": ["Coal boiler"],
        "ventilation_type": ["Natural with grilles and windows"]
    },
    "1920-1945": {
        "wall_insulation": ["None"],
        "floor_insulation": ["None"],
        "flat_roof_insulation": ["None"],
        "slanted_roof_insulation": ["None"],
        "window_type_living": ["Single-glazing"],
        "window_type_bedrooms": ["Single-glazing"],
        "heating_system": ["Coal boiler"],
        "ventilation_type": ["Natural with grilles and windows"]
        },
    "1946-1964": {
        "wall_insulation": ["None"],
        "floor_insulation": ["None"],
        "flat_roof_insulation": ["None"],
        "slanted_roof_insulation": ["None"],
        "window_type_living": ["Single-glazing"],
        "window_type_bedrooms": ["Single-glazing"],
        "heating_system": ["Coal boiler"],
        "ventilation_type": ["Natural with grilles and windows"]
    },
    "1965-1974": {
        "wall_insulation": ["Reasonable 10cm - Rc 2,6"],
        "floor_insulation": ["Reasonable 10cm - Rc 2,4"],
        "flat_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
        "slanted_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
        "window_type_living": ["Single-glazing"],
        "window_type_bedrooms": ["Single-glazing"],
        "heating_system": ["Gas boiler"],
        "ventilation_type": ["Natural with grilles and windows"]
    },
    "1975-1991": {
        "wall_insulation": ["Reasonable 10cm - Rc 2,6"],
        "floor_insulation": ["Reasonable 10cm - Rc 2,4"],
        "flat_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
        "slanted_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
        "window_type_living": ["Double-glazing"],
        "window_type_bedrooms": ["Double-glazing"],
        "heating_system": ["Gas boiler"],
        "ventilation_type": ["Mechanical exhaust"]
    },
    "1992-2005": {
        "wall_insulation": ["Good 16cm - Rc 3,9"],
        "floor_insulation": ["Good 16cm - Rc 3,7"],
        "flat_roof_insulation": ["Good 16cm - Rc 4"],
        "slanted_roof_insulation": ["Good 17cm - Rc 4"],
        "window_type_living": ["HR++ glazing"],
        "window_type_bedrooms": ["HR++ glazing"],
        "heating_system": ["High-performance combi boiler"],
        "ventilation_type": ["Mechanical exhaust with CO2 control"]
    },
    "2006-2014": {
        "wall_insulation": ["Excellent 21cm - Rc 5"],
        "floor_insulation": ["Excellent 22cm - Rc 5"],
        "flat_roof_insulation": ["Excellent 26cm - Rc 6"],
        "slanted_roof_insulation": ["Excellent 26cm - Rc 6"],
        "window_type_living": ["Triple glazing"],
        "window_type_bedrooms": ["Triple glazing"],
        "heating_system": ["Hybrid heat pump"],
        "ventilation_type": ["Whole-house balanced ventilation with heat recovery"]
    },
    "2015-now": {
        "wall_insulation": ["Excellent 21cm - Rc 5"],
        "floor_insulation": ["Excellent 22cm - Rc 5"],
        "flat_roof_insulation": ["Excellent 26cm - Rc 6"],
        "slanted_roof_insulation": ["Excellent 26cm - Rc 6"],
        "window_type_living": ["Vacuum glass"],
        "window_type_bedrooms": ["Vacuum glass"],
        "heating_system": ["Ground source heat pump"],
        "ventilation_type": ["Ventilation unit with heat recovery in living room and master bedroom"]
    }
}

# Input section other informatio
st.title("Other information")
st.header("In this next step you have to select and fill in a couple of things about your home, in order to make the quick scan as complete as possible")

st.header("Roof")
# Add a select box for the type of roof
roof_type = st.selectbox("Select the type of roof you have:", ["Flat", "Slanted", "Flat and slanted"])
# Display the selected type of roof
st.write("You have selected:", roof_type, "roof")

# Add an input box for the area of the slanted roof
if roof_type == "Slanted":
    slanted_roof_area = st.selectbox("Enter the area of your roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
    st.write("The area of your roof is:", slanted_roof_area, "square meters")

# Add a select box for the area of the flat roof
if roof_type == "Flat":
    flat_roof_area = st.selectbox("Enter the area of your flat roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
    st.write("The area of your flat roof is:", flat_roof_area, "square meters")

# Add a select box for the area of the flat and slanted roof
if roof_type == "Flat and slanted":
    flat_roof_area = st.selectbox("Enter the area of your flat roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
    st.write("The area of your flat roof is:", flat_roof_area, "square meters")
    slanted_roof_area = st.selectbox("Enter the area of your slanted roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
    st.write("The area of your slanted roof is:", slanted_roof_area, "square meters")
"---"

st.header("Energy consumption and price")
# Add a input box for the consumption of gas
gas_consumption = st.number_input("Enter the annual consumption of gas from last year in m3:", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)

# Add a input box for the price of gas
gas_price = st.number_input("Enter the current price you pay for gas in €/m3:", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

# Add a input box for the consumption of electricity
electricity_consumption = st.number_input("Enter the annual consumption of electricity from last year in kWh:", min_value=0.0, max_value=10000.0, value=0.0, step=1.0)

# Add a input box for the price of electricity
electricity_price = st.number_input("Enter the current price you pay for electricity in €/kWh:", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

# Add a input box till when your energy contract last
end_date = st.date_input("Enter the date when your energy contract ends:")
st.write("Your energy contract ends on:", end_date)

"---"
st.header("Saving and generating energy")
# Add a select box for whether or not you have solar panels
solar_panels = st.selectbox("Do you have solar panels?", ["Yes", "No"])

# Check the value of solar_panels and display the select box for the type of input you want to give if "Yes" is selected
if solar_panels == "Yes":
    input_type = st.selectbox("Select the type of input you want to give:", ["Wattage peak of solar panels", "Amount of solar panels"])
    st.write("You have selected:", input_type, "as the type of input you want to give")

# Check the value of input_type and display the input box for the wattage peak of your solar panels if "Wattage peak of solar panels" is selected
    if input_type == "Wattage peak of solar panels":
        wattage_peak = st.number_input("Enter the wattage peak of your solar panels:")
        st.write("You have entered:", wattage_peak, "watts as the wattage peak of your solar panels")
# Check the value of input_type and display the input box for the amount of solar panels you have if "Amount of solar panels" is selected
    if input_type == "Amount of solar panels":
        amount_of_solar_panels = st.number_input("Enter the amount of solar panels you have:")
        st.write("You have entered:", amount_of_solar_panels, "solar panels")

# Add a select box for whether or not you have a solar boiler
solar_boiler = st.selectbox("Do you have a solar boiler?", ["Yes", "No"])
# Display the selected value
st.write("You have selected:", solar_boiler)

# Add a select box for whether or not you have a shower with heat recovery
shower_with_heat_recovery = st.selectbox("Do you have a shower with heat recovery?", ["Yes", "No"])
# Display the selected value
st.write("You have selected:", shower_with_heat_recovery)

"---"

#Prefilled section
st.title("This is the prefilled section")
st.header("In this last section, all items are prefilled based on the year of built.")
st.info('Please change if not correct!', icon="ℹ️")

st.subheader("Insulation")
# Use the selected "year of built" to get the prefilled options for each selectbox
wall_insulation = st.selectbox("Select the type of wall insulation you have:", options[year_of_built]["wall_insulation"])
st.write("You have selected:", wall_insulation, "wall insulation")

# Add a select box for the type of floor insulation
floor_insulation = st.selectbox("Select the type of floor insulation you have:", options[year_of_built]["floor_insulation"])
# Display the selected type of floor insulation
st.write("You have selected:", floor_insulation, "floor insulation")

# Check the value of roof_type and display the select box for the type of flat roof insulation if "flat" or "flat and slanted" is selected
if roof_type in ["Flat", "Flat and slanted"]:
    flat_roof_insulation = st.selectbox("Select the type of flat roof insulation you have:", options[year_of_built]["flat_roof_insulation"])
    st.write("You have selected:", flat_roof_insulation, "flat roof insulation")

# Check the value of roof_type and display the select box for the type of slanted roof insulation if "slanted" is selected
if roof_type in ["Slanted", "Flat and slanted"]:
    slanted_roof_insulation = st.selectbox("Select the type of slanted roof insulation you have:", options[year_of_built]["slanted_roof_insulation"])
    st.write("You have selected:", slanted_roof_insulation, "slanted roof insulation")

st.subheader("Windows")
# Add a select box for the type of window you have for living spaces
window_type_living = st.selectbox("Select the type of window you have for living spaces:", options[year_of_built]["window_type_living"])
# Display the selected type of window
st.write("You have selected:", window_type_living, "windows for living spaces")

# Add a select box for the type of window you have for bedrooms
window_type_bedrooms = st.selectbox("Select the type of window you have for bedrooms:", options[year_of_built]["window_type_bedrooms"])
# Display the selected type of window
st.write("You have selected:", window_type_bedrooms, "windows for bedrooms")

st.subheader("Heating and ventilation")
# Add a select box for the type of heating system you have for heating and warm water
heating_system = st.selectbox("Select the type of heating system you have for heating and warm water:", options[year_of_built]["heating_system"])
# Display the selected type of heating system
st.write("You have selected:", heating_system, "heating system")

# Add a select box for the type of ventilation you have
ventilation_type = st.selectbox("Select the type of ventilation you have:", options[year_of_built]["ventilation_type"])
# Display the selected type of ventilation
st.write("You have selected:", ventilation_type, "ventilation")

"---"

# Create a list of all the input box and select box variables
input_select_vars = [postcode, huisnummer, year_of_built, wall_insulation, floor_insulation, flat_roof_insulation, roof_type, window_type_bedrooms, heating_system, ventilation_type]

st.info('You can ignore the error message below. It will disappear when you click on the button to see your summary', icon="ℹ️") 

# Check if all the input boxes and select boxes are filled
if all(var is not None and var != "" for var in input_select_vars):
    st.success('Everything is filled in. You can now go to the next step to get a summary of your input', icon="✅")
 # Send the GET request with the params dictionary
    if st.button('Click here to see your summary'):
        response = requests.request("GET", url, headers=headers, params=params)
        data = response.json()
        if type(data) == list:
            data = data[0]
        if  data.get('labelLetter') is None:
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
        # # Write the output
        #     st.write(f"-Your energy label is: {label_letter} and is valid until {valid_until}. ")
        #     if building_area:
        #         st.write(f"-Your house type is: {building_type} and the area is: {building_area} m2")
        #     else:
        #         st.write(f"-Your house type is: {building_type} and the area is not available")
        #     st.write(f"-Roof type is: {roof_type}") 
        #     if roof_type in ["Flat", "Flat and slanted"]:
        #         st.write(f"-Flat roof insulation is: {flat_roof_insulation}")
        #     if roof_type in ["Slanted", "Flat and slanted"]:
        #         st.write(f"-Slanted roof insulation is: {slanted_roof_insulation}")  
        #     st.write(f"-Wall insulation is: {wall_insulation}")
        #     st.write(f"-Floor insulation is: {floor_insulation}")
        #     st.write(f"-Window type for living spaces is: {window_type_living}")
        #     st.write(f"-Window type for bedrooms is: {window_type_bedrooms}")
        #     st.write(f"-Heating system is: {heating_system}")
        #     st.write(f"-Ventilation type is: {ventilation_type}")
        #     st.write(f"-Year of built is: {year_of_built}")
        #     st.write(f"-Postcode is: {postcode}")
        #     st.write(f"-Huisnummer is: {huisnummer}")
            summary = "- Postcode is: " + postcode + "\n"
            summary += "- Huisnummer is: " + huisnummer + "\n"
            summary += "- Your energy label is: " + label_letter + " and is valid until " + valid_until + "\n"
            summary += "- Your house type is: " + building_type + "\n"
            if building_area:
                summary += "- The area of your house is: " + str(building_area) + " m2\n"
            else:
                summary += "- The area of your house is not available\n"
            summary += "- Roof type is: " + roof_type + "\n"
            if roof_type in ["Flat", "Flat and slanted"]:
                summary += "- Flat roof insulation is: " + flat_roof_insulation + "\n"
            if roof_type in ["Slanted", "Flat and slanted"]:
                summary += "- Slanted roof insulation is: " + slanted_roof_insulation + "\n"
            summary += "- Wall insulation is: " + wall_insulation + "\n"
            summary += "- Floor insulation is: " + floor_insulation + "\n"
            summary += "- Window type for living spaces is: " + window_type_living + "\n"
            summary += "- Window type for bedrooms is: " + window_type_bedrooms + "\n"
            summary += "- Heating system is: " + heating_system + "\n"
            summary += "- Ventilation type is: " + ventilation_type + "\n"
            summary += "- Year of built is: " + year_of_built + "\n"
        if data.get('labelLetter') is None:
            st.header("Type of house")
            # Set up the select box for the home type
            home_type = st.selectbox("Select the type of home you live in:", ["Detached", "Semi-detached", "Terraced", "Corner house"])
            # Display the entered type of house
            st.write("You have selected:", home_type)

            # Add an input box for the area
            area = st.selectbox("Select the area of your home (in square meters)", ["Less than 50m2", "50m2-100m2", "100m2-150m2", "150m2-200m2", "200m2-250m2", "250m2-300m2", "300m2-350m2","350m2-400m2","More than 400m2"])
            # Display the selected area
            st.write("You have selected:", area, "square meters")
else:
        st.error('Please fill in all the input boxes and select boxes')

# Create a string variable to hold the summary
# summary = "- Postcode is: " + postcode + "\n"
# summary += "- Huisnummer is: " + huisnummer + "\n"
# summary += "- Your energy label is: " + label_letter + " and is valid until " + valid_until + "\n"
# summary += "- Your house type is: " + building_type + "\n"
# if building_area:
#     summary += "- The area of your house is: " + str(building_area) + " m2\n"
# else:
#     summary += "- The area of your house is not available\n"
# summary += "- Roof type is: " + roof_type + "\n"
# if roof_type in ["Flat", "Flat and slanted"]:
#     summary += "- Flat roof insulation is: " + flat_roof_insulation + "\n"
# if roof_type in ["Slanted", "Flat and slanted"]:
#     summary += "- Slanted roof insulation is: " + slanted_roof_insulation + "\n"
# summary += "- Wall insulation is: " + wall_insulation + "\n"
# summary += "- Floor insulation is: " + floor_insulation + "\n"
# summary += "- Window type for living spaces is: " + window_type_living + "\n"
# summary += "- Window type for bedrooms is: " + window_type_bedrooms + "\n"
# summary += "- Heating system is: " + heating_system + "\n"
# summary += "- Ventilation type is: " + ventilation_type + "\n"
# summary += "- Year of built is: " + year_of_built + "\n"


# Check if all the input boxes and select boxes are filled
if all(var is not None and var != "" for var in input_select_vars):
    st.text(summary)
    st.download_button("Download summary", file_name="summary-of-my-home.txt", data=summary)
    
else:
    st.error('Please fill in all the input boxes and select boxes')






