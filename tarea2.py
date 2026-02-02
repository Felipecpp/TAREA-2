"""Programa para registrar alumnos y notas."""

alumnos = {}

while True:
    try:
        cantidad = int(input("¿Cuántos alumnos vas a introducir?: "))
        break
    except ValueError:
        print("Entrada inválida. Introduce un número entero.")

for indice in range(1, cantidad + 1):
    while True:
        nombre = input(f"Nombre del alumno {indice}: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    if nombre in alumnos:
        print(f"Error: el alumno '{nombre}' ya existe.")
        raise SystemExit(1)

    notas = []
    while True:
        try:
            nota = int(
                input(
                    f"Introduce una nota para {nombre} (número negativo para terminar): "
                )
            )
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")
            continue

        if nota < 0:
            break
        notas.append(nota)

    alumnos[nombre] = notas

print("\nLista de alumnos y su nota media:")
for nombre, notas in alumnos.items():
    if notas:
        media = sum(notas) / len(notas)
    else:
        media = 0.0
    print(f"- {nombre}: {media:.2f}")
