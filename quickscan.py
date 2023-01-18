import streamlit as st

st.title("Quick scan of your house")
"---"

st.header("Type of house")
# Set up the select box for the home type
home_type = st.selectbox("Select the type of home you live in:", ["Detached", "Semi-detached", "Terraced", "Corner house"])
# Display the entered type of house
st.write("You have selected:", home_type)

# Set up the year of built select box
year_of_built = st.selectbox("Select the year of built:", ["Till 1919", "1920-1945", "1946-1964", "1965-1974", "1975-1991", "1992-2005", "2006-2014", "2015-now"])
# Display the selected year of built
st.write("You have selected year of built:", year_of_built)

# Add an input box for the area
area = st.selectbox("Select the area of your home (in square meters)", ["Less than 50m2", "50m2-100m2", "100m2-150m2", "150m2-200m2", "200m2-250m2", "250m2-300m2", "300m2-350m2","350m2-400m2","More than 400m2"])
# Display the selected area
st.write("You have selected:", area, "square meters")
"---"

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

st.header("Number of people you live with")
# Add a select box for the number of people living in the home
num_people = st.selectbox("Select the number of people you live with:", ["1", "2", "3", "4", "5", "6 or more"])
# Display the selected number of people
st.write("You live with:", num_people, "people")
"---"

st.header("Municipality")
# Add a select box for the municipalities in the province of Utrecht
municipality = st.selectbox("Select your municipality:", ["Amersfoort", "Baarn", "Bunnik", "Bunschoten", "De Bilt", "Driebergen-Rijsenburg", "Houten", "IJsselstein", "Leusden", "Loenen", "Maarssen", "Maarssenbroek", "Montfoort", "Nieuwegein", "Nieuwegein-Noord", "Oudewater", "Renswoude", "Soest", "Utrecht", "Utrechtse Heuvelrug", "Veenendaal", "Wijk bij Duurstede", "Zeist", "Woudenberg"])
# Display the selected municipality
st.write("You have selected:", municipality)
"---"

st.header("Insulation")
# Add a select box for the type of facade insulation
facade_insulation = st.selectbox("Select the type of facade insulation you have:", ["Reasonable 10cm - Rc 2,6", "Good 16cm - Rc 3,9", "Excellent 21cm - Rc 5"])
# Display the selected type of facade insulation
st.write("You have selected:", facade_insulation, "facade insulation")

# Add a select box for the type of floor insulation
floor_insulation = st.selectbox("Select the type of floor insulation you have:", ["Reasonable 10cm - Rc 2,4", "Good 16cm - Rc 3,7", "Excellent 22cm - Rc 5"])
# Display the selected type of floor insulation
st.write("You have selected:", floor_insulation, "floor insulation")

# Check the value of roof_type and display the select box for the type of flat roof insulation if "flat" or "flat and slanted" is selected
if roof_type in ["Flat", "Flat and slanted"]:
    flat_roof_insulation = st.selectbox("Select the type of flat roof insulation you have:", ["Reasonable 10cm - Rc 2,4", "Good 16cm - Rc 4", "Excellent 26cm - Rc 6"])
    st.write("You have selected:", flat_roof_insulation, "flat roof insulation")

# Check the value of roof_type and display the select box for the type of slanted roof insulation if "slanted" is selected
if roof_type in ["Slanted", "Flat and slanted"]:
    slanted_roof_insulation = st.selectbox("Select the type of slanted roof insulation you have:", ["Reasonable 10cm - Rc 2,4", "Good 17cm - Rc 4", "Excellent 26cm - Rc 6"])
    st.write("You have selected:", slanted_roof_insulation, "slanted roof insulation")
"---"

st.header("Windows")
# Add a select box for the type of window you have for living spaces
window_type = st.selectbox("Select the type of window you have for living spaces:", ["Single-glazing", "Double-glazing", "HR++ glazing", "Triple glazing", "Vacuum glass"])
# Display the selected type of window
st.write("You have selected:", window_type, "windows for living spaces")

# Add a select box for the type of window you have for bedrooms
window_type = st.selectbox("Select the type of window you have for bedrooms:", ["Single-glazing", "Double-glazing", "HR++ glazing", "Triple glazing", "Vacuum glass"])
# Display the selected type of window
st.write("You have selected:", window_type, "windows for bedrooms")


