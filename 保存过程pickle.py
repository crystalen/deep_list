import pickle
class Dog():
    def __init__(self,name):
        self.age=1
        self.name=name
    
    def bark(self): 
        print('my name is',self.name)

dog1=Dog('hh')
with open('object.data','wb')as f_out:
    pickle.dump(dog1,f_out)

with open('object.data','rb')as f_in:
    dog2=pickle.load(f_in)

dog1.bark()
dog2.bark()
print(dog1.age,dog2.age)

with open('class.data','wb')as ff_out:
    pickle.dump(Dog,ff_out)

with open('class.data','rb')as ff_in:
    N_Dog=pickle.load(ff_in)

dog3=Dog('bb')
dog4=N_Dog('kk')
dog3.bark()
dog4.bark()
print(dog3.age,dog4.age)