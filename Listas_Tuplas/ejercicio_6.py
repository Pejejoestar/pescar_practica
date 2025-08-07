#Escribir un programa que almacene las asignaturas de un curso, ej. Matemáticas, Física, Química, Historia, y Lengua.
#En una lista, pregunte al usuario la nota que ha sacado en c/ asignatura y elimine de la lista las asignaturas aprobadas.
#Al final del programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

listado_materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

diccionario = {
    'Matemáticas': 0, 
    'Física': 0, 
    'Química': 0, 
    'Historia': 0,
    'Lengua': 0
}
for materia in listado_materias:
    nota_usuario = int(input(f'Qué nota sacaste en {materia} '))

    diccionario[materia] = nota_usuario
    if diccionario[materia] >= 6:
        del diccionario[materia]
        print(f"Materia aprobada")

print(f"Materias recursadas: {diccionario}")