from django.urls import path
from . import views


urlpatterns = [path('', views.show_main),
               path('panel/', views.show_panel),
               path('login/', views.login_user, name='login'),
               path('logout/', views.logout_user, name='logout'),
               path('panel/<str:pict_name>/<int:rect_id>', views.rect_delete),
               path('panel/<str:pict_name>', views.pict_modify),
               path("<str:pict_name>/", views.pict_site)]
