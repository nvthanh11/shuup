# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

class ProductValidationIssue:
    '''
    issue_type: info, warning, error
    '''
    def __init__(self, code: str, message: str, issue_type: str, is_html: bool = False):
        self.code = code
        self.message = message
        self.issue_type = issue_type
        self.is_html = is_html
