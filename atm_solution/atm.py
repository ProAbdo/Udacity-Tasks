class ATM:
    def __init__(self,balance,bank_name):
        self.withdrawals_list=[]
        self.balance=balance
        self.bank_name=bank_name
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print withdrawal
    def withdraw(self, request):
        print "Welcome to "+ self.bank_name
        print "Current balance = " + str(self.balance)
        print "="*30
        result = self.balance

        if request > self.balance:
            print("Can't give you all this money !!")
        elif request < 0:
            print("More than zero plz!")
        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            while request > 0:

                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0
        print "="*30
        return result    
        print "="*30
 

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2= ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
atm1.show_withdrawals()
