from google import genai

client = genai.Client(api_key="AIzaSyCpX11YMKBrHkkCYxrOh_OZuVpv9sLG-hc")

if __name__ == "__main__":
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    print(response.text)