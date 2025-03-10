class parrot:
    spieces='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot('blu',10)
woo=parrot('woo',18)

print("blu is a {}".format(blu.spieces))
print("woo is also a {}".format(woo.spieces))

print("{}is years {}".format(blu.name,blu.age))
print("{}is a {}".format(woo.name,woo.age))



                     