st.header("Heating and ventilation")
# Add a select box for the type of heating system you have for heating and warm water
heating_system = st.selectbox("Select the type of heating system you have for heating and warm water:", ["High-performance combi boiler", "Hybrid heat pump", "Full air heat pump", "Ground source heat pump", "Heat grid"])
# Display the selected type of heating system
st.write("You have selected:", heating_system, "heating system")

# Add a select box for the type of ventilation you have
ventilation_type = st.selectbox("Select the type of ventilation you have:", ["Natural with grilles and windows", "Mechanical exhaust", "Mechanical exhaust with CO2 control", "Whole-house balanced ventilation with heat recovery", "Ventilation unit with heat recovery in living room and master bedroom"])
# Display the selected type of ventilation
st.write("You have selected:", ventilation_type, "ventilation")


st.header("Electricity")
# Add a input box for the price of electricity
electricity_price = st.number_input("Enter the current price you pay for electricity in €/kWh:", min_value=0.0, max_value=100.0, value=0.0, step=0.1)




# calculations

# Set up factors for the different types of homes
home_type_factors = {
    "Detached": 1.5,
    "Semi-detached": 1.3,
    "Terraced": 1.1,
    "Upstairs apartment": 0.9,
    "Ground floor apartment": 0.8,
    "Corner house": 1.2
}

# Set up factors for the year of built
year_of_built_factors = {
    "Till 1919": 1.2,
    "1920-1945": 1.1,
    "1946-1964": 1.0,
    "1965-1974": 0.9, 
    "1975-1991": 0.8, 
    "1992-2005": 0.7, 
    "2006-2014": 0.6, 
    "2015-now": 0.5 
}

# Set up factors for the area of floor
area_factors = {
    "Less than 50m2": 0.8,
    "50m2-100m2": 0.9,
    "100m2-150m2": 1.0,
    "150m2-200m2": 1.1,
    "200m2-250m2": 1.2,
    "250m2-300m2": 1.3,
    "300m2-350m2": 1.35,
    "350m2-400m2": 1.4,
    "More than 400m2": 1.45
}

# Set up factors for how much people your are living with
people_factors = {
    "1": 0.8,
    "2": 0.9,
    "3": 1.0,
    "4": 1.1,
    "5": 1.2,
    "6 or more": 1.3,
}

# Set up factors for the different types of roof
roof_type_factors = {
    "Flat roof": 1.0,
    "Sloped roof": 1.1
}

# set up factors for the area of slanted roof
roof_area_factors = {
    "Less than 15m2": 0.8,
    "15m2 - 20m2": 0.9,
    "20m2 - 25m2": 1.0,
    "25m2 - 30m2": 1.1,
    "30m2 - 35m2": 1.2,
    "35m2 - 40m2": 1.3,
    "40m2 - 45m2": 1.35,
    "45m2 - 50m2": 1.40,
    "More than 50m2": 1.45
}

# set up factors for the area of flat roof
flat_roof_area_factors = {
    "Less than 15m2": 0.9,
    "15m2 - 20m2": 0.95,
    "20m2 - 25m2": 1.0,
    "25m2 - 30m2": 1.05,
    "30m2 - 35m2": 1.1,
    "35m2 - 40m2": 1.15,
    "40m2 - 45m2": 1.2,
    "45m2 - 50m2": 1.25,
    "More than 50m2": 1.3
}

# Set up factors for the different types of roof insulation
roof_insulation_factors = {
    "Reasonable 10cm - Rc 2,4": 1.0,
    "Good 16cm - Rc 3,7": 0.9,
    "Excellent 22cm - Rc 5": 0.85
}

# Set up factors for the different types of facade insulation
facade_insulation_factors = {
    "Reasonable 10cm - Rc 2,6": 0.98,
    "Good 16cm - Rc 3,9": 0.89,
    "Excellent 22cm - Rc 5,2": 0.85
}

# Set up factors for the different types of floor insulation
floor_insulation_factors = {
    "Reasonable 10cm - Rc 2,4": 1.0,
    "Good 16cm - Rc 3,7": 0.9,
    "Excellent 22cm - Rc 5": 0.85
}

# Set up factors for the different types of flat roof insulation
flat_roof_insulation_factors = {
    "Reasonable 10cm - Rc 2,4": 1.0,
    "Good 16cm - Rc 4": 0.87,
    "Excellent 26cm - Rc 6": 0.82
}

