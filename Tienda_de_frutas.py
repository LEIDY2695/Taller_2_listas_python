#Actividad 1  -frutas 
list=["mandarina","lulo","fresa","maracuya","limon"]
# print(list)
print(list[0],list[4])

#Actividad 2
print(list[2])  
#print(list[10])  #posicion inexistente
#El sistema genera un error, ya que no exite un elemento en la posicion que se esta ingresando.

# Actividad 3
list.append("melon")   
print(list)

list.insert(2,"cereza")
print(list)


# Actividad 4
list.remove("fresa")
print(list)         

list.pop()
print(list)

list.pop(4)
print(list)

# remove - elimina el elemento que se le indique, en este caso "fresa"
# pop - elimina el ultimo elemento de la lista, en este caso "melon"    
# pop(4) - elimina el elemento que se encuentra en la posicion 4, en este caso "limon"


# #Actividad 5

print(list) #Lista antes del cambio

list[1] = 'sandia'
print(list) #Lista despues del cambio


# Actividad 6

list.extend(['uva','coco', 'piña'])
print(list)

print(len(list))
