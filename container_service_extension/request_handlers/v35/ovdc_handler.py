# container-service-extension
# Copyright (c) 2019 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause
import container_service_extension.def_.models as def_models
import container_service_extension.def_.ovdc_service as ovdc_service
import container_service_extension.operation_context as ctx
import container_service_extension.request_handlers.request_utils as request_utils  # noqa: E501
from container_service_extension.shared_constants import RequestKey
from container_service_extension.telemetry.constants import CseOperation
from container_service_extension.telemetry.telemetry_handler import record_user_action_telemetry  # noqa: E501


@request_utils.v35_api_exception_handler
def ovdc_update(data, operation_context: ctx.OperationContext):
    """Request handler for ovdc enable, disable operations.

    Add or remove the respective cluster placement policies to enable or
    disable cluster deployment of a certain kind in the OVDC.

    Required data: k8s_runtime

    :return: Dictionary with org VDC update task href.
    """
    ovdc_spec = def_models.Ovdc(**data[RequestKey.V35_SPEC])
    return ovdc_service.update_ovdc(operation_context,
                                    ovdc_id=data[RequestKey.OVDC_ID],
                                    ovdc_spec=ovdc_spec)


@record_user_action_telemetry(cse_operation=CseOperation.OVDC_INFO)
@request_utils.v35_api_exception_handler
def ovdc_info(data, operation_context: ctx.OperationContext):
    """Request handler for ovdc info operation.

    Required data: ovdc_id

    :return: Dictionary with org VDC k8s provider metadata.
    """
    ovdc_id = data[RequestKey.OVDC_ID]
    return ovdc_service.get_ovdc(operation_context, ovdc_id)


@record_user_action_telemetry(cse_operation=CseOperation.OVDC_LIST)
@request_utils.v35_api_exception_handler
def ovdc_list(data, operation_context: ctx.OperationContext):
    """Request handler for ovdc list operation.

    :return: List of dictionaries with org VDC k8s runtimes.
    """
    return ovdc_service.list_ovdc(operation_context)
