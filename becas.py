def leer_numero(mensaje):
    return float(input(mensaje));

def validar_datos(promedio, ingreso, reprobadas, activo):
    if promedio < 0 or promedio > 10:
        return False
    if ingreso < 0:
        return False
    if reprobadas < 0:
        return False
    if activo not in ["S", "N"]:
        return False
    return True

def clasificar(promedio, ingreso, reprobadas, activo):
    if promedio >= 9 and ingreso <= 500 and reprobadas == 0:
        return "Beca completa", "Promedio >= 9, ingreso <= 500, 0 reprobadas"

    # Beca parcial
    if reprobadas <= 1:
        if promedio >= 8 and ingreso <= 800:
            return "Beca parcial", "Promedio >= 8 e ingreso <= 800"
        if promedio >= 9 and ingreso <= 1000:
            return "Beca parcial", "Promedio >= 9 e ingreso <= 1000"

    return "Sin beca", "No cumple condiciones de beca completa ni parcial"

def main():
    totales = {
        "Dato inválido": 0,
        "Sin beca": 0,
        "Beca parcial": 0,
        "Beca completa": 0,
    }

    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre.upper() == "FIN":
            break

        promedio = leer_numero("Promedio académico (0-10): ")
        ingreso = leer_numero("Ingreso mensual familiar: ")
        reprobadas = leer_numero("Materias reprobadas: ")
        activo = input("Estudiante activo (S/N): ").strip().upper()

        if not validar_datos(promedio, ingreso, reprobadas, activo):
            resultado, razon = "Dato inválido", "Uno o más campos fuera de rango"
        else:
            resultado, razon = clasificar(promedio, ingreso, reprobadas, activo)

        totales[resultado] += 1
        print(f"  -> Resultado: {resultado} ({razon})")

    print("\n--- Totales ---")
    for categoria, cantidad in totales.items():
        print(f"{categoria}: {cantidad}")
        
if __name__ == "__main__":
    main()