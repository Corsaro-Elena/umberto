#dichiaro di star facendo una lista e la stampo
thislist = ["apple", "banana", "cherry"]
print(thislist)

#dichiaro di star facendo una lista con valori duplicati
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#dichiaro di star stampando il numero di elementi nella lista
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#dichiaro di star inserendo nella lista tipi di dati stringa, int, booleani
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#dichiaro di star scrivendo una lista con dati booleani , stringa, int
list1 = ["abc", 34, True, 40, "male"]

#dichiaro di star utilizzando il list() costruttore per creare un elenco per poi stamparlo 
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#dichiaro di star stampando la seconda voce della lista 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#dichiaro di star stampando l'ultima voce della lista
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#dichiaro di stampare i dati terzo quarto quinto
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#dichiaro di star stampando i dati prima del quarto
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#dichiaro che sto stampando i dati da ciliegia fino alla fine
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#dichiaro di star stampando gli elementi da orange a mango anche se non incluso 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#dichiaro di star controllando se mela è nell'elenco
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#dichiaro di star cambiando uno degli oggetti presenti nella lista(2)
 thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#dichiaro di star modificando i valori banana e ciliegia 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#dichiaro di star cambiando il secondo valori con due valori diversi
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#dichiaro di modificare il secondo e il terzo valore con un solo elemento 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#dichiaro di utilizzare aunguria come terzo elemento
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#dichiaro di utilizzare append() per aggiungere un elemento nella lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#dichiaro di inserire un elemento in seconda posizione
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#dichiaro di star aggiungendo gli elementi di tropical a thislist
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#dichiaro di star aggiungendo una tuple alla lista
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#dichiaro di  star rimuovendo un dato
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#dichiaro di star rimuovendo il secondo elemento
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#dichiaro di star rimuovendo l'ultimo elemento 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#dichiaro di star rimuovendo il primo elemento 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#dichiaro di voler eliminare l'intera lista
thislist = ["apple", "banana", "cherry"]
del thislist

#dichiaro di eliminare e stampare ciò che c'era nella lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#dichiaro di star stampando tutti gli elementi, uno ad uno
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#dichiaro di stampare gli elementi facendo riferimento al loro numero di indice
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#dichiaro di stampare tutti gli elementi utilizzano un while per scorrere tutti i numeri di indice
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#dichiaro di utilizzare for per stampare tutti gli elementi di un elenco 
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]