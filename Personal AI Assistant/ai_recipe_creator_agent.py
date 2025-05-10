import cohere

# Initialize Cohere client with your API key
co = cohere.Client('SjyS7xPZqAisqztLmaHBf3VwjsxWShRrgcEBKxeu')  # Replace with your actual API key

# Define your input ingredients
ingredients = "chicken, garlic, and tomatoes"

# Create a message prompt
message = f"Create a detailed cooking recipe using the following ingredients: {ingredients}"

# Generate the recipe using the chat method (since you're using command-r)
response = co.chat(
    model='command-r',
    message=message,
)

# Print the generated recipe
print("Recipe:\n")
print(response.text.strip())
