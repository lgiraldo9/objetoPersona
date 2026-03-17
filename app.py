from persona import LuisGiraldo

# Programa principal
def main():
    # Crear una lista para almacenar las personas
    personas = []

    # Crear una instancia de la clase Luis
    luis = LuisGiraldo("01", "123456789", "Luis", "Garcia", 30, 50000)
    sofia = LuisGiraldo("02", "987654321", "Sofia", "Lopez", 25, 45000)
    mario = LuisGiraldo("03", "456789123", "Mario", "Martinez", 28, 60000)
    guillermo = LuisGiraldo("04", "321654987", "Guillermo", "Sanchez", 35, 70000)
    ana = LuisGiraldo("05", "654987321", "Ana", "Gomez", 22, 40000)
    maria = LuisGiraldo("06", "987321654", "Maria", "Rodriguez", 27, 55000)
    # Agregar las personas a la lista
    personas.append(luis)
    personas.append(sofia)
    personas.append(mario)
    personas.append(guillermo)
    personas.append(ana)
    personas.append(maria)


    # Imprimir la informacion de cada persona en la lista
    print("Lista de personas:")
    # Imprimir la informacion de la persona en la posicion 5 (índice 4)
    print("\nInformacion de la persona en la posición 5:")
    persona = personas[5]
    print(f"id: {persona.get_id()}, Nombre: {persona.get_nombre()}, Apellido: {persona.get_apellido()}, Edad: {persona.get_edad()}, Sueldo: {persona.get_sueldo()}")

    print("\nInformacion de todas las personas en la lista:")
    # Imprimir la informacion de cada persona en la lista
    for persona in personas:
        print(f"id: {persona.get_id()}, Nombre: {persona.get_nombre()}, Apellido: {persona.get_apellido()}, Edad: {persona.get_edad()}, Sueldo: {persona.get_sueldo()}")


if __name__ == "__main__": 
    main()
    # Fin del programa