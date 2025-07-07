
from base_bot import BaseBot

class WillowBot(BaseBot):
   
    
    def __init__(self):
        super().__init__("Willow")
    
    def get_sentence(self):
       
        return f"Hello {self.name}"
