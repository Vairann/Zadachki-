class prakt:

    def add(self ,a, b):
        return a + b

    def divide(self ,a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def is_palindrome(self ,s):
        clean = ''.join(c.lower() for c in s if c.isalnum())
        return clean == clean[::-1]