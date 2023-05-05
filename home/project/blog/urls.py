
from django.urls import path
from blog import views

from django.contrib import admin
app_name = "blog"

urlpatterns = [
 path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("delete/<int:post_pk>/", views.delete, name="delete"),
    path(
        "delete_comment/<int:post_pk>/<int:comment_pk>/",
        views.delete_comment,
        name="delete_comment",
    ),
]