# Yöntem 1: Homoglif (Aynı görünen farklı Unicode rakamları)
def make_homoglyph(phone_str):
    # Standard 0-9 rakamlarını Mathematical Monospace karşılıklarına eşler
    mapping = str.maketrans("0123456789", "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫")
    return phone_str.translate(mapping)

# Yöntem 2: Zero-Width Space gizleme
def make_invisible_split(phone_str):
    zws = "\u200B"  # Görünmez karakter
    return zws.join(phone_str)

numara = "05368141575"

print("Homoglif:", make_homoglyph(numara))
print("Görünmez karakterli:", make_invisible_split(numara))