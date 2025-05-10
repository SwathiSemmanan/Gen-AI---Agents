import cohere

# Initialize Cohere client with your API key
co = cohere.Client("SjyS7xPZqAisqztLmaHBf3VwjsxWShRrgcEBKxeu")  # Replace with your actual Cohere API key

# Define the agent's instructions as part of the system prompt
system_prompt = (
    "You are a highly knowledgeable book recommendation agent. "
    "Your goal is to help the user discover books based on their preferences, reading history, and interests. "
    "If the user mentions a specific genre, suggest books that span both classics and modern hits. "
    "When the user mentions an author, recommend similar authors or series they may enjoy. "
    "Highlight notable accomplishments of the book, such as awards, best-seller status, or critical acclaim. "
    "Provide a short summary or teaser for each book recommended. "
    "Offer up to 5 book recommendations for each request, ensuring they are diverse and relevant. "
    "Leverage online resources like Goodreads, StoryGraph, and LibraryThing for accurate and varied suggestions. "
    "Focus on being concise, relevant, and thoughtful in your recommendations."
)

# Define the user's request (e.g., based on books they like)
user_input = (
    "I really found anxious people and lessons in chemistry interesting, can you suggest me more such books?"
)

# Generate the book recommendations using Cohere's generate API
response = co.generate(
    model='command-xlarge',  # Use the correct model ID
    prompt=system_prompt + "\n\n" + user_input,
    max_tokens=300  # Adjust token length if needed
)

# Print the generated book recommendations
print("Book Recommendations:\n")
print(response.generations[0].text.strip())
