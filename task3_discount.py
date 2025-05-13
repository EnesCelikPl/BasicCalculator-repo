"""
Task 3: Product Discount Eligibility

Koşul Tablosu:
| is_vip | purchase_total > 1000 | İndirim |
|--------|------------------------|----------|
| False  | False                 | 0.0      |
| False  | True                  | 0.05     |
| True   | False                 | 0.1      |
| True   | True                  | 0.2      |
"""

def get_discount(is_vip: bool, purchase_total: float) -> float:
    if is_vip and purchase_total > 1000:
        return 0.2
    elif is_vip:
        return 0.1
    elif purchase_total > 1000:
        return 0.05
    else:
        return 0.0

# Test
print(get_discount(True, 1200))   # 0.2
print(get_discount(True, 800))    # 0.1
print(get_discount(False, 1500))  # 0.05
print(get_discount(False, 600))   # 0.0
