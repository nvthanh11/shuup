# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.dispatch import Signal

# This should yield a list of ProductValidation's objetcs
get_product_validation_issues = Signal(providing_args=["shop_product", "shop", "user", "supplier"], use_caching=True)
