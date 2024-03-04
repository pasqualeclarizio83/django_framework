Progetto:

django-admin startproject ebooksapi

ebooksapi


python manage.py startapp ebooks


dopo aver scritto i serializers, possiamo scrivere le nostre API views:


from rest_framework import serializers
from ebooks.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"




ebooks -> api -> urls.py

from django.urls import path
from ebooks.api.views import (EbookDetailAPIView, EbookListCreateAPIView,
                              ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    path("ebooks/", 
         EbookListCreateAPIView.as_view(), 
         name="ebook-list"),

    path("ebooks/<int:pk>/", 
         EbookDetailAPIView.as_view(), 
         name="ebook-detail"),

    path("ebooks/<int:ebook_pk>/review/", 
         ReviewCreateAPIView.as_view(), 
         name="ebook-review"),

    path("reviews/<int:pk>/", 
         ReviewDetailAPIView.as_view(), 
         name="review-detail")
]

Lista Vuota!!!!


Accesso:

http://127.0.0.1:8000/api/ebooks/



http://127.0.0.1:8000/api/ebooks/1/









