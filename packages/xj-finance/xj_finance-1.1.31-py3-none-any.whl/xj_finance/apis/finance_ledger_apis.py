# _*_coding:utf-8_*_

import os, logging, time, json, copy

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from ..services.finance_ledger import FinanceLedgerService
from ..utils.custom_tool import request_params_wrapper, flow_service_wrapper, format_params_handle
from xj_finance.utils.user_wrapper import user_authentication_wrapper
from ..utils.model_handle import util_response

logger = logging.getLogger(__name__)


class FinanceLedgerApi(APIView):  # 或继承(APIView)

    # 财务添加
    @api_view(['GET'])
    @user_authentication_wrapper
    @request_params_wrapper
    def ledger(self, *args, user_info, request_params, **kwargs, ):
        params = request_params
        user_id = user_info.get("user_id")
        platform_id = user_info.get("platform_id")
        params.setdefault("account_id", user_id)  # 用户ID
        transact_set, err = FinanceLedgerService.ledger()
        if err is None:
            return util_response(data=transact_set)
        return util_response(err=47767, msg=err)
