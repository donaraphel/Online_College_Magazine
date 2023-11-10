from django.apps import AppConfig

print("Debug: The apps.py file is being executed.")

class CollegeMagazineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_magazine_app'
