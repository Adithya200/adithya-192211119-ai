import yfinance as yf
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords and lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return tokens


def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return info


def main():
    print("Welcome to the Financial Stock Assistant AI Chatbot!")
    print("Ask me about any stock by its ticker symbol.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Tokenize and preprocess user input
        tokens = preprocess_text(user_input)

        # Check if the user input contains a valid stock ticker symbol
        for token in tokens:
            if token.isalpha() and token.isupper() and len(token) <= 5:
                symbol = token
                break
        else:
            print("I couldn't find a valid stock symbol in your query. Please try again.")
            continue

        # Get stock information
        stock_info = get_stock_info(symbol)

        # Display stock information
        if stock_info:
            print(f"Stock: {symbol}")
            print(f"Name: {stock_info.get('longName', 'N/A')}")
            print(f"Industry: {stock_info.get('industry', 'N/A')}")
            print(f"Market Cap: {stock_info.get('marketCap', 'N/A')}")
            print(f"Price: {stock_info.get('regularMarketPrice', 'N/A')}")
            print(f"Previous Close: {stock_info.get('previousClose', 'N/A')}")
        else:
            print(f"Sorry, I couldn't find information for the stock symbol {symbol}.")


if __name__ == "__main__":
    main()
