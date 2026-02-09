from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

# Radius of the sphere
r = Decimal("10")

# High-precision pi
getcontext().prec = 110
pi_full = Decimal(
    "3.14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
)

# Surface area formula: A = 4πr²
def surface_area(pi_value):
    return Decimal(4) * pi_value * r * r

decimal_places = [20, 40, 60, 100]

for d in decimal_places:
    getcontext().prec = d + 5

    # Truncation
    pi_trunc = pi_full.quantize(Decimal(1).scaleb(-d), rounding=ROUND_DOWN)
    area_trunc = surface_area(pi_trunc)

    # Rounding
    pi_round = pi_full.quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    area_round = surface_area(pi_round)

    # Difference
    difference = abs(area_round - area_trunc)

    # Convert difference to full decimal string
    difference_decimal = f"{difference:.100f}".rstrip('0')  # show up to 50 decimals for clarity

    print("=" * 70)
    print(f"Precision: {d} decimal places")
    print(f"Truncated pi = {pi_trunc}")
    print(f"Surface Area (Truncation) = {area_trunc}")
    print(f"Rounded pi = {pi_round}")
    print(f"Surface Area (Rounding) = {area_round}")
    print(f"Difference = {difference}  (decimal form: {difference_decimal})")
