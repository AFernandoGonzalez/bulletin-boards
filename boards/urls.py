
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boardapp.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'boardapp.views.custom_page_not_found_view'
handler500 = 'boardapp.views.custom_error_view'
handler403 = 'boardapp.views.custom_permission_denied_view'
handler400 = 'boardapp.views.custom_bad_request_view'