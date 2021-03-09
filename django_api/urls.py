from rest_framework.routers import DefaultRouter


from books.views import BookView
from guests.views import GuestView
from slots.views import SlotView
from tables.views import TableView
from restaurants.views import RestaurantView
from folder.views import FolderView
from templates.views import TemplateView
from job_apps.views import JobappView
from task.views import TaskView
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from patients.views import PatientView, PrescriptionView

router = DefaultRouter()

router.register(r'books', BookView, basename="book")
router.register(r'guests', GuestView, basename="guest")
router.register(r'slots', SlotView, basename="slot")
router.register(r'tables', TableView, basename="table")
router.register(r'restaurants', RestaurantView, basename="restaurant")
router.register(r'folders', FolderView, basename="folder")
router.register(r'tasks', TaskView, basename='task')
router.register(r'jobapps', JobappView, basename='jobapp')
router.register(r'templates', TemplateView, basename="template")
router.register(r'patients', PatientView, basename="patient")
router.register(r'prescriptions', PrescriptionView, basename="prescriptions")


urlpatterns = [
    url('', include("home.urls")),
    url('admin/', admin.site.urls),
]

urlpatterns += router.urls
