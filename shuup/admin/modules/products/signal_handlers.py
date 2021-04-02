# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.dispatch import receiver

from shuup.admin.modules.products.signals import get_product_validation_issues
from shuup.admin.modules.products.issues import ProductValidationIssue
from shuup.core.models import Category


def update_categories_post_save(sender, instance, **kwargs):
    if not getattr(settings, "SHUUP_AUTO_SHOP_PRODUCT_CATEGORIES", False):
        return

    if not instance.pk or not instance.primary_category:
        return

    categories = instance.categories.values_list("pk", flat=True)
    if instance.primary_category.pk not in categories:
        instance.categories.add(instance.primary_category)


def update_categories_through(sender, instance, **kwargs):
    action = kwargs.get("action", "post_add")
    if action != "post_add":
        return

    if not getattr(settings, "SHUUP_AUTO_SHOP_PRODUCT_CATEGORIES", False):
        return

    if not instance.pk:
        return
    if isinstance(instance, Category):
        shop_products = instance.shop_products.all()
        for shop_product in shop_products:
            set_shop_product_category(shop_product)
    else:
        set_shop_product_category(instance)


def set_shop_product_category(instance):
    if not instance.categories.count():
        return

    if not instance.primary_category:
        instance.primary_category = instance.categories.first()
        instance.save()


@receiver(get_product_validation_issues)
def product_signal(sender, shop_product, shop, user, supplier=None, **kwargs):
    '''
    Yield a list of the ProductValidationIssue's objects
    '''
    # some conditions here
    product = shop_product.product
    if not all([product.height, product.width, product.depth, product.gross_weight]):
        yield ProductValidationIssue(
            code="ahihi",
            message="Product size and/or weight attributes not configured properly",
            issue_type="warning",
            is_html=False
        )
