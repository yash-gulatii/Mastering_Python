"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example_input():
    manatees = []
    n = int(input("Enter the number of manatees"))
    m = int(input("Enter the number of element in a manatee"))
    for i in range(0,n):
        print(i+1,"manatee")
        manatee = {}
        for j in range(i,m):
            print("Enter the Key of" , j+1 , "manatee")
            key = input()
            print("Enter the Value of" , j+1 , "manatee")
            value = input()
            manatee[key] = value 
        manatees.append(manatee)    
    return manatees

def example1(manatees):
    for manatee in manatees:
        print (manatee['name'])

def example2(manatees):
    print (manatees[0]['name'])
    print (manatees[0]['age'])

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print (manatee_property, ": ", manatee[manatee_property])

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print (oldest_manatee)

manatees = example_input()
example1(manatees)
example2(manatees)
example3(manatees)
example4(manatees)