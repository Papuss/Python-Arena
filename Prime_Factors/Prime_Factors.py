__author__ = 'Gazdik_Zsolt'

class Prime_factor(object):
    @staticmethod
    def generate(n):
        primes = []
        canditate = 2
        while n>1:
            while n % canditate == 0:
                primes.append(canditate)
                n //= canditate
            canditate += 1
        if n>1:
            primes.append(n)

        return primes
