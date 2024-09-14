from django.contrib import admin
from django.urls import path, include
from main.views import landing_page, branch_login, branch_home, manage_students, add_student, delete_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('branch_login/', branch_login, name='branch_login'),
    path('branch_home/', branch_home, name='branch_home'),
    path('manage_students/', manage_students, name='manage_students'),
    path('add_student/', add_student, name='add_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
]
