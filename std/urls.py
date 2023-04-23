from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('home/',home),
    path('st-add/',add_std),
    path('delete-std/<int:roll>',delete_std),
    path('update-std/<int:roll>',update_std),
    path('do-update-std/<int:roll>',do_update_std),
    path('dis-map/',dis_map),
    path('dis/',dis),
    path('add-pt/',add_pt),
    path('delete-map/<int:gid>',delete_map),
    path('update-map/<int:gid>',update_map),
    path('do-update-map/<int:gid>',do_update_map),
]
