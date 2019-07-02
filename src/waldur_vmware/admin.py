from __future__ import unicode_literals

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from waldur_core.core.admin import ExecutorAdminAction
from waldur_core.structure import admin as structure_admin

from . import executors, models


class DiskAdmin(structure_admin.ResourceAdmin):

    class Pull(ExecutorAdminAction):
        executor = executors.DiskPullExecutor
        short_description = _('Pull')

        def validate(self, instance):
            if instance.state not in (models.Disk.States.OK, models.Disk.States.ERRED):
                raise ValidationError(_('Disk has to be in OK or ERRED state.'))

    pull = Pull()


admin.site.register(models.VMwareService, structure_admin.ServiceAdmin)
admin.site.register(models.VMwareServiceProjectLink, structure_admin.ServiceProjectLinkAdmin)
admin.site.register(models.Disk, DiskAdmin)
