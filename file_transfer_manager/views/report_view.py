from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin

from .site_monitoring_starts_view import SiteMonitoringStartView


class ReportView(SiteMonitoringStartView, EdcBaseViewMixin, TemplateView):

    app_config_name = 'file_transfer_manager'
    template_name = 'file_transfer_manager/report.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            project_name=self.app_config.project_name,
            institution=self.app_config.institution)
        return context
