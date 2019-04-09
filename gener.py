

# -*- coding: UTF-8 -*-
import os
import binascii
import string
class gen():
    """
    Класс для генерации пароля
    """
    def __init__(self):
        """
        Инициалирует переменные.

        Атрибуты
        --------
        passwordSymbols : string
            Алфавит для генерируемого пароля.
        len : int
            Длина пароля. (Значение 0)
        """
        self.passwordSymbols = string.ascii_letters+string.digits + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя;*()_+=-,.[]{}" 
        self.len = 0
    def genRandomSymbols(self):
        """
        Генерирует пароль.
        
        Возврат
        -------
        password : string
            Возвращает пароль.
        """
        password = ''
        for i in range(self.len):
            password += self.passwordSymbols[int(binascii.hexlify(os.urandom(1)),16) % len(self.passwordSymbols)]
        return password
    def validat(self,length):
        """
        Проверка на введеную длину пароля.
        
        Параметры
        ---------
        length : string
            Введенная длина пароля.
        
        Возврат
        -------
        bool
            Возвращает True.
        bool
            Возвращает False.
        """
        try:
            if int(length) not in range(8,61):
                return False
            return True
        except:
             return False
    def inp(self):
        """
        Вводится длина пароля.
        
        Ошибки
        ------
        validate
            Возникает если введено не число или находится вне диапазона.
        """
        validate = False
        while validate==False:
           password_length = input('Введите длину пароля(не менее 8 символов): ')
           validate = self.validat(password_length)
           if validate == False:
                print('Некорректный ввод!Введите число в диапазоне 8-60.') 
        self.len = int(password_length)        
    def main(self):
        """
        Основная функция, которая вызывает все остальные.
        """  
        self.inp()
        print(self.genRandomSymbols())
 
  
