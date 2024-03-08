import yfinance as yf
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')

class StockAssistant:
    def _init_(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def process_text(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [self.ps.stem(word) for word in tokens if word not in self.stop_words and word not in string.punctuation]
        return tokens

    def get_stock_info(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')
            if not data.empty:
                info = {
                    'Open': data['Open'][0],
                    'High': data['High'][0],
                    'Low': data['Low'][0],
                    'Close': data['Close'][0]
                }
                return info
            else:
                return "No data available for the symbol."
        except:
            return "Error fetching data for the symbol."

    def respond(self, user_input):
        tokens = self.process_text(user_input)
        if 'price' in tokens:
            index = tokens.index('price')
            if index > 0:
                symbol = tokens[index - 1].upper()
                info = self.get_stock_info(symbol)
                if isinstance(info, dict):
                    response = f"Stock information for {symbol} today:\n"
                    for key, value in info.items():
                        response += f"{key}: {value}\n"
                    return response
                else:
                    return info
            else:
                return "Please provide a valid stock symbol."
        else:
            return "I'm sorry, I couldn't understand your request."

if __name__ == "__main__":
    assistant = StockAssistant()
    print("Welcome to the Financial Stock Assistant!")
    print("You can ask about the price of any stock by providing its symbol.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Thank you for using the Financial Stock Assistant. Goodbye!")
            break
        response = assistant.respond(user_input)
        print("Assistant:", response)