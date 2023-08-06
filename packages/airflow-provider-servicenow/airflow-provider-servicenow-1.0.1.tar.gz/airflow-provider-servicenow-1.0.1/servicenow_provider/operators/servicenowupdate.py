from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable
from airflow.decorators.base import task_decorator_factory,DecoratedOperator
from airflow.exceptions import AirflowException
from airflow.models import BaseOperator, BaseOperatorLink
from airflow.operators.python import PythonVirtualenvOperator

from servicenow_provider.hooks.servicenow import ServiceNowHook

if TYPE_CHECKING:
    from airflow.utils.context import Context


class ServiceNowOperatorExtraLink(BaseOperatorLink):

    name = "ServiceNow Registry"

    def get_link(self, operator: BaseOperator, *, ti_key=None):
        return "https://www.servicenow.com"


class ServiceNowUpdateOperator(PythonVirtualenvOperator):
    """
    Calls a ServiceNow API endpoint, gets a record by sys_id and returns the response

    :param conn_id: connection to run the operator with ServiceNow
    :type conn_id: str
    :param table: The ServiceNow table to query
    :type table: str
    :param sys_id: The sys_id of the record to get
    :type sys_id: str
    :param batch_size: The number of records to fetch at a time. Defaults to 100
    :type batch_size: int
    """

    # Specify the arguments that are allowed to parse with jinja templating
    template_fields = []
    template_fields_renderers = {}
    template_ext = ()
    ui_color = "#f4a460"

    operator_extra_links = (ServiceNowOperatorExtraLink(),)

    def __init__(
        self,
        *,
        conn_id: str = "servicenow_default",
        table: str,
        display_value: bool = False,
        feilds: list[str] = None,
        op_args: Collection[Any] | None = None,
        op_kwargs: Mapping[str, Any] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.table = table
        self.display_value = display_value
        self.feilds = feilds
        if kwargs.get("xcom_push") is not None:
            raise AirflowException("'xcom_push' was deprecated, use 'BaseOperator.do_xcom_push' instead")

    def execute(self, context):
        hook = ServiceNowHook(servicenow_conn_id=self.conn_id)
        result = super().execute_callable()
        update_result = list()
        for k,v in result.items():
            try:
                update_sys_id = hook.Update(
                    table=self.table,
                    data=v,
                    sys_id=k,
                )
                if update_sys_id:
                    update_result.append(str(update_sys_id))
            except Exception as e:
                self.log.error(e)
        print(update_result)
        return update_result

class _ServiceNowUpdateDecoratedOperator(DecoratedOperator, ServiceNowUpdateOperator):
    """
    Wraps a Python callable and captures args/kwargs when called for execution.

    :param python_callable: A reference to an object that is callable
    :param op_kwargs: a dictionary of keyword arguments that will get unpacked
        in your function (templated)
    :param op_args: a list of positional arguments that will get unpacked when
        calling your callable (templated)
    :param multiple_outputs: If set to True, the decorated function's return value will be unrolled to
        multiple XCom values. Dict will unroll to XCom values with its keys as XCom keys. Defaults to False.
    """

    custom_operator_name: str = "@task.servicenowupdate"

    def __init__(self, *, python_callable, op_args, op_kwargs, **kwargs) -> None:
        kwargs_to_upstream = {
            "python_callable": python_callable,
            "op_args": op_args,
            "op_kwargs": op_kwargs,
        }
        super().__init__(
            kwargs_to_upstream=kwargs_to_upstream,
            python_callable=python_callable,
            op_args=op_args,
            op_kwargs=op_kwargs,
            **kwargs,
        )

if TYPE_CHECKING:
    from airflow.decorators.base import TaskDecorator

def servicenowupdate(
    python_callable: Callable | None = None,
    multiple_outputs: bool | None = None,
    **kwargs,
) -> "TaskDecorator":
    return task_decorator_factory(
        python_callable=python_callable,
        multiple_outputs=multiple_outputs,
        decorated_operator_class=_ServiceNowUpdateDecoratedOperator,
        **kwargs,
    )
