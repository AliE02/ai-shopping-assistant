import openai

class Stylist():
    """
    This class represents a stylist agent that interacts with user and provides a comprehensive
    description of the user's needs and preferences.
    """
    def __init__(self, api_key):
        """
        Initializes the stylist agent with the OpenAI API key.
        """
        self.api_key = api_key
        self.conversation_history = []
        
        openai.api_key = self.api_key
        with open("stylist_prompt.txt", "r") as file:
            self.conversation_history.append(("metadata", file.read()))




    def answer(self, question):
        """
        Answers a question asked by the user and updates the conversation history.
        """
        self.conversation_history.append(question)

        response = openai.Completion.create(
            engine="davinci",
            prompt=self.get_prompt(),
            max_tokens=150
        )
        output = response.choices[0].text
        self.conversation_history.append(("stylist", output))

        return output




    
    def get_prompt(self):
        """
        Returns the conversation history as a prompt.
        """
        return "\n".join([f"{role}: {message}" for role, message in self.conversation_history])
    