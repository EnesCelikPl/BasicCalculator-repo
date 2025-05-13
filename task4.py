"""
Task 4: Age and Membership Validation

Koşul Tablosu:
| Age between 18–60? | Already a member? | Sonuç (is_eligible) |
|---------------------|-------------------|----------------------|
| ❌ Hayır            | ❌ Hayır          | False               |
| ❌ Hayır            | ✅ Evet           | False               |
| ✅ Evet             | ✅ Evet           | False               |
| ✅ Evet             | ❌ Hayır          | True                |
"""

def is_eligible(age: int, is_member: bool) -> bool:
    if age < 18 or age > 60:
        return False
    if is_member:
        return False
    return True

# Test örnekleri
print(is_eligible(25, False))  # True
print(is_eligible(25, True))   # False
print(is_eligible(17, False))  # False
print(is_eligible(61, False))  # False
