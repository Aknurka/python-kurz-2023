jmeno = input("Zadejte prosím Vaše jméno: ")
print("Vaše jméno je " + jmeno)
email = jmeno.lower() + "@czechitas.cz"
print("Vytvořená emailová adresa: " + email)

jmeno_a_prijmeni = input("Zadejte vaše jméno a příjmení: ")

# Všechna písmena velká
print("Všechna písmena velká: " + jmeno_a_prijmeni.upper())

# Všechna písmena malá
print("Všechna písmena malá: " + jmeno_a_prijmeni.lower())

# Standardní varianta - první písmeno velké, další malá
print("Standardní varianta: " + jmeno_a_prijmeni.title())

# Iniciály
jmeno, prijmeni = jmeno_a_prijmeni.split()
print("Iniciály: " + jmeno[0].upper() + ". " + prijmeni[0].upper() + ".")

# Křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak standardní varianta.
if len(jmeno) > 5:
    jmeno = jmeno[0] + "."
print("Křestní jméno zkrácené na první písmeno a příjmení: " + jmeno.capitalize() + " " + prijmeni.capitalize())