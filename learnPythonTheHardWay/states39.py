states = {
	"Lucy": "Cedric",
	"Ennie": "Joyce",
	"Maria": "Putini",
	"Mamorake": "Danny",
	"Mavis": "Foster",
	"Isahai": "Koketso",
	"Oupa": "keMolebetse",
	"Nathaniel": None,
	"Junior": "Lethabo",
}

cities = {
	1: "Johannesburg",
	2: "Cape Town",
	3: "Durban",
	4: "Germiston",
	5: "Pretoria",
	6: "Port Elizabeth",
	7: "East London",
	8: "Bloemfontein"
}

cities[9] = "Soweto"
cities[10] = "Pietermaritzburg"

print("-"*10)
print("Lucy's firsborn is: ", states["Lucy"])
print("Nathaniel's firsborn is: ", states["Nathaniel"])


print("-"*10)
for i, city in list(cities.items()):
	print(f"{i} has the city {city}")
