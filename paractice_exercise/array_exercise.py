#Let us say your expense for every month are listed below,
    #1.January - 2200
    #2.February - 2350
    #3.March - 2600
    #3.April - 2130
    #4.May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
#based on this

#creating a array
exp = [2200,2350,2600,2130,2190]

print("1 ", exp[1]-exp[0]) #different between First two mounths Exp
print("2 ", exp[0]+exp[1]+exp[2]) #total of three mounths exp
print("3 ", 2000 in exp) #its print True or Flase
exp.append(1980) #adding june month expense
print("4 ",exp) #adding june month expense
print("5 ", exp[3]-200) 
print(exp)
