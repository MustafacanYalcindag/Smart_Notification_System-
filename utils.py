import random

def mesajhavuzu():
    havuz = ["Sisteme giriş yapıldı", "Yeni bildiriminiz var", "Güvenlik uyarısı!", "Mesaja bakınız"]
    mesaj = random.choice(havuz)
    return mesaj