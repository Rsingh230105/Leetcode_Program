class bikeShop:
    def __init__(self,stock):
        self.stock=stock

    def display(self):
        print("Total Bikes:",self.stock)

    def rentForBike(self,q):

        if q<=0:
            print("Ente the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("Total Price",q*100)
            print("Total Available Bikes",self.stock )


while True:
  obj=bikeShop(100)
  uc=int(input('''1.Display available stocks
2.Request a bike for rent(100 rs-->1 quantity)
3.Exit '''))

  if uc==1:
      obj.display()
  elif uc==2:
      n=int(input("Enter the Qty:"))
      obj.rentForBike(n)
  else:
      break


