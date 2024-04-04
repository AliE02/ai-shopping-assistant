from Stylist import Stylist
from SalesPerson import SalesPerson




class Store():
    """
    This class represents a store where user, stylist and salesperson agents interact with each other.
    """
    def __init__(self, api_key):
        """
        Initializes the store with the OpenAI API key.
        """
        self.api_key = api_key
        self.stylist = Stylist(api_key)
        self.salesperson = SalesPerson(api_key)

    def start(self):
        """
        Starts the conversation between the user, stylist and salesperson agents.
        """
        print("Welcome to our store! How can I help you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Thank you for visiting our store! Have a great day!")
                break
            stylist_output = self.handle_stylist(self.stylist.answer(("user", user_input)))
            print(f"Assistant: {stylist_output}")

    
    def handle_stylist(self, stylist_output):
        if stylist_output.startswith("[User]"):
            stylist_output = stylist_output[6:]
            return stylist_output
        elif stylist_output.startswith("[SalesPerson]"):
            stylist_output = stylist_output[14:]
            return self.handle_salesperson(self.request_items(stylist_output))
        else:
            return self.handle_stylist(self.stylist.answer(("metadata", "Your output is not valid. Please try again.")))

