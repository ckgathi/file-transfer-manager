from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'file_transfer_manager'
    base_template_name = 'edc_base/base.html'
    project_name = 'File Transfer Manager'
    institution = 'CDC Botswana'

    protocol_sites = {
        'Kweneng District clinics': 'community_clinic', }
