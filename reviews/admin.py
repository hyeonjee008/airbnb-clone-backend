from typing import Any
from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class GoodBadFilter(admin.SimpleListFilter):
    title = "만족도 필터"

    parameter_name = "goodbad"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        goodbad = self.value()
        if goodbad == "good":
            return reviews.filter(rating__gte=3)
        elif goodbad == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        GoodBadFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
