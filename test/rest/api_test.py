import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )



    def test_api_raiz_cuadrada(self):
        url = f"{BASE_URL}/calc/raiz_cuadrada/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '4.0')

    def test_api_logaritmo_base_diez(self):
        url = f"{BASE_URL}/calc/logaritmo_base_diez/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '2.0')

    def test_api_logaritmo_base_diez_error(self):
        url = f"{BASE_URL}/calc/logaritmo_base_diez/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("HTTPError not raised")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

        
    # =============== codigo nuevo aqui =============


    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '2')

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/4/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '12')

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '5.0')

    def test_api_divide_para_Cero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("HTTPError not raised")  # Esto se ejecuta si no se levanta ninguna excepción
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)  # valida estado HTTP es 400

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), '8')

    def test_api_power_con_numero_invalido(self):
        url = f"{BASE_URL}/calc/power/two/three"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.BAD_REQUEST)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)



    def test_api_raiz_cuadrada_negativo(self):        
        url = f"{BASE_URL}/calc/raiz_cuadrada/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.BAD_REQUEST)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)


    def test_api_ruta_no_existe(self):
        url = f"{BASE_URL}/calc/no_existe/6"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            
            self.fail("HTTPError not raised")
        except HTTPError as e:            
            self.assertEqual(e.code, http.client.NOT_FOUND)


    def test_api_multiply_demuestra_fallo(self):
        # Asume que cambias el permiso a otro usuario para esta prueba
        url = f"{BASE_URL}/calc/multiply/5/6"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("HTTPError not raised")  
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)  
            expected_error_msg = "User has no permissions"
            self.assertIn(expected_error_msg, e.reason)  



        

  