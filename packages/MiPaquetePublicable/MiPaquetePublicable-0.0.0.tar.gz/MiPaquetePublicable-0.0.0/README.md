# Módulo de Cálculos Matemáticos Elementales

Este módulo proporciona diversas funciones para realizar cálculos matemáticos elementales, incluyendo operaciones de suma, resta, multiplicación, división decimal y división entera.

## Uso

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosElementales` desde `elementales` y llama a los métodos estáticos correspondientes.

```python
# from elementales.funciones_basicas import CalculosMatematicosElementales
from funciones_basicas import CalculosMatematicosElementales

# Ejemplo de uso del método de suma
resultado_suma = CalculosMatematicosElementales.suma(2, 3)
print(resultado_suma)  # Salida: El resultado de la SUMA 2.0 + 3.0 es 5.0

# Ejemplo de uso del método de resta
resultado_resta = CalculosMatematicosElementales.resta(10, 5)
print(resultado_resta)  # Salida: El resultado de la RESTA 10.0 - 5.0 es 5.0

# Ejemplo de uso del método de multiplicación
resultado_multiplicacion = CalculosMatematicosElementales.multiplicacion(4, 3)
print(resultado_multiplicacion)  # Salida: El resultado de la MULTIPLICACION 4.0 * 3.0 es 12.0

# Ejemplo de uso del método de división decimal
resultado_division_decimal = CalculosMatematicosElementales.division_decimal(10, 3)
print(resultado_division_decimal)  # Salida: El resultado de la DIVISIÓN DECIMAL 10.0 / 3.0 es 3.3333333333333335

# Ejemplo de uso del método de división entera
resultado_division_entera = CalculosMatematicosElementales.division_entera(10, 3)
print(resultado_division_entera)  # Salida: El resultado de la DIVISIÓN ENTERA 10 // 3 es 3
```

## Métodos disponibles

A continuación se enumeran los métodos disponibles en la clase `CalculosMatematicosElementales`:

- `suma(x: float, y: float) -> float`: Realiza la suma de dos números.

- `resta(x: float, y: float) -> float`: Realiza la resta de dos números.

- `multiplicacion(x: float, y: float) -> float`: Realiza la multiplicación de dos números.

- `division_decimal(x: float, y: float) -> float`: Realiza la división decimal de dos números.

- `division_entera(x: int, y: int) -> int`: Realiza la división entera de dos números.

## Notas

- Recuerda que para utilizar este módulo, asegúrate de tener instalado Python.

- Los métodos `suma`, `resta`, `multiplicacion`, `division_decimal` y `division_entera` funcionan con números reales.

- La división decimal puede producir resultados con una precisión limitada en números decimales repetitivos.

# Módulo de Cálculos Matemáticos Compuestos Avanzados

Este módulo proporciona diversas funciones para realizar cálculos matemáticos compuestos avanzados, incluyendo operaciones de potencia, raíz cuadrada, logaritmo, piso, techo, factorial y multiplicación de números imaginarios.

## Uso

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosCompuestos` desde `compuestos` y llama a los métodos estáticos correspondientes.

```python
# from compuestos.funciones_avanzadas import CalculosMatematicosCompuestos
from funciones_avanzadas import CalculosMatematicosCompuestos

# Ejemplo de uso del método de potencia
resultado_potencia = CalculosMatematicosCompuestos.potencia(2, 3)
print(resultado_potencia)  # Salida: El resultado de la POTENCIA 2 elevado a 3 es 8

# Ejemplo de uso del método de raiz cuadrada
resultado_raiz = CalculosMatematicosCompuestos.raiz_cuadrada(9, 16)
print(resultado_raiz)  # Salida: El resultado de la raiz cuadrada del valor absoluto de 9 + 16 es 5.0

# Ejemplo de uso del método de logaritmo
resultado_logaritmo = CalculosMatematicosCompuestos.logaritmo(10, 100)
print(resultado_logaritmo)  # Salida: El logaritmo del valor absoluto de 10 en base 100 es 0.5

# Ejemplo de uso del método de piso
resultado_piso = CalculosMatematicosCompuestos.piso(7, 2)
print(resultado_piso)  # Salida: El piso de 7 dividido 2 es 3

# Ejemplo de uso del método de techo
resultado_techo = CalculosMatematicosCompuestos.techo(7, 2)
print(resultado_techo)  # Salida: El techo de 7 dividido 2 es 4

# Ejemplo de uso del método de factorial
resultado_factorial = CalculosMatematicosCompuestos.factorial(5)
print(resultado_factorial)  # Salida: El factorial de 5 es 120

# Ejemplo de uso del método de multiplicación de números imaginarios
resultado_imaginarios = CalculosMatematicosCompuestos.imaginarios(2j, 3j)
print(resultado_imaginarios)  # Salida: La multiplicación del número imaginario 2j con el número imaginario 3j es -6
```

## Métodos disponibles

A continuación se enumeran los métodos disponibles en la clase `CalculosMatematicosCompuestos`:

- `potencia(x: float, y: float) -> float`: Calcula la potencia de x elevado a y.

- `raiz_cuadrada(x: float, y: float) -> float`: Calcula la raiz cuadrada del valor absoluto de (x + y).

- `logaritmo(x: float, y: float) -> float`: Calcula el logaritmo del valor absoluto de x en base y.

- `piso(x: float, y: float) -> int`: Calcula el piso de la división de x entre y.

- `techo(x: float, y: float) -> int`: Calcula el techo de la división de x entre y.

- `factorial(n: int) -> int`: Calcula el factorial de un número entero no negativo n.

- `imaginarios(x: complex, y: complex) -> complex`: Calcula la multiplicación de dos números imaginarios x e y.

## Notas

- Recuerda que para utilizar este módulo, asegúrate de tener instalado Python y el módulo math.

- Si el método `factorial` es llamado con un número entero negativo, se lanzará una excepción `ValueError`.

- Los métodos `piso` y `techo` devuelven resultados como enteros.

- El método `imaginarios` opera con números imaginarios utilizando el operador `*`.

- Si deseas más detalles sobre cada método, consulta la documentación en el código fuente.

- Para ejecutar las pruebas unitarias, puedes utilizar el framework `unittest` o `pytest` y verificar que cada método funcione correctamente.