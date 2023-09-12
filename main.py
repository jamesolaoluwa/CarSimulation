class simulation:
    def __init__ (self,brand,model,color,year,speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed
        
    def start(self):
        print(f'{self.brand} {self.model} has started')
        
    def accelerate(self):
        option = input('Enter Acceleration Option [yes, no]: ')
        if option == 'yes':
            print('Nitro Engaged')
        elif option == 'no':
            print('Nitro Disengaged')
    def stop(self):
        print(f'{self.brand} {self.model} has stopped')
      
car1 = simulation('Audi','GM5','Black',2020,345)
car1.start()
car1.accelerate()

class simulation2(simulation):
    def opentrunk(self):
        option = input('Enter opentrunk Option [yes, no]: ')
        if option == 'yes':
            print('Trunk opened')
        elif option == 'no':
            print('Trunk closed')
          
car2 = simulation2('lambogini','Mercilado','Yellow',2020,500)
car2.start()
car2.accelerate()
car2.opentrunk()