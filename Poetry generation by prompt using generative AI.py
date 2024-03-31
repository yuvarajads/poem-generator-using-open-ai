import openai

# Function to load OpenAI API key from a secure location
def load_api_key():
    # Replace this function with your own method of loading the API key
    return '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'

# Class for interacting with OpenAI GPT-3.5 model to generate poetry
class PoetryGenerator:
    def __init__(self):
        self.api_key = load_api_key()

    # Method to generate poetry based on user prompt
    def generate_poetry(self, prompt, max_tokens=100, temperature=0.7, engine="text-davinci-003"):
        try:
            openai.api_key = self.api_key
            # Request poem generation from OpenAI
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print("Error generating poetry:", e)
            return None

# Class for handling user interaction
class UserInterface:
    def __init__(self):
        self.poetry_generator = PoetryGenerator()

    # Method to run the user interface
    def run(self):
        print("Welcome to AI Poetry Generator!")
        while True:
            prompt = input("Enter your poetry prompt (type 'exit' to quit): ")
            if prompt.lower() == 'exit':
                print("Exiting...")
                break
            else:
                poem = self.poetry_generator.generate_poetry(prompt)
                if poem:
                    print("\nGenerated Poetry:")
                    print(poem)
                else:
                    print("Failed to generate poetry. Please try again.")

# Main function to start the application
def main():
    ui = UserInterface()
    ui.run()

if __name__ == "__main__":
    main()
