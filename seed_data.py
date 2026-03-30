# seed_data.py

import os
import django
from django.utils.text import slugify
from django.utils import timezone

# Django sozlamalarini ulash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post   # app nomini moslab oling

def run():
    user = User.objects.first()

    if not user:
        print("❌ Avval kamida bitta User yarating")
        return

    it_posts = [
        {
            "title": "Python dasturlash tiliga kirish",
            "body": "Python — sodda va kuchli dasturlash tili. U web, AI va data sohalarda keng qo‘llaniladi."
        },
        {
            "title": "Django nima va nega u mashhur",
            "body": "Django — bu tez va xavfsiz web ilovalar yaratish uchun mo‘ljallangan framework."
        },
        {
            "title": "REST API nima?",
            "body": "REST API frontend va backend o‘rtasida ma’lumot almashish uchun ishlatiladi."
        },
        {
            "title": "Frontend va Backend farqi",
            "body": "Frontend — foydalanuvchi ko‘radigan qism, Backend esa server tomoni hisoblanadi."
        },
        {
            "title": "Git va GitHub bilan ishlash",
            "body": "Git — versiya nazorati tizimi, GitHub esa kodlarni saqlash platformasi."
        },
        {
            "title": "Sun’iy intellekt (AI) asoslari",
            "body": "AI kompyuterlarni aqlli qarorlar qabul qilishga o‘rgatadi."
        },
        {
            "title": "Machine Learning nima?",
            "body": "Machine Learning — ma’lumotlar asosida o‘rganadigan algoritmlar to‘plami."
        },
        {
            "title": "Docker nima uchun kerak?",
            "body": "Docker ilovalarni konteynerlarda ishga tushirishga yordam beradi."
        },
        {
            "title": "Linux dasturchilar uchun",
            "body": "Linux — serverlar va dasturchilar orasida eng mashhur OS."
        },
        {
            "title": "PostgreSQL vs MySQL",
            "body": "Ikkalasi ham kuchli DB, ammo PostgreSQL murakkab loyihalar uchun qulayroq."
        },
        {
            "title": "API xavfsizligi",
            "body": "Token, JWT va OAuth API’larni himoyalashda ishlatiladi."
        },
        {
            "title": "Clean Code nima?",
            "body": "Toza kod — o‘qilishi va tushunilishi oson bo‘lgan koddir."
        },
        {
            "title": "Microservices arxitekturasi",
            "body": "Katta ilovalarni kichik servislar orqali qurish usuli."
        },
        {
            "title": "Django ORM afzalliklari",
            "body": "ORM orqali SQL yozmasdan DB bilan ishlash mumkin."
        },
        {
            "title": "Celery va Background tasklar",
            "body": "Celery og‘ir vazifalarni fon rejimida bajaradi."
        },
        {
            "title": "Redis nima?",
            "body": "Redis — tezkor xotira asosidagi ma’lumotlar ombori."
        },
        {
            "title": "CI/CD tushunchasi",
            "body": "CI/CD kodni avtomatik test va deploy qilish jarayoni."
        },
        {
            "title": "Backend dasturchi bo‘lish yo‘li",
            "body": "Python, Django, DB va API bilish muhim."
        },
        {
            "title": "Web ilova optimizatsiyasi",
            "body": "Keshlash va query optimizatsiyasi tezlikni oshiradi."
        },
        {
            "title": "Dasturchilar uchun maslahatlar",
            "body": "Har kuni kod yozing va yangi texnologiyalarni o‘rganing."
        },
    ]

    posts = []

    for post in it_posts:
        posts.append(
            Post(
                title=post["title"],
                slug=slugify(post["title"]),
                author=user,
                body=post["body"],
                publish=timezone.now(),
                status=Post.Status.PUBLISHED
            )
        )

    Post.objects.bulk_create(posts)
    print("✅ IT mavzusida 20 ta turli post qo‘shildi")

if __name__ == "__main__":
    run()
