"""
Task 2: Login Verification System

Koşul & Karar Tablosu:
| Kullanıcı Var mı? | Şifre Doğru mu? | Sonuç            |
|-------------------|------------------|-------------------|
| ❌ Hayır          | -               | "User not found"  |
| ✅ Evet           | ❌ Hayır         | "Wrong password"  |
| ✅ Evet           | ✅ Evet          | "Login successful"|
"""

# Kullanıcılar
users = {
    "admin": "admin123",
    "user": "pass456"
}

# Doğrulama fonksiyonu
def verify_login(username: str, password: str) -> str:
    if username not in users:
        return "User not found"
    elif users[username] != password:
        return "Wrong password"
    else:
        return "Login successful"

# Test
print(verify_login("admin", "admin123"))  # ✅ Login successful
print(verify_login("admin", "wrong"))     # ❌ Wrong password
print(verify_login("ghost", "test"))      # ❌ User not found
