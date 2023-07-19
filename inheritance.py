class parent():
    def __init__(self):
        print("This is parent class")
        
    def menu(dish):
        if dish=="Pizza":
            print("You can add the following toppins")
            print("More Cheese| Add Pineapple | Add Origano | Add Mayoneise")
            
        elif dish=="Capuccino":
              print("You can add the following toppinns")
              print("Whipped cream | Add ice | Chocolate | Biscuits")
        elif dish=="Tea":
              print("You can add the following side dish")
              print(" bread | Tea Biscuits | Toast ")
              
        else:
            print("please enter valid dish")
            
            
    def final_amount(dish, add_ons):
        if dish=="Pizza" and add_ons=="Cheese":
            print("you need to pay 250 USD")
        if dish=="Pizza" and add_ons=="Pineapple":
            print("you need to pay 350 USD")
        if dish=="Pizza" and add_ons=="Origano":
            print("you need to pay 150 USD")
        if dish=="Pizza" and add_ons=="Mayoneise":
            print("you need to pay 255 USD")  
        if dish=="Capuccino" and add_ons=="Whipped Cream":
            print("you need to pay 250 USD")
        if dish=="Capuccino" and add_ons=="Ice":
            print("you need to pay 350 USD")
        if dish=="Capuccino" and add_ons=="Chocolate":
            print("you need to pay 150 USD")
        if dish=="Capuccino" and add_ons=="Bisuits":
            print("you need to pay 255 USD")         
        if dish=="Tea" and add_ons=="Bread":
            print("you need to pay 350 USD")
        if dish=="Tea" and add_ons=="Tea Biscuits":
            print("you need to pay 150 USD")
        if dish=="Tea" and add_ons=="Toast":
            print("you need to pay 255 USD")                       
            
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
       
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)

class child3(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)        

child1_object=child1("Pizza")
child1_object.get_menu()

child2_object=child2("Pizza","Pineapple")
child2_object.get_final_amount()  

child3_object=child3("Tea","Toast")
child3_object.get_final_amount()      