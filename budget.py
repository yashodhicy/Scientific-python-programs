class Category:
  
  def __init__(self,name):
    self.name = name
    self.ledger=list()
  
  def __str__(self):
    title = f"{self.name:*^30}\n"
    lines=""
    total=0
    for line in self.ledger:
      lines += f"{line['description'][0:23]:23}{line['amount']:>7.2f}\n"
      total += line['amount']
    output = title+ lines+ "Total: " + str(total)
    return output

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def get_balance(self):
    
    balance=0
    for item in self.ledger:
      balance += item["amount"]
    return balance
  
  def check_funds(self,amount):
    bal = self.get_balance()
    if amount > bal:
      return False
    return True

  def withdraw(self,amount,description=""):
    check=self.check_funds(amount)
    if check==True:
      self.ledger.append({"amount": -amount, "description": description})
      return True;
    return False
  
  def transfer(self,amount,name):
    self.withdraw(amount,f"Transfer to {name.name}")
    trans=self.check_funds(amount)
    if trans==True:
        name.deposit(amount,"Transfer from {}".format(self.name))
        return True
    return False
    
  def getWithdrawls(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    
    return total
def calc(num):
  step1= num*100
  step2 = (step1//10)*10
  
  return step2

def totalwithdraws(types):
  totalw = 0
  twlist=[]
  for type in types:
    totalw += type.getWithdrawls()
    twlist.append(type.getWithdrawls())
  rounded = list(map(lambda x:calc(x/totalw), twlist))
  
  return rounded








def create_spend_chart(categories):
  percentages =totalwithdraws(categories)
  
  res1=""
 
  title = "Percentage spent by category\n"
  i=100
  while i>=0:
    
    barinput=""
    y=f"{i:>3}| "
    for percentage in percentages:
      if percentage>=i:
        barinput += "o  "
      else:
        barinput += "   "
    i-=10
    res1 += f"{y}{barinput}\n"
  
  dashes = "    " '-'+'---'*len(categories)+('\n')
  max_length = max(map(lambda x: len(x.__dict__.get('name')), categories))

  j=0
  res2=""
  while j< max_length:
    string=""
    
    for l in categories:
      name=l.__dict__.get('name')
      if j<len(name):
        string += name[j]+"  "
      else:
        string += "   "
    res2 += f"     {string}"
    if(j != max_length-1):
          res2 += '\n'
    j+=1
  res= title+res1+dashes+res2
  return res
  

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business,food,entertainment]))


