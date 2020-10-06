from django.utils.translation import ugettext_lazy as _

from app.admin import ModelAdmin, admin
from magnets.models import EmailLeadMagnetCampaign


@admin.register(EmailLeadMagnetCampaign)
class EmailLeadMagnetCampaignAdmin(ModelAdmin):
    fields = [
        'name',
        'slug',
        'template_id',
        'success_message',
    ]

    list_display = [
        'name',
        'slug',
        'lead_count',
    ]

    prepopulated_fields = {
        'slug': ['name'],
    }

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .with_lead_count()

    def lead_count(self, obj=None):
        return obj.lead_count if obj and hasattr(obj, 'lead_count') and obj.lead_count else '—'

    lead_count.short_description = _('Lead count')
    lead_count.admin_order_field = 'lead_count'
