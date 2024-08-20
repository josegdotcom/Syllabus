# Tarea 1: DCCultivo 🌱💧

```Desarrolla el archivo aquí utilizando lo estipulado en el archivo "README_inicial.md```

# Actualizaciones Tarea

> 13 de agosto

1. Se sube la tarea al repositorio Syllabus.
2. Se cambia y actualiza el Enunciado ya que se añadía una extensión .py innecesaria para el comando de ejecución de _tests_. Específicamente en la sección 6.1 Ejecución de _tests_.

    En cambio, si deseas ejecutar un subconjunto de _tests_, puedes hacerlo escribiendo lo siguiente:

    `python3 -m unittest -v -b tests_publicos.<test_N>`

    Reemplazando `<test_N>` por el test que desees probar

    Por ejemplo, si quisieras probar si realizaste correctamente el método crear_plano de Predio, deberás escribir lo siguiente:

    `python3 -m unittest -v -b tests_publicos.test_00_crear_plano`

> 19 de agosto

1. Se hace un cambio menor al enunciado, en la subsección __3.2.2 Menu de Acciones__. Para la acción Plantar del menú, se mencionaba ingresar `codigo_cultivo` como _str_, cuando es indiferente el tipo de dato ya que todos los datos ingresados con input() entran como _str_. Se precisa esto para eliminar confusiones en el enunciado de la siguiente forma:
    > Plantar: (...)Puedes asumir que el usuario ingresará correctamente los datos, es decir, entregará un número entero válido entre 0 y 9 para el parámetro de `codigo_cultivo` y dos números enteros positivos para los parámetros de `alto` y `ancho`. (...)