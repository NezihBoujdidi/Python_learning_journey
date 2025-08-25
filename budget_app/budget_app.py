class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_name(self):
        return self.name
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for l in self.ledger :
            total+= l['amount']
        return total

    def transfer(self, amount, cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {cat.get_name()}')
            cat.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        total = 0
        for l in self.ledger :
            total+= l['amount']
        if amount > total :
            return False
        return True

    def __str__(self):
        budget_str=(30-len(self.name))//2*'*'+self.name+(((30-len(self.name))//2)+((30-len(self.name))%2))*'*'+'\n'
        for d in self.ledger:
            amount = d['amount']
            formatted_amount = f'{amount:.2f}'
            if len(d['description'])>23:
                budget_str+=d['description'][0:23:]+(7-len(formatted_amount))*' '+formatted_amount+'\n'
            else:
                budget_str+=d['description']+(30-len(d['description'])-len(formatted_amount))*' '+formatted_amount+'\n'
        budget_str+= f'Total: {self.get_balance()}'

        return budget_str

def create_spend_chart(categories):
    spendings={}
    total_spent=0
    for cat in categories:
        cat_spent=0
        for l in cat.ledger:
            if l['amount'] < 0:
                cat_spent+= -l['amount']
        spendings[cat.get_name()]=cat_spent
        total_spent+= cat_spent
    for key, value in spendings.items():
        spendings[key]=(((value*100)/total_spent)//10)*10
    chart_str ='Percentage spent by category\n'
    for i in range(100,-1,-10):
        if len(str(i)) == 2:    
            chart_str+= ' '+str(i)+'|'+' '
        elif i==0:
            chart_str+= '  '+str(i)+'|'+' '
        else:
            chart_str+=str(i)+'|'+' '
        for value in spendings.values():
            if value >= i:
                chart_str+='o  '
            else:
                chart_str+='   '
        chart_str+='\n'
    chart_str+='    '+'---'*len(spendings)+'-'+'\n'
    longest = 0
    for key in spendings.keys():
        if len(key)>longest:
            longest=len(key)
    for j in range(longest):
        chart_str+=' '*5
        for key in spendings.keys():
            if len(key)-1>=j:
                chart_str+=key[j]+'  '    
            else:
                chart_str+='   '
        if j!= longest-1: 
            chart_str+='\n'        
    return chart_str

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(14.08, 'groceries')
gaming = Category('Gaming')
gaming.deposit(2000, 'deposit')
gaming.withdraw(46.15, 'mouse')
print(food)
print(clothing)
print(create_spend_chart([food, clothing, gaming]))
                       
