import string 
def caesar_cipher(text, shift):
    """
    Реализация шифра Цезаря

    Args:
        text (str): передаваемый текст для шифрования
        shift (int): величина сдвига (положительная - шифрование, отрицательная дешифрование)
    """
    wheel = (string.digits + [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)] + string.ascii_letters +string.punctuation + ' ' ) #Колесо символов
    result = []
    wheel_size = len(wheel)
    
    for char in text:
        if char in wheel:
            cur_index = wheel.index(char) # Текущий индекс символа в колесе
            new_index = (cur_index + shift) % wheel_size #Вычисленный новый индекс с учетом размера колеса
            if new_index < 0:
                new_index += wheel_size
            result.append(wheel[new_index])
        else:
            result.append(char)
    return ''.join(result)

def encrypt(text, sid = 70212446):
    shift = sid % 11
    return caesar_cipher(text, shift)

def decrypt(text, sid = 70212446):
    shift = sid % 11
    return caesar_cipher(text, -shift)

