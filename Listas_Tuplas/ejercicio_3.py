#Escribir un programa que almacene las asignaturas de un curso, ej. Matemáticas, Física, Química, Historia, y Lengua.
#En una lista, pregunte al usuario la nota que ha sacado en c/u, y dsp las muestre por pantalla con el msj
#"En <asignatura> has sacado <nota>", donde <asignatura> es c/u de las asignaturas de la lista y <nota> c/u
#De las correspondientes notas introducidas por el usuario

diccionario = {
    'Matemáticas': 0, 
    'Física': 0, 
    'Química': 0, 
    'Historia': 0,
    'Lengua': 0
}
for materia in diccionario:
    nota_usuario = int(input(f'Qué nota sacaste en {materia} '))

    diccionario[materia] = nota_usuario
    print(f"En {materia} has sacado {nota_usuario}")

print(f"Boletín final: {diccionario}")