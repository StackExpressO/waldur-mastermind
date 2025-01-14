from waldur_rancher import views as rancher_views
from waldur_mastermind.marketplace import processors


class RancherCreateProcessor(processors.BaseCreateResourceProcessor):
    viewset = rancher_views.ClusterViewSet
    fields = (
        'name',
        'instance',
    )


class RancherDeleteProcessor(processors.DeleteResourceProcessor):
    viewset = rancher_views.ClusterViewSet
