import sys
from sayings.py import hello
"""
knk bir py dosyasını library yapacaksan orada main çalıştırma no matter sadece bir fonksiyon from ettiğin python
direkt o py dosyasını baştan sonra okur ve main() varsa onu çalıştırır so sadece functionların olduğu py dosyası yap
"""
if len(sys.argv) == 2:
    hello(sys.argv[1])
# * yukarıda sayings.py içinden sadece hello functionu çalıştırılır



