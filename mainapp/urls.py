from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from mainapp.view import login, home, add_manager, add_customer, \
    add_purchase, call_notes, attachments, task, calendars
from mainapp.view.import_export.export_data import export_xls, import_xls
from mainapp.view.pdfs import offers


app_name = 'mainapp'
urlpatterns = [
    path('', include(('mainapp.urls2', 'mainapp'), namespace='new')),

    path('heartbeat/', login.heartbeat, name='heartbeat'),
    path('', login.LoginView.as_view(), name='login'),
    path('logout', login.logout_view, name='logout'),

    # Home
    path('home/', home.HomeView.as_view(), name='home'),
    path('home/customer/<customer_id>/', home.CustomerHomeView.as_view(), name='customer_home'),

    path('manager/', add_manager.CreateManagerView.as_view(), name='add_manager'),
    path('manager/<int:pk>/', add_manager.UpdateManagerView.as_view(), name='edit_manager'),
    path('delete_manager/<manager_id>', add_manager.delete_manager, name='delete_manager'),

    path('customers/', add_customer.ListCustomerView.as_view(), name='list_customer'),
    path('customer/', add_customer.AddCustomerView.as_view(), name='add_customer'),
    path('customer/<int:pk>/', add_customer.UpdateCustomerView.as_view(), name='edit_customer'),
    path('update_customer/<int:pk>/', add_customer.update_customer, name='patch_customer'),
    path('delete/customer/<int:pk>/', add_customer.DeleteCustomerView.as_view(), name='delete_customer'),

    path('add_purchase/', add_purchase.AddPurchaseView.as_view(), name='add_purchase'),
    path('purchases/', add_purchase.ListPurchaseView.as_view(), name='list_purchase'),
    path('purchases/<int:pk>/', add_purchase.UpdatePurchaseView.as_view(), name='edit_purchase'),
    path('update_purchase/<int:pk>/', add_purchase.update_purchase, name='patch_purchase'),
    path('delete/purchases/<int:pk>/', add_purchase.DeletePurchaseView.as_view(), name='delete_purchase'),

    path('task_list/', task.TasksView.as_view(), name='open_task_list'),
    path('task/<int:pk>/', task.TaskUpdateView.as_view(), name='edit_task'),
    path('delete/task/<int:pk>/', task.DeleteTaskView.as_view(), name='delete_task'),
    path('mark_complete/<int:pk>/', task.mark_completed, name='mark_completed'),
    path('create_calendar_task/', task.create_task, name='create_calendar_task'),

    path('call_notes/<customer_id>/', call_notes.CallNotesCreateView.as_view(), name='add_call_notes'),
    path('call_notes/<customer_id>/<int:pk>/', call_notes.CallNotesUpdateView.as_view(), name='edit_call_notes'),
    path('delete/call_notes/<customer_id>/<int:pk>/', call_notes.CallNotesDeleteView.as_view(), name='delete_call_notes'),

    path('chat/', include(('chat.urls', 'chat'), 'chat')),

    path('<int:customer_id>/attachments/', attachments.AttachmentCreateView.as_view(), name='add_attachments'),
    path('<int:customer_id>/attachments/<int:pk>/', attachments.UpdateAttachmentView.as_view(), name='edit_attachments'),
    path('delete/<int:customer_id>/attachments/<int:pk>/', attachments.DeleteAttachmentView.as_view(), name='delete_attachments'),
    path('email/<int:customer_id>/attachment/<int:pk>/', attachments.email_attachment, name='email_attachment'),

    # attachment type settings
    path('attachment_type/', attachments.UpdateAttachmentTemplateView.as_view(), name='attachment_type'),

    # calendar
    path('calendar/', calendars.calendar, name='calendar'),

    # export and import urls
    path('export_data/', export_xls, name='export_xls'),
    path('import_data/', import_xls, name='import_xls'),

    path('offer/<customer_id>/', offers.download_offer, name='pdf_offer'),
    path('offer_confirm/<customer_id>/', offers.download_offer_confirm, name='pdf_offer_confirm'),
    path('install/<customer_id>/', offers.download_install, name='pdf_install'),
    path('invoice/<customer_id>/', offers.download_invoice, name='pdf_invoice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
