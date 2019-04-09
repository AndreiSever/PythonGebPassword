

import unittest
import gener
 
class Test(unittest.TestCase):
    """
    Класс тестирования методов класса gen.
    """
    def test_gen(self):
        """
        Проверяет длину сгенерированного пароля.
        """
        clas=gener.gen()
        clas.len = 8
        lenPass = clas.genRandomSymbols() 
        self.assertEqual(len(lenPass), 8)
        
    def test_validate1(self):
        """
        Проверяет вхождение длины пароля в допустимый диапазон.
        """
        clas=gener.gen()
        self.assertEqual(clas.validat(8), True)
        
    def test_validate2(self):
        """
        Проверяет вхождение длины пароля в допустимый диапазон.
        """
        clas=gener.gen()
        self.assertEqual(clas.validat(60), True)
if __name__ == '__main__':
    unittest.main()
