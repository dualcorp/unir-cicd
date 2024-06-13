import unittest
from unittest.mock import patch


import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    
    def test_power_with_positive_numbers(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(3, 2), 9)

    def test_power_with_zero_exponent(self):
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(-3, 0), 1)

    def test_power_with_negative_numbers(self):
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-3, 2), 9)

    def test_power_with_negative_exponent(self):
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)
        self.assertAlmostEqual(self.calc.power(-2, -2), 0.25)    

    
    


    # ajuste de pruebas de metodos existentes no considerados ================================================

    def test_restar_devuelve_resultado_correcto(self):
        # Verifica que la resta de dos números iguales sea cero
        self.assertEqual(0, self.calc.substract(2, 2), "Debería ser 0 al restar dos números iguales")
        # Verifica que la resta de un número menor a uno mayor sea negativa
        self.assertEqual(-4, self.calc.substract(2, 6), "Debería ser -4 al restar 2 de 6")
        # Verifica que la resta de un número mayor a uno menor sea positiva
        self.assertEqual(5, self.calc.substract(10, 5), "Debería ser 5 al restar 5 de 10")
        # Verifica que la resta de un minuendo negativo y un sustraendo positivo sea más negativa
        self.assertEqual(-10, self.calc.substract(-5, 5), "Debería ser -10 al restar 5 de -5")



    def test_check_type_with_invalid_type(self):
        # Test para verificar que el tipo de los parámetros sea correcto
        with self.assertRaises(TypeError, msg="Debería lanzar TypeError con tipos de datos no numericos"):
            self.calc.check_type("string")


    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    @patch('app.util.validate_permissions', return_value=False)
    def test_multiply_no_permissions(self, mock_validate_permissions):
        with self.assertRaises(InvalidPermissions, msg="Debería lanzar una excepción si no hay permisos"):
            self.calc.multiply(2, 3)    



    


    # codigo nuevo  =================================================

    def test_raiz_cuadrada_returns_correct_result(self):
        self.assertEqual(4, self.calc.raiz_cuadrada(16))
        self.assertEqual(3, self.calc.raiz_cuadrada(9))

    def test_raiz_cuadrada_fails_with_negative_parameter(self):
        self.assertRaises(ValueError, self.calc.raiz_cuadrada, -1)

    def test_logaritmo_base_diez_returns_correct_result(self):
        self.assertAlmostEqual(2, self.calc.logaritmo_base_diez(100))
        self.assertAlmostEqual(1, self.calc.logaritmo_base_diez(10))

    def test_logaritmo_base_diez_fails_with_non_positive_parameter(self):
        self.assertRaises(ValueError, self.calc.logaritmo_base_diez, 0)
        self.assertRaises(ValueError, self.calc.logaritmo_base_diez, -10)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
