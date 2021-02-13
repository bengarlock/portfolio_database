from rest_framework import routers
from books.views import BookView
from guests.views import GuestView
from slots.views import SlotView
from tables.views import TableView
from restaurants.views import RestaurantView
from folder.views import FolderView
from templates.views import TemplateView
# from okta_interview.views import OktaInterviewView
from job_apps.views import JobappView
from task.views import TaskView
from django.contrib import admin
from django.conf.urls import url
from django.urls import include

router = routers.SimpleRouter()

router.register(r'books', BookView)
router.register(r'guests', GuestView)
router.register(r'slots', SlotView)
router.register(r'tables', TableView)
router.register(r'restaurants', RestaurantView)
router.register('folders', FolderView)
router.register('tasks', TaskView)
router.register('jobapps', JobappView)
router.register('templates', TemplateView)
# router.register("oktausers", OktaInterviewView)



urlpatterns = [
    url('', include("home.urls")),
    url('admin/', admin.site.urls),
]

urlpatterns += router.urls
