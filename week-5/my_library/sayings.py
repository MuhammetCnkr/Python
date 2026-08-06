def main():
    hello("Muhammet")
    goodbye("Muhammet")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()


#bu yukarıdaki özel bir durum sen burada main çalışması için sadece cli'dan çalıştırılsa çalıştır diyorsun
#bir library import yaparsan main kısmı çalıştırılmaz.
#tekrar main() yapmana gerek yok