# Set up factors for the different types of slanted roof insulation
slanted_roof_insulation_factors = {
    "Reasonable 10cm - Rc 2,4": 1.0,
    "Good 17cm - Rc 4": 0.87,
    "Excellent 26cm - Rc 6": 0.82
}

# Set up factors for the different types of windows
window_type_factors = {
    "Single-glazing": 1.1,
    "Double-glazing": 1.0,
    "HR++ glazing": 0.95,
    "Triple glazing": 0.94,
    "Vacuum glass": 0.95
}

# Set up factors for the different types of heating systems
heating_system_factors = {
    "High-performance combi boiler": 1.0,
    "Hybrid heat pump": 1.2,
    "Full air heat pump": 1.3,
    "Ground source heat pump": 1.4,
    "Heat grid": 0.8
}


# Set up factors for the different types of ventilation
ventilation_type_factors = {
    "Natural with grilles and windows": 1.1,
    "Mechanical exhaust": 1.0,
    "Mechanical exhaust with CO2 control": 1.1,
    "Whole-house balanced ventilation with heat recovery": 1.15,
    "Ventilation unit with heat recovery in living room and master bedroom": 1.1
}


# Calculate the annual electricity consumption based on the input
if roof_type == "Slanted":
    annual_electricity_consumption = 3500 * home_type_factors[home_type] * year_of_built_factors[year_of_built] * area_factors[area] * people_factors[num_people] * roof_area_factors[slanted_roof_area] * facade_insulation_factors[facade_insulation] * floor_insulation_factors[floor_insulation] * slanted_roof_insulation_factors[slanted_roof_insulation] * window_type_factors[window_type] * heating_system_factors[heating_system] * ventilation_type_factors[ventilation_type]
# Add an input box for your annual electricity consumption in kWh and prefill it with the calculated value
    annual_electricity_consumption = st.number_input("Enter your annual electricity consumption in kWh:", value=annual_electricity_consumption)
    st.write("Based on your input, this should be your annual electricity consumption")

# Calculate the annual electricity consumption based on the input
if roof_type == "Flat":
    annual_electricity_consumption = 3500 * home_type_factors[home_type] * year_of_built_factors[year_of_built] * area_factors[area] * people_factors[num_people] * flat_roof_area_factors[flat_roof_area] * facade_insulation_factors[facade_insulation] * floor_insulation_factors[floor_insulation] * flat_roof_insulation_factors[flat_roof_insulation] * window_type_factors[window_type] * heating_system_factors[heating_system] * ventilation_type_factors[ventilation_type]
# Add an input box for your annual electricity consumption in kWh and prefill it with the calculated value
    annual_electricity_consumption = st.number_input("Enter your annual electricity consumption in kWh:", value=annual_electricity_consumption)    
    st.write("Based on your input, this should be your annual electricity consumption")

# Calculate the annual electricity consumption based on the input
if roof_type == "Flat and slanted":
    annual_electricity_consumption = 3500 * home_type_factors[home_type] * year_of_built_factors[year_of_built] * area_factors[area] * people_factors[num_people] * roof_area_factors[slanted_roof_area] * flat_roof_area_factors[flat_roof_area] * facade_insulation_factors[facade_insulation] * floor_insulation_factors[floor_insulation] * flat_roof_insulation_factors[flat_roof_insulation] * slanted_roof_insulation_factors[slanted_roof_insulation] * window_type_factors[window_type] * heating_system_factors[heating_system] * ventilation_type_factors[ventilation_type]
# Add an input box for your annual electricity consumption in kWh and prefill it with the calculated value
    annual_electricity_consumption = st.number_input("Enter your annual electricity consumption in kWh:", value=annual_electricity_consumption) 
    st.write("Based on your input, this should be your annual electricity consumption")

# calculate the annual electricity bill based on the price of the contract
annual_electricity_bill = annual_electricity_consumption * electricity_price
st.write("Your annual electricity bill is: €", annual_electricity_bill)

"---"
st.header("Step 2")
###
###

# Add a select box for whether or not you have a solar boiler
solar_boiler = st.selectbox("Do you have a solar boiler?", ["Yes", "No"])
# Display the selected value
st.write("You have selected:", solar_boiler)

# Add a select box for whether or not you have a shower with heat recovery
shower_with_heat_recovery = st.selectbox("Do you have a shower with heat recovery?", ["Yes", "No"])
# Display the selected value
st.write("You have selected:", shower_with_heat_recovery)

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
