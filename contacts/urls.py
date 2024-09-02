from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_contact/', views.home_contact, name='home_contact'),
    path('signup/', views.signup, name='signup'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts_completed/', views.contacts_completed, name='contacts_completed'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:contact_id>/complete', views.complete_contact, name='complete_contact'),
    path('contacts/<int:contact_id>/delete', views.delete_contact, name='delete_contact'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]