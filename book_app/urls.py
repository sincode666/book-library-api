from django.urls import path
from .views import add_show_books,get_by_id,delete_records,patch_using,replace
urlpatterns=[
    path('books/',add_show_books),
    path('book/<int:id>/',get_by_id),
    path('books/<int:id>/replace/',replace),
    path('books/<int:id>/patch/',patch_using),
    path('books/<int:id>/delete/',delete_records),

]
