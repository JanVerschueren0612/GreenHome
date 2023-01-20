import streamlit as st
import requests
from datetime import datetime
import re


# Set the title of the app
st.title('Quick Scan :house:')

# Give a discription of the tool
st.subheader("Make a positive impact on the environment and save money with our sustainable home improvement scan.")
st.subheader("Powered by:")
st.image('images/logo.jpg')


"---"
#Step 1/3
with st.container():
    # Set the header of the tool
    st.header("Step 1/3: Find your energy label")

    # info balloon upload energy label
    st.image('images/step1.png')

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload here", type=["png", "jpg", "jpeg", "pdf"])

    # Show the image if a file was uploaded
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Your energy label", use_column_width=True)

    # Give a discription of the energy label
    st.subheader('Enter your address and get your energy label, expiration date, type of house and house area. ')
    st.warning("Warning: This tool is now only working when a energy label is available!")
   
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about energy label"):
        st.write("- The energy label of your home shows, among other things, how well your house is insulated. All about this energy label when buying, selling and renting your home.")
        st.write("- For more inforation, check this link: https://www.energielabel.nl")

    st.subheader("Required")
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
    st.subheader("Optional")    
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
    if st.button('Check your energy label'):
        response = requests.request("GET", url, headers=headers, params=params)
        data = response.json()
        if type(data) == list:
            data = data[0]
        if data.get('labelLetter') is None:
            st.error("Energy label not available for this address")
            st.write("You can request a energy label at a certified energy performance company on this site: https://platform.centraalregistertechniek.nl/Vakbedrijven/Zoeken?t=Energie-advies")
            # st.header("Type of house")
            # # Set up the select box for the home type
            # home_type = st.selectbox("Select the type of home you live in:", ["Detached", "Semi-detached", "Terraced", "Corner house"])
            # # Display the entered type of house
            # st.write("You have selected:", home_type)
            # # Add an input box for the area
            # area = st.text_input("Input the area of your home (in square meters)")
            # # Display the selected area
            # st.write("You have selected:", area, "square meters")
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
            st.success("Your input is saved! You can go to the next step.")    
    "---"

    st.header("Year of built")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("How to find your year of built?"):
        st.write("you can easily find more infomation about your home, including year of built by going to BAG Viewer: https://bagviewer.kadaster.nl/lvbag/bag-viewer/#")

    # Set up the year of built select box
    year_of_built = st.selectbox("Select the year of built:", ["Till 1919", "1920-1945", "1946-1964", "1965-1974", "1975-1991", "1992-2005", "2006-2014", "2015-now"])
    # # Display the selected year of built
    # st.write("You have selected year of built:", year_of_built)

    st.header("Roof")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about your roof"):
        st.write("- To calculate the area of your flat roof, you can visit this site: https://www.mapdevelopers.com/area_finder.php.")
        st.write("- And for more information about measuring your slanted roof, you can visit this site: https://nps-duurzaam.nl/blog/hoeveel-zonnepanelen-passen-op-mijn-dak/")

    # Add a select box for the type of roof
    roof_type = st.selectbox("Select the type of roof you have:", ["Flat and slanted","Flat", "Slanted"])
    # # Display the selected type of roof
    # st.write("You have selected:", roof_type, "roof")

    # Add an input box for the area of the slanted roof
    if roof_type == "Slanted":
        slanted_roof_area = st.selectbox("Enter the area of your roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
        # st.write("The area of your roof is:", slanted_roof_area, "square meters")

    # Add a select box for the area of the flat roof
    if roof_type == "Flat":
        flat_roof_area = st.selectbox("Enter the area of your flat roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
        # st.write("The area of your flat roof is:", flat_roof_area, "square meters")

    # Add a select box for the area of the flat and slanted roof
    if roof_type == "Flat and slanted":
        flat_roof_area = st.selectbox("Enter the area of your flat roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
        # st.write("The area of your flat roof is:", flat_roof_area, "square meters")
        slanted_roof_area = st.selectbox("Enter the area of your slanted roof (in square meters)", ["Less than 15m2","15m2 - 20m2","20m2 - 25m2","25m2 - 30m2","30m2 - 35m2","35m2 - 40m2","40m2 - 45m2","45m2 - 50m2","More than 50m2"])
        # st.write("The area of your slanted roof is:", slanted_roof_area, "square meters")

#Dictionary for year of built
with st.container():
    # Create a dictionary of options for each selectbox based on the "year of built" selection
    options = {
        "Till 1919": {
            "wall_insulation": ["None"],
            "floor_insulation": ["None"],
            "flat_roof_insulation": ["Reasonable 10cm - Rc 2,6"],
            "slanted_roof_insulation": ["Bad 3cm - Rc 0,9"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Natural with grilles and windows"]
        },
        "1920-1945": {
            "wall_insulation": ["None"],
            "floor_insulation": ["None"],
            "flat_roof_insulation": ["Reasonable 10cm - Rc 2,6"],
            "slanted_roof_insulation": ["Bad 3cm - Rc 0,9"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Natural with grilles and windows"]
            },
        "1946-1964": {
            "wall_insulation": ["None"],
            "floor_insulation": ["None"],
            "flat_roof_insulation": ["Reasonable 10cm - Rc 2,6"],
            "slanted_roof_insulation": ["Bad 3cm - Rc 0,9"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Natural with grilles and windows"]
        },
        "1965-1974": {
            "wall_insulation": ["None"],
            "floor_insulation": ["None"],
            "flat_roof_insulation": ["Bad 3cm - Rc 0,9"],
            "slanted_roof_insulation": ["Bad 3cm - Rc 0,9"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Natural with grilles and windows"]
        },
        "1975-1991": {
            "wall_insulation": ["Poor 7cm - Rc 1,9"],
            "floor_insulation": ["Poor 5cm - Rc 1,3"],
            "flat_roof_insulation": ["Poor 5cm - Rc 1,3"],
            "slanted_roof_insulation": ["Poor 5cm - Rc 1,3"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Natural with grilles and windows"]
        },
        "1992-2005": {
            "wall_insulation": ["Reasonable 10cm - Rc 2,6"],
            "floor_insulation": ["Reasonable 10cm - Rc 2,4"],
            "flat_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
            "slanted_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
            "window_type_living": ["Double-glazing"],
            "window_type_bedrooms": ["Double-glazing"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Mechanical ventilation"]
        },
        "2006-2014": {
            "wall_insulation": ["Reasonable 10cm - Rc 2,6"],
            "floor_insulation": ["Reasonable 10cm - Rc 2,4"],
            "flat_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
            "slanted_roof_insulation": ["Reasonable 10cm - Rc 2,4"],
            "window_type_living": ["HR++ glass"],
            "window_type_bedrooms": ["HR++ glass"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Mechanical ventilation"]
        },
        "2015-now": {
            "wall_insulation": ["Good 16cm - Rc 3,9"],
            "floor_insulation": ["Good 16cm - Rc 3,7"],
            "flat_roof_insulation": ["Good 17cm - Rc 4"],
            "slanted_roof_insulation": ["Good 17cm - Rc 4"],
            "window_type_living": ["HR++ glass"],
            "window_type_bedrooms": ["HR++ glass"],
            "heating_system": ["High-performance combi boiler"],
            "ventilation_type": ["Mechanical ventilation"]
        }
    }

"---"

#Step 2/3
with st.container():
    st.title("Step 2/3: Check prefilled items")
    
    # info balloon upload energy label
    st.image('images/step2.png')

    st.header("Insulation")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about wall insulation"):
        st.write("- You can find information about your facade insulation in a purchase brochure, an architectural report, your home's energy label or invoices from renovations. Or check the facade of your home yourself.")
        st.write("- More information is this PDF from MilieuCentraal: https://www.milieucentraal.nl/media/mholxybf/hoe-check-ik-mijn-gevelisolatie.pdf")
    # Use the selected "year of built" to get the prefilled options for each selectbox
    wall_insulation = st.selectbox("Select the type of wall insulation you have:", options[year_of_built]["wall_insulation"])
    # st.write("You have selected:", wall_insulation, "wall insulation")


    # Add a select box for the type of floor insulation
    with st.expander("Info about floor insulation"):
        st.write("- You can find information about your floor insulation on this site: https://www.milieucentraal.nl/energie-besparen/isoleren-en-besparen/vloerisolatie/")
    floor_insulation = st.selectbox("Select the type of floor insulation you have:", options[year_of_built]["floor_insulation"])


    # Check the value of roof_type and display the select box for the type of flat roof insulation if "flat" or "flat and slanted" is selected
    with st.expander("Info about roof insulation"):
          st.write("- You can find information about your floor insulation on this site: https://www.milieucentraal.nl/media/zebh5elt/hoe-check-ik-mijn-dakisolatie.pdf")
    if roof_type in ["Flat", "Flat and slanted"]:
        flat_roof_insulation = st.selectbox("Select the type of flat roof insulation you have:", options[year_of_built]["flat_roof_insulation"])


    # Check the value of roof_type and display the select box for the type of slanted roof insulation if "slanted" is selected
    with st.expander("Info about roof insulation"):
        st.write("- You can find information about your floor insulation on this site: https://www.milieucentraal.nl/media/zebh5elt/hoe-check-ik-mijn-dakisolatie.pdf")
    if roof_type in ["Slanted", "Flat and slanted"]:
        slanted_roof_insulation = st.selectbox("Select the type of slanted roof insulation you have:", options[year_of_built]["slanted_roof_insulation"])

    st.header("Windows")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about windows"):
        st.write("You can find information about your windows on this site: https://www.milieucentraal.nl/tests-en-tools/check-je-ramen/")

    # Add a select box for the type of window you have for living spaces
    window_type_living = st.selectbox("Select the type of window you have for living spaces:", options[year_of_built]["window_type_living"])

    # Add a select box for the type of window you have for bedrooms
    window_type_bedrooms = st.selectbox("Select the type of window you have for bedrooms:", options[year_of_built]["window_type_bedrooms"])

    st.header("Heating and ventilation")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("info about heating and ventilation"):
        st.write("- You can find more information about heating systems on this site: https://support.google.com/googlenest/answer/9242116?hl=nl")
        st.write("- You can find more information about ventilation systems on this site: https://www.milieucentraal.nl/energie-besparen/ventilatie/")

    # Add a select box for the type of heating system you have for heating and warm water
    heating_system = st.selectbox("Select the type of heating system you have for heating and warm water:", options[year_of_built]["heating_system"])
    # Display the selected type of heating system
    # st.write("You have selected:", heating_system, "heating system")

    # Add a select box for the type of ventilation you have
    ventilation_type = st.selectbox("Select the type of ventilation you have:", options[year_of_built]["ventilation_type"])
    # Display the selected type of ventilation
    # st.write("You have selected:", ventilation_type, "ventilation")

"---"

#Step 3/3
with st.container():
    st.title("Step 3/3: Additional information")
        
    # info balloon upload energy label
    st.image('images/step3.png')

    st.header("Energy consumption and price")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about energy consumption and price"):
        st.write("- You can find information about your energy consumption and price on your energy bill.")
        st.write("- For more information about your energy consumption, you can visit this site: https://www.milieucentraal.nl/energie-besparen/inzicht-in-je-energierekening/gemiddeld-energieverbruik/.")

    # Add a input box for the consumption of gas
    gas_consumption = st.number_input("Enter the annual consumption of gas from last year in m3:", min_value=0.0, max_value=10000.0, value=2000.0, step=1.0)
    if not gas_consumption:
        st.error("Gas consumption is required")
    # Add a input box for the price of gas
    gas_price = st.number_input("Enter the current price you pay for gas in €/m3:", min_value=0.0, max_value=100.0, value=2.70, step=0.1)
    if not gas_price:
        st.error("Gas price is required")
    # Add a input box for the consumption of electricity
    electricity_consumption = st.number_input("Enter the annual consumption of electricity from last year in kWh:", min_value=0.0, max_value=100000.0, value=3700.0, step=1.0)
    if not electricity_consumption:
        st.error("Electricity consumption is required")
    # Add a input box for the price of electricity
    electricity_price = st.number_input("Enter the current price you pay for electricity in €/kWh:", min_value=0.0, max_value=100.0, value=0.75, step=0.1)
    if not electricity_price:
        st.error("Electricity price is required")

    # Add a input box till when your energy contract last
    end_date = st.date_input("Enter the date when your energy contract ends:")
    if not end_date:
        st.error("End date is required")

    # st.write("Your energy contract ends on:", end_date)

    "---"
    st.header("Saving and generating energy")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("info about generating energy"):
        st.write("- You can find more information about solar panels on this site: https://www.milieucentraal.nl/energie-besparen/zonnepanelen/")
        st.write("- Is your roof suitable for solar panels, check this site: https://www.zonatlas.nl/start/")
        st.write("- You can find more information about wind turbines on this site: https://www.milieucentraal.nl/energie-besparen/windenergie/")
        st.write("- You can find more information about heat pumps on this site: https://www.milieucentraal.nl/energie-besparen/warmtepomp/")
        st.write("- You can find more information about heat recovery on this site: https://www.milieucentraal.nl/energie-besparen/energiezuinig-ventileren/")
        st.write("- You can find more information about solar thermal panels on this site: https://www.milieucentraal.nl/energie-besparen/zonneboiler/")
        st.write("- You can find more information about biomass boilers on this site: https://www.milieucentraal.nl/energie-besparen/houtkachel/")
        st.write("- You can find more information about little adjustments to save energy on this site: https://zetookdeknopom.nl/?utm_campaign=ezk-energie-maatregelen-04-2022&utm_medium=search&utm_source=google&utm_content=ros-search-alg&utm_term=searchad-multi-device-cpc-performance")
  
    # Add a select box for whether or not you have solar panels
    solar_panels = st.selectbox("Do you have solar panels?", ["No","Yes"])

    # Check the value of solar_panels and display the select box for the type of input you want to give if "Yes" is selected
    if solar_panels == "Yes":
        input_type = st.selectbox("Select the type of input you want to give:", ["Wattage peak of solar panels", "Amount of solar panels"])
        # st.write("You have selected:", input_type, "as the type of input you want to give")

    # Check the value of input_type and display the input box for the wattage peak of your solar panels if "Wattage peak of solar panels" is selected
        if input_type == "Wattage peak of solar panels":
            wattage_peak = st.number_input("Enter the wattage peak of your solar panels:")
            # st.write("You have entered:", wattage_peak, "watts as the wattage peak of your solar panels")
    # Check the value of input_type and display the input box for the amount of solar panels you have if "Amount of solar panels" is selected
        if input_type == "Amount of solar panels":
            amount_of_solar_panels = st.number_input("Enter the amount of solar panels you have:")
            # st.write("You have entered:", amount_of_solar_panels, "solar panels")

    # Add a select box for whether or not you have a solar boiler
    solar_boiler = st.selectbox("Do you have a solar boiler?", ["No","Yes"])
    # Display the selected value
    # st.write("You have selected:", solar_boiler)

    # Add a select box for whether or not you have a shower with heat recovery
    shower_with_heat_recovery = st.selectbox("Do you have a shower with heat recovery?", ["No","Yes"])
    # Display the selected value
    # st.write("You have selected:", shower_with_heat_recovery)

    "---"
    st.header("Personal information")
    # Add a expander to explain this step in the quick scan tool
    with st.expander("Info about personal information"):
        st.write("- We want to know your motivation and budget to give personal recommendation to improve your house")
    
    # Add a select box for the motivation to save energy
    motivation = st.selectbox("Select the motivation to save energy:", [
        "I want to save money", 
        "I want to save energy", 
        "I want to save the environment", 
        "I want a better energy label", 
        "I want to save money and energy", 
        "I want to save money and have a better energy label",
        "I want to save energy and have a better energy label",
        "I want to save money, energy and have a better energy label",
        "I want to have a better energy label and save the environment",
        "I want to save money and the environment", 
        "I want to save energy and the environment", 
        "I want to save money, energy and the environment"])

    # Add a select box for the budget to invest
    budget = st.number_input("What is your budget to start with", min_value=0.0, max_value=1000000.0, value=500.0, step=0.1)


"---"
#summary
with st.container():
    st.title("Your summary")

    # Create a list of all the input box and select box variables
    input_select_vars = [postcode, huisnummer, year_of_built, wall_insulation, floor_insulation, roof_type, window_type_bedrooms, heating_system, ventilation_type, motivation, budget]

    # Check if all the input boxes and select boxes are filled
    if all(var is not None and var != "" for var in input_select_vars):
        st.image('images/summary.png')
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
                summary = "- Postcode is: " + postcode + "\n"
                summary += "- Huisnummer is: " + huisnummer + "\n"
                summary += "- Year of built is: " + year_of_built + "\n"
                summary += "- Your energy label is: " + label_letter + " and is valid until " + valid_until + "\n"
                summary += "- Your house type is: " + building_type + "\n"
                if building_area:
                    summary += "- The area of your house is: " + str(building_area) + " m2\n"
                else:
                    summary += "- The area of your house is not available\n"
                summary += "- Roof type is: " + roof_type + "\n"
                if roof_type in ["Flat", "Flat and slanted"]:
                    summary += "- Flat roof insulation is: " + flat_roof_insulation + "\n"
                    summary += "- Flat roof area is: " + flat_roof_area + "\n"
                if roof_type in ["Slanted", "Flat and slanted"]:
                    summary += "- Slanted roof insulation is: " + slanted_roof_insulation + "\n"
                    summary += "- Slanted roof area is: " + slanted_roof_area + "\n"
                summary += "- Wall insulation is: " + wall_insulation + "\n"
                summary += "- Floor insulation is: " + floor_insulation + "\n"
                summary += "- Window type for living spaces is: " + window_type_living + "\n"
                summary += "- Window type for bedrooms is: " + window_type_bedrooms + "\n"
                summary += "- Heating system is: " + heating_system + "\n"
                summary += "- Ventilation type is: " + ventilation_type + "\n"
                summary += "- Gas consumption is: " + str(gas_consumption) + "m3" + "\n"
                summary += "- Gas price is: €" + str(gas_price) + "\n"
                summary += "- Electricity consumption is: " + str(electricity_consumption) + "kWh" + "\n"
                summary += "- Electricity price is: €" + str(electricity_price) + "\n"
                summary += "- Energy contract ends on: " + str(end_date) + "\n"
                if solar_panels == "Yes":
                    summary += "- You have solar panels\n"
                    if input_type == "Wattage peak of solar panels":
                        summary += "- Wattage peak of solar panels is: " + str(wattage_peak) + " watts\n"
                    if input_type == "Amount of solar panels":
                        summary += "- Amount of solar panels is: " + str(amount_of_solar_panels) + "\n"
                if solar_boiler == "Yes":
                    summary += "- You have a solar boiler\n"
                if shower_with_heat_recovery == "Yes":
                    summary += "- You have a shower with heat recovery\n"
                summary += "- Your motivation is: " + motivation + "\n"
                summary += "- Your budget is: €" + str(budget) + "\n"

    else:
            st.error('Please fill in all the required input boxes and select boxes')

    st.info("You can ignore this error. When you click on click here to see your summary, it wil disappear.")
    # Check if all the input boxes and select boxes are filled
    if all(var is not None and var != "" for var in input_select_vars):
        st.text(summary)
        
        # Get the current time and date
        now = datetime.now()

        # Format the date and time string as "yyyy-mm-dd"
        date_time = now.strftime("%d-%m-%Y")
        
        # Download summary
        st.download_button("Download summary", file_name= date_time + "_summary-of-my-home.txt", data=summary)







