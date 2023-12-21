from django.urls import path
from .views import home_page, about_page

urlpatterns = [
    path('', home_page, name="home"),
    path('aboutfgksdjfkldsjfk/', about_page, name="about")

]