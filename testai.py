import os
from openai import OpenAI, AuthenticationError

api_key = os.environ.get("OPENAI_API_KEY")
print("Loaded key:", api_key[:8] + "..." if api_key else "NOT FOUND")

client = OpenAI(api_key=api_key)

try:
    models = client.models.list()
    print("Success! Your API key works.")
    print(f"Number of models available: {len(list(models))}")
except AuthenticationError:
    print("FAIL: Authentication error! Invalid or missing API key.")
except Exception as e:
    print(f"Other error: {e}")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
