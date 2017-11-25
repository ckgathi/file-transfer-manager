from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'File Transfer Monitor'
    site_header = 'File Transfer Monitor'
    index_title = 'File Transfer Monitor'
    site_url = '/file_transfer_monitor/list/'


file_transfer_monitor_admin = AdminSite(name='file_transfer_monitor_admin')
