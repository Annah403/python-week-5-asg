# defined class(The parent class)
class FitnessTracker:
    def __init__(self, user_name, age, weight):
        # intializing attributes 
        self.user_name =user_name
        self.age =age
        self.weight =weight
        self.steps = 0

# method - adding steps and updating the total 
    def add_steps(self, steps):
        self.steps += steps
        return f"{self.user_name} walked {steps}. Total: {self.steps}steps."
    # method- displaying the user profile
    def profile(self):
        return f"user:{self.user_name},age: {self.age}, weight: {self.weight}kg."
    

# child class
class healthfitness(FitnessTracker):
        def __init__(self,user_name, age, weight, heart_rate=60):
            super().__init__(user_name,age, weight)
            self.__heart_rate = heart_rate
        

        def track_heart_rate(self):
            return f"{self.user_name}'s heart rate: is {self.__heart_rate} bpm"
        
# polymorphism
        def calories_burned(self):
            calories = self.steps * 0.5
            weight_loss = calories/ 7700
            return f"{self.user_name} lost approximately  {weight_loss:.3f} kg after {self.steps} steps."


