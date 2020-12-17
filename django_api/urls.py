from rest_framework import routers
from books.views import BookView
from guests.views import GuestView
from slots.views import SlotView
from tables.views import TableView
from restaurants.views import RestaurantView
from folder.views import FolderView
from task.views import TaskView
from django.contrib import admin
from django.conf.urls import url

router = routers.SimpleRouter()

router.register(r'books', BookView)
router.register(r'guests', GuestView)
router.register(r'slots', SlotView)
router.register(r'tables', TableView)
router.register(r'restaurants', RestaurantView)
router.register('folders', FolderView)
router.register('tasks', TaskView)


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', )
]

urlpatterns += router.urls
