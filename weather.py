# App to Get Temperature Data from "Open Weather Map" Service
import pyowm

#Define global variable to store OWM weather-query object
owm = pyowm.OWM('0c59c1e37d1993be20e8d33ebca2955c')
wman = owm.weather_manager()

#Function that gets weather info from API - DO NOT EDIT
#  Returns results in dictionary with
#  keys 'temp', 'temp_max', 'temp_min'
#  and values that are floats
#  DO NOT EDIT THIS FUNCTION
def getWeather(city, country):
    location = city+','+country
    observation = wman.weather_at_place(location).weather
    return observation.temperature('fahrenheit')

def main():
    bingus = True

    while bingus:
        yaga = True
        print("Find temperature in cities worldwide\nPlease enter a city and country")
        city = input("City: ")
        country = input("Country: ")
        dic = getWeather(city, country)

        print(f"""\nMax temperature: {dic.get('temp_max', 'N/a')} °F   {"{:.2f}".format((dic.get('temp_max', 'N/a') - 32) / 1.8)} °C
    Current temperature: {dic.get('temp', 'N/a')} °F   {"{:.2f}".format((dic.get('temp', 'N/a') - 32) / 1.8)} °C
    Minimum temperature: {dic.get('temp_min', 'N/a')} °F   {"{:.2f}".format((dic.get('temp_min', 'N/a') - 32) / 1.8)} °C
            """)
        while yaga:
            again = input("Check weather in another city? (Y or N): ")
            if again.lower() == "y":
                yaga = False
            elif again.lower() == "n":
                bingus = False
                yaga = False
            else:
                print("Error! Please enter a valid input.")
    # Add code that prints program's purpose, then:
    #   1. Prompts user for city and country
    #   2. Calls getWeather with city and country and saves returned dictionary
    #   3. Uses keys "temp_max", "temp", and "temp_min" to extract temperatures
    #   4. Prints the temperatures
    #   5. Asks if user wants to check another city (Y or N)
    #   6. Validates user response
    #   7. If Y, loop back to step 1

#Start the app
main()
