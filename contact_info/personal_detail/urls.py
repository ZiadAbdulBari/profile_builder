from django.urls import path
from personal_detail import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'personal_detail'

urlpatterns = [
    path('', views.contact_list, name = 'contact_list'),
    path('add_contact/', views.add_contact, name = 'addContact'),
    path('show_individual_contact/<int:contact_id>/', views.show_individual_contact, name = 'showIndividualContact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='deleteContact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='editContact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)