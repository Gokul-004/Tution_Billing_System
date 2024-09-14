from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('branch_login/', views.branch_login, name='branch_login'),
    path('branch_home/', views.branch_home, name='branch_home'),
    path('manage_students/', views.manage_students, name='manage_students'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]
