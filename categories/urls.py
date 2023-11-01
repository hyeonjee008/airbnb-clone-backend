from django.urls import path
from . import views


# ModelViewSet 사용 시
urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]


# 기본 APIView 사용시 (ModelViewSet 사용 안할 시)
# urlpatterns = [
#     path("", views.Categories.as_view()),
#     path("<int:pk>", views.CategoryDetail.as_view()),
# ]
