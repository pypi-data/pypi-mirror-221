class CalculosMatematicosElementales:

    @staticmethod
    def suma(x: float, y: float) -> float:
        """
        Realiza la suma de dos números.

        Parameters:
            x (float): Primer número a sumar.
            y (float): Segundo número a sumar.

        Returns:
            float: Resultado de la suma.
        """
        print(f'El resultado de la SUMA {x} + {y} es {x + y}')
        return x + y

    @staticmethod
    def resta(x: float, y: float) -> float:
        """
        Realiza la resta de dos números.

        Parameters:
            x (float): Número al que se le restará el otro número.
            y (float): Número que se restará al primer número.

        Returns:
            float: Resultado de la resta.
        """
        print(f'El resultado de la RESTA  {x} - {y} es {x - y}')
        return x - y
    
    @staticmethod
    def multiplicacion(x: float, y: float) -> float:
        """
        Realiza la multiplicación de dos números.

        Parameters:
            x (float): Primer número a multiplicar.
            y (float): Segundo número a multiplicar.

        Returns:
            float: Resultado de la multiplicación.
        """
        print(f'El resultado de la MULTIPLICACION  {x} * {y} es {x * y}')
        return x * y
    
    @staticmethod
    def division_decimal(x: float, y: float) -> float:
        """
        Realiza la división decimal de dos números.

        Parameters:
            x (float): Número que se dividirá.
            y (float): Número por el cual se dividirá.

        Returns:
            float: Resultado de la división decimal.
        """
        print(f'El resultado de la DIVISIÓN DECIMAL {x} / {y} es {x / y}')
        return x / y
    
    @staticmethod
    def division_entera(x: int, y: int) -> int:
        """
        Realiza la división entera de dos números.

        Parameters:
            x (int): Número que se dividirá.
            y (int): Número por el cual se dividirá.

        Returns:
            int: Resultado de la división entera.
        """
        print(f'El resultado de la DIVISIÓN ENTERA {x} // {y} es {x // y}')
        return x // y