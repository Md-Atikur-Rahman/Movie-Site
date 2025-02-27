from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import re_path

from authentication import views as auth_app
from .views import dashboard

from movie import views as movie_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_dashboard'),
    path('captcha/', include('captcha.urls')),

    # auth
    path('auth/login', auth_app.user_login, name='login'),
    path('auth/logout', auth_app.user_logout, name='logout'),
    #     path('auth/create', auth_app.register, name='register'),
    path('auth/forget-password/', auth_app.ForgetPassword, name="forget_password"),
    path('auth/change-password/<token>/',
         auth_app.ChangePassword, name="change_password"),
    path('auth/change-user-password/',
         auth_app.ChangePasswordByUser, name="change_user_password"),
    path('auth/update-profile/',
         auth_app.update_profile, name="update_profile"),


    # movie
    path('movie/add_movie/',
         movie_view.add_movie, name="add_movie"),
    path('movie/movie_detail/<int:movie_id>/',
         movie_view.movie_detail, name="movie_detail"),

    #     # Ststem Admin
    #     #     path('system_admin/add_vehicle/', waste_app.add_vehicle, name="add_vehicle"),

    #     # STS Manager
    #     path('sts_manager/transfer_waste/start',
    #          waste_app.waste_transfer_start, name="waste_transfer_start"),

    #     path('sts_manager/transfer_waste/start_complete',
    #          waste_app.waste_transfer_start_complete, name="waste_transfer_start_complete"),

    #     path('sts_manager/transfer_waste/complete/<int:transfer_id>',
    #          waste_app.waste_transfer_complete, name="waste_transfer_complete"),

    #     path('sts_manager/transfer_waste/create_fleet_step_1',
    #          waste_app.create_fleet_step_1, name="create_fleet_step_1"),

    #     path('sts_manager/transfer_waste/create_fleet_step_2',
    #          waste_app.create_fleet_step_2, name="create_fleet_step_2"),


    #     # landfill manager
    #     path('landfill_manager/transfer_waste/dump_start/<int:transfer_id>',
    #          waste_app.waste_transfer_start_dumping, name="waste_transfer_start_dumping"),
    #     path('landfill_manager/transfer_waste/dump_end/<int:transfer_id>',
    #          waste_app.waste_transfer_end_dumping, name="waste_transfer_end_dumping"),
    #     path('landfill_manager/transfer_waste/report/<int:transfer_id>',
    #          waste_app.waste_transfer_generate_bill, name="waste_transfer_generate_bill"),

    #     #     path('sts_manager/transfer_waste/edit/<int:transfer_id>',
    #     #          waste_app.edit_waste_transfer, name="edit_waste_transfer"),


    path('', dashboard, name='dashboard'),

]


# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
