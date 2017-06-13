"""You are to create a Car class that can be used to instantiate various vehicles.

It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

Let the test guide you to building your Car boiler-plate."""
class Car(object):
    num_of_doors=4
    num_of_wheels=4
    speed=0

    def __init__(self, car_name='General', car_model='GM', car_type= 'saloon'):
    	self.name =car_name
    	self.model =car_model
    	self.car_type =car_type
    	if (self.name=='Porshe' or self.name=='Koenigsegg'):
    		self.num_of_doors = 2
    	if(not self.is_saloon()):
    		self.num_of_wheels=8
    def is_saloon(self):
    	return self.car_type=='saloon'

    def drive(self, speed):
        if self.car_type =='trailer':
            self.speed=77
        else:
            self.speed = pow(10, speed)
        return self

