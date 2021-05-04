from django.urls import path
from scmapp import views

app_name = 'scmapp'

urlpatterns = [
    path('',views.index),

    path('atest',views.atest,name='atest'),
    

    path('login',views.admin_login,name='admin_login'),
    path('login_admin',views.login_admin,name='login_admin'),

    path('admin_home',views.admin_home,name='admin_home'),

    path('admin_event',views.admin_event,name='admin_event'),



    path('admin_search',views.admin_search,name='admin_search'),#search event

    path('latest',views.latest,name='latest'),#search event




    path('update_event/<int:id>',views.update_event,name='update_event'),
    path('db_update_event/<int:id>',views.db_update_event,name='db_update_event'),
    path('db_delete_event/<int:id>',views.db_delete_event,name='db_delete_event'),

    path('add_event',views.add_event,name='add_event'),
    path('db_add_event',views.db_add_event,name='db_add_event'),

    # path('user_logout',views.user_logout,name='user_logout'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
]
