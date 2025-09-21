def caesar_cipher(text, shift):
    """
    Реализация шифра Цезаря

    Args:
        text (str): передаваемый текст для шифрования
        shift (int): величина сдвига (положительная - шифрование, отрицательная дешифрование)
    """
    wheel = ([chr(i) for i in range(32, 127)] + [chr(i) for i in range(1040, 1104)]) #Колесо символов
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

def encrypt(text, id = 70212446):
    shift = id % 11
    return caesar_cipher(text, shift)

def decrypt(text, id = 70212446):
    shift = id % 11
    return caesar_cipher(text, -shift)

