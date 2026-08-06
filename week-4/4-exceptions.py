#ValueError: invalid literal for int() with base 10: '' #buradaki base 10 decimal sistem demek
#NameError: name 'x' is not defined. bu hata seninle ilgili x variable'ı tanımlanmamış
#Syntax errors generally mean you should double-check that you typed your code correctly.
#Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead.
#Your program may throw an error because of this unexpected input from the user.
#KeyError: istenilen key dictte keylerde bulunmazsa meydana gelir
"""
print("163" * 14314432454)
yukarıdaki gibi işlem yapmak istediğinde memoryError alırsın çünkü çarpma işlemi yapmaz sadece stringi o defa
ekrana yazar
"""


try: #hatanın gelebileceği kod satırı bu blokta
    x = int(input("x: ")) #burada hata olursa direkt except'e bakar
except ValueError: #ValueError olursa bunu yap anlamında
    print("x is not an integer")
else: #else bloğu try ile ilişkili except ile değil yani try'da hata olmazsa direkt else geçer olursa zaten except'e geçer
    print(f"x is {x}")

#doğru girilirse try ve except sıkıntı çıkarmaz else çalışır, yanlış girilirse excepte varsa ona geçilir except işlemi yapılır stop edilir (else çalıştırılmaz)
#print else'in içinde olmaz ise ve integer girilmezse int() o inputu integera çeviremez ve asign yapamaz böyle bir durumda x is not defined



while True:
    try:
        x = int(input("x: "))
        #break #bu kısma break koyman sıkıntı çıkarmaz zaten yukarıda int() hata çıkarırsa direkt except'e atılıyor program.
        #burada break yaparsan else bloğuna gerek kalmaz zaten hata olmazsa try ile aynı hizada olanlara uğramaz bir alt tab'a geçer
    except ValueError: #except bloğu çalıştığı zaman işlemini yapar ve while tekrar başlar
        print("x is not an integer")
    else:
        break
print(x)





def main():
    x = get_int()
    print(x)
def get_int():
    while True:
        try:
        x = int(input("x: ")) #return int(input("x: ")) #bu da burada kullanılabilir
            return x # burada kullanılabilir
        except ValueError:
            print("x is not an integer")
        else:
            break #return x burada break yerine kullanılabilir ve x'i return edir
    return x
main()





#We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying our code as follows
get_int("what is x? ")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) #bir hata çıkmazsa return yapar ve while breaklenir
        except ValueError:
            pass #bu başa yollar tekrar veri ister mesaj yazmana gerek kalmaz






def get_pace(miles,minutes):
    if not minutes > 0:
        raise Exception()
#yukarıda raise ValueError kullanman daha iyi olur daha detaylı
#ayrıca biraz açıklamalı error vermek istersen raise ValeuError("Invalid minutes.") şeklinde açıklamalı da yapabilirsin
    return miles / minutes

get_pace(miles=45.8, minutes=0)
# * yukarıdaki gibi çalıştırma yaparsan Exception() adında sana error yollar açıklama falan bulunmaz.




""""
breakpoints in vscode means that it helps you to figure out what happens each of lines
to use breakpoints in vscode click the left of the line number, kırmızı bir nokta göreceksin ona tıklaman lazım
bu işlemlerden sonra run and debug kısmını çalıştırman lazım soldaki sidebardan

bu brekapointler sayesinde aslında pythonun kodu nasıl satır satır okudğunu izleyebilir hafızaya variableları nasıl yazdığını görebilirsin
sidebarda local global değişkenleri vs görebilirsin
"""
