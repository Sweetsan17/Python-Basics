class PersonDetails:
    # get details from users 

    def getDetails(self):
        self.name = input("Enter Your Name : ")
        self.age = int(input("Enter Your Age : "))
        self.sub1 = int(input("Enter The E-Tech Mark : "))
        self.sub2 = int(input("Enter The SFT Mark : "))
        self.sub3 = int(input("Enter The ICT Mark : "))
    # calculate average from subject marks 

    def average(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3
    # function for check the status in person 

    def status(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Minor"
    # Display the person Details in function 

    def showPersonDetails(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Mark 1  : {self.sub1}")
        print(f"Mark 2  : {self.sub2}")
        print(f"Mark 3  : {self.sub3}")
        print(f"Status  : {self.status()}")
        print(f"Average : {self.average()}")      
 
person = PersonDetails() # object creating assigned class name 

person.getDetails()  # user inputs  inside function

person.showPersonDetails() # peson details are shows 





       
