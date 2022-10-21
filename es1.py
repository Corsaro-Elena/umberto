#dichiaro 2 variabili x e y e le stampo 
x = "luca"
y= 5
print(x)
print(y)
#dichiaro 2 variabili x e cambio il tipo di variabile e le stampo
x = 3
x = "sally"
print(x)
#dichiaro 3 varibili numeriche x y e z e le stampo
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
#dichiaro 2 variabili 
x = 5
y = "John"
print(type(x))
print(type(y))
#dichiaro 2 variabili  posso utilizzare sia le virgolette che gli apici
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)
#dichiaro che i nomi delle variabili fanno distinzione tra maiuscole e minuscole
a = 4
A = "Sally"
print(a)
print(A)
#dichiaro nomi variabili legali
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#dichiaro nomi variabili illegali
2myvar = "John"
my-var = "John"
my var = "John"
#dichiaro che ogni parola tranne l'iniziale possiede la maiuscola
myVariableName = "John"
#dichiaro che ogni parola inzia con una kettera maiuscola
MyVariableName = "John"
#dichiaro che ogni parola è separata da un carattere di sottolineatura
my_variable_name = "John"
#dichiaro che si possono associare valori a più variabili in una riga
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#dichiaro che posso assegnare lo stesso valore a più variabili in una riga
x = y = z = "Orange"

print(x)
print(y)
print(z)
#dichiaro che posso avviare uno "spacchettamento"
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#dichiaro che la funzione print  serve per generare variabili 
x = "Python is awesome"
print(x)
#dichiaro che nella funzione print si emmettono più variabili separate da una virgola
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#dichiaro che utilizzando il + genero più variabili
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#dichiaro che il + si può utilizzare come operatore matematico
x = 5
y = "John"
print(x + y)
#dichiaro che per generare più variabili è meglio separarle con le virgole
x = 5
y = "John"
print(x, y)
#dichiaro di utilizzare variabili globali
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#dichiaro che la variabile globale con lo stesso nome rimarrà com'era
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#dichiaro che se si utilizza la global parola chiave, la variabile appartiene all'ambito globale
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#dichiaro che utilizzando la globalparola chiave si può modificare una variabile globale all'interno di una funzione
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)