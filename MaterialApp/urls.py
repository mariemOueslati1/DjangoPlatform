from django.urls import path
from .views import *

urlpatterns = [

    # Add other URL patterns as needed
    path('materials/add/<int:course_id>/', AddMaterialView.as_view(), name='add-material'),
    path('materials/<int:pk>/update/', UpdateMaterialView.as_view(), name='update-material'),
    path('materials/<int:material_id>/delete/', DeleteMaterialView.as_view(), name='delete-material'),
    path('materials/materialsList/<int:course_id>/',ListMaterialView.as_view(), name='material-list'),
    path('materials/materialsDetails/<int:material_id>/',MaterialDetailView.as_view(), name='material-list-details'),
    path('materials/<int:material_id>/download/', MaterialDownloadView.as_view(), name='material_download'),
    path('materials/<int:material_id>/read/', MaterialReadView.as_view(), name='material_read'),
]
