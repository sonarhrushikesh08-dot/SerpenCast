#SerpenCast

import requests
import google.generativeai as genai

#api_keys

OPENWEATHER_API_KEY = "xxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxx"

#for authentication with GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

#loading of gemini model

model = genai.GenerativeModel("gemini-1.5-flash")

#weather function

def get_weather(city):
    url = (
        f"xxxxxxxxxxxxxxxxxxxxx"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_data

    else:
        return None


# ask about weather to gemini function 

def ask_gemini_about_weather(weather_data, question):

    prompt = f"""
    Weather Data:
    City: {weather_data['city']}
    Temperature: {weather_data['temperature']}°C
    Humidity: {weather_data['humidity']}%
    Weather: {weather_data['description']}
    Wind Speed: {weather_data['wind_speed']} m/s

    User Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text

#main function

def main():

    city = input("Enter city name: ")

    weather_data = get_weather(city)

    if weather_data:

        print("="*30)
        print("WEATHER REPORT".center(30))
        print("="*30)
        print(
          f"\n{'City'.ljust(15)}:{weather_data['city']}\n"
          f"\n{'Temperature'.ljust(15)}:{weather_data['temperature']}°C\n"
          f"\n{'Humidity'.ljust(15)}:{weather_data['humidity']}%\n"
          f"\n{'Condition'.ljust(15)}:{weather_data['description']}\n"
          f"\n{'Wind Speed'.ljust(15)}:{weather_data['wind_speed']}m/s\n"
          )
        question = input("\nAsk Gemini about the weather: ")

        ai_response = ask_gemini_about_weather(
            weather_data,
            question
        )

        print("="*30)
        print("GEMINI'S RESPONSE".center(30))
        print("="*30)
        print(ai_response)

    else:
        print("City not found or API error.")


#main variable
 
if __name__ == "__main__":
    main()