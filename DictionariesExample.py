import os

os.system("clear")

favorite_pizza = {
	"Merv": "Pepperoni",
	"Tina": "Cheese",
	"Mateo": "Mushrooms",
	"Tayal": "Sausage"
}

print(favorite_pizza)

#Call mushooms
print(favorite_pizza["Mateo"])

favorite_pizza.update({"Zeus":"black peppers"})

print(favorite_pizza)

favorite_pizza1 = {
	"Merv": "Pepperoni",
	"Tina": "Cheese",
	"Mateo": "Mushrooms",
	"Tayal": "Sausage",
	"iPhone": [4,5,6,7,'X',11]
}

print(favorite_pizza1)