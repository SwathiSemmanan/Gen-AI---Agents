import cohere

# Initialize Cohere client with your API key
co = cohere.Client('SjyS7xPZqAisqztLmaHBf3VwjsxWShRrgcEBKxeu')  # Replace with your actual Cohere API key

# Define the system prompt with instructions
system_prompt = (
    "You are a product recommender agent specializing in finding products that match user preferences. "
    "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%. "
    "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, Meesho, Nike, and other reputable platforms. "
    "Verify that each product recommendation is in stock and available for purchase. "
    "Avoid suggesting counterfeit or unverified products. "
    "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response. "
    "Format the recommendations neatly and ensure clarity for ease of user understanding."
)

# Define user preferences
user_preferences = (
    "I am looking for running shoes with the following preferences: "
    "Color: Black, Purpose: Comfortable for long-distance running, Budget: Under Rs. 10,000"
)

# Generate product recommendations using Cohere's chat() method
response = co.chat(
    model='command-r',
    message=user_preferences,
    chat_history=[
        {"role": "SYSTEM", "message": system_prompt}
    ]
)

# Print the recommendations
print("Product Recommendations:\n")
print(response.text.strip())
