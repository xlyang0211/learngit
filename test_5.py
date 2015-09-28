__author__ = 'seany'

from decimal import Decimal

str_1 = "1.23e-12"
print str("%.10e" % (Decimal(str_1) * 10 ** 9))

a = [1, 2, 3]
print sum(a)