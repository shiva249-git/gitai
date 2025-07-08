import os
import openai

# Get API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# (Optional) Debug print - remove or comment out after testing for security
print("Loaded key:", api_key[:8] + "..." if api_key else "NOT FOUND")

# Configure OpenAI
openai.api_key = api_key

try:
    # List available models (tests authentication)
    models = openai.Model.list()
    print("Success! Your API key works.")
    print(f"Number of models available: {len(models['data'])}")
except openai.error.AuthenticationError:
    print("FAIL: Authentication error! Invalid or missing API key.")
except Exception as e:
    print(f"Other error: {e}")
if __name__ == "__main__":
    app.run(port=5000, debug=True)
