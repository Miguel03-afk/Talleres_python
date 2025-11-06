total_area = float(input("Ingrese el área total del terreno en metros cuadrados: "))

area_cultivos = total_area * 0.40
area_vivienda = total_area * 0.25
area_zonas_verdes = total_area * 0.15
area_otros = total_area - (area_cultivos + area_vivienda + area_zonas_verdes)

print(f"Área para cultivos: {area_cultivos} m²")
print(f"Área para construir vivienda: {area_vivienda} m²")
print(f"Área para zonas verdes: {area_zonas_verdes} m²")
print(f"Área disponible para otros proyectos: {area_otros} m²")
