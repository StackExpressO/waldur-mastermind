from __future__ import unicode_literals

from nodeconductor_assembly_waldur.billing import views


def register_in(router):
    router.register(r'billing-price-estimates', views.PriceEstimateViewSet, base_name='billing-price-estimate')
