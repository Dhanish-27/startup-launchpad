from django.urls import path
from . import views

app_name="altruisty"

urlpatterns=[
    path("services/",views.services,name="services"),
    path("details/<str:heading>/",views.DetailsPage,name="details"),
    path("",views.home,name="index"),
    path("about/",views.aboutus,name="about"),
    path("internship/",views.registerdataintern,name="intern"),
    path("verify/",views.verify,name="verify"),
     path("register_mentor/",views.registerdatamentor,name="register_mentor"),
     path("register_elearning/",views.registerdataelearning,name="register_elearning"),
     path("register_internship/",views.registerdataintern,name="register_internship"),
    path("contact/",views.contact,name="contact"),
    path("e-learning/",views.registerdataelearning,name="E-learning"),
    path("mentor_registration/",views.registerdatamentor,name="Mentorform"),
    path("startup_registration/",views.registerdatastartup,name="Startupform"),
    path("college_registration/",views.registerdatacollege,name="CollegeForm"),
    path('payment/<str:id>/', views.qr_page, name='payment'),
    path('payment/qr/<str:price>/', views.upi_qr_view, name='upi_qr'),
    path('payment/submit/<str:id>/', views.submit_payment, name='submit_payment'),
    path("coupon-check/<str:id>/", views.coupon_check, name="coupon_check"),
   
    ]