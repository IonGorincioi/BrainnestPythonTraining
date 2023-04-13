# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

def pythagorean_triplet(n):
    for c in range(1, int(n/2)):
        for a in range(1, int(n/3)):
            b = n - c - a
            if a ** 2 + b ** 2 == c ** 2:
                abc_product = a * b * c

                return f"Pythagorean triplet product: {a} * {b} * {c} = {abc_product}"


# print(pythagorean_triplet(12))
print(pythagorean_triplet(1000))
