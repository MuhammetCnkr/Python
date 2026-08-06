from my_library.sayings.py import hello


"""
eğer bulunduğun dizinde kendine bir package yapmak istersen altına bir folder aç (package_name) onun içine de modüllerinin
olduğu python dosyaları aç (içinde bir tane __init__.py açman lazım ki python onun bir library olduğunu anlasın).
mesela folder => file_1.py file_2.py olsun. file_1.py de 3 tane fonksiyon yaz tanımla.
bunu normal dizinden kullanmak için 'from package_name.file_1.py import <function_name>' yapabilirsin.
"""
