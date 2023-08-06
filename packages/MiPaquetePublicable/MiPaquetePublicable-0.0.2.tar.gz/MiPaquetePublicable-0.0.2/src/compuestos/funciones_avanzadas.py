import math

class CalculosMatematicosCompuestos:
    @staticmethod
    def potencia(x: float, y: float) -> float:
        """
        Calcula la potencia de x elevado a y y muestra el resultado.

        Parameters:
            x (float): El número base.
            y (float): El exponente.

        Returns:
            float: El resultado de la potencia.
        """
        print(f'El resultado de la POTENCIA {x} elevado a {y} es {x ** y}')
        return x ** y

    @staticmethod
    def raiz_cuadrada(x: float, y: float) -> float:
        """
        Calcula la raiz cuadrada del valor absoluto de (x + y) y muestra el resultado.

        Parameters:
            x (float): Primer número.
            y (float): Segundo número.

        Returns:
            float: El resultado de la raiz cuadrada.
        """
        print(f'El resultado de la raiz cuadrada del valor absoluto de {x} + {y} es {math.sqrt(abs(x + y))}')
        return math.sqrt(abs(x + y))

    @staticmethod
    def logaritmo(x: float, y: float) -> float:
        """
        Calcula el logaritmo del valor absoluto de x en base y y muestra el resultado.

        Parameters:
            x (float): El número del cual se calculará el logaritmo.
            y (float): La base del logaritmo.

        Returns:
            float: El resultado del logaritmo.
        """
        print(f'El logaritmo del valor absoluto de {x} en base {y} es {math.log(abs(x), abs(y))}')
        return math.log(abs(x), abs(y))

    @staticmethod
    def piso(x: float, y: float) -> int:
        """
        Calcula el piso de la división de x entre y y muestra el resultado.

        Parameters:
            x (float): Numerador.
            y (float): Denominador.

        Returns:
            int: El resultado del piso.
        """
        print(f'El piso de {x} dividido {y} es {math.floor(x / y)}')
        return math.floor(x / y)

    @staticmethod
    def techo(x: float, y: float) -> int:
        """
        Calcula el techo de la división de x entre y y muestra el resultado.

        Parameters:
            x (float): Numerador.
            y (float): Denominador.

        Returns:
            int: El resultado del techo.
        """
        print(f'El techo de {x} dividido {y} es {math.ceil(x / y)}')
        return math.ceil(x / y)

    @staticmethod
    def factorial(n: int) -> int:
        """
        Calcula el factorial de un número entero no negativo (n).

        Parameters:
            n (int): El número entero del cual se calculará el factorial.

        Returns:
            int: El resultado del factorial de n.

        Raises:
            ValueError: Si n es un número entero negativo.

        Examples:
            >>> factorial(5)
            El factorial de 5 es 120
            120

            >>> factorial(0)
            El factorial de 0 es 1
            1

            >>> factorial(10)
            El factorial de 10 es 3628800
            3628800

        Note:
            El factorial de un número entero no negativo n (representado por n!) es el producto
            de todos los enteros positivos desde 1 hasta n. Por convención, se define que el
            factorial de 0 es 1.
        """
        if n < 0:
            raise ValueError("El factorial solo está definido para números enteros no negativos.")
        
        print(f'El factorial de {n} es {math.factorial(n)}')
        return math.factorial(n)

    @staticmethod
    def imaginarios(x: complex, y: complex) -> complex:
        """
        Calcula la multiplicación de dos números imaginarios x e y y muestra el resultado.

        Parameters:
            x (complex): Primer número imaginario.
            y (complex): Segundo número imaginario.

        Returns:
            complex: El resultado de la multiplicación de los números imaginarios.
        """
        print(f'La multiplicación del número imaginario {x} con el número imaginario {y} es {x * y}')
        return x * y
