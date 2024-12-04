class Parent : 
    def __init__(self,name,id):
        self.name = name
        self.id = id 

    def show(self):
        print(self.name)
        print(self.id)

class Human(Parent):
    def __init__(self, name, id , salary , post):
        self.salary = salary 
        self.post = post 

        Parent.__init__(self,name,id)


Human = Human("PhiladelphiaPennsylvania" , 29 , 10000000 , "CEO")
Human.show()
print(Human.salary , Human.post)
        
        

    
    


        