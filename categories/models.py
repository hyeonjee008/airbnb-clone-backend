from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:  # 관리자페이지에 Categorys로 자동 생성되는데, 표출이름 수동 설정
        verbose_name_plural = "Categories"
