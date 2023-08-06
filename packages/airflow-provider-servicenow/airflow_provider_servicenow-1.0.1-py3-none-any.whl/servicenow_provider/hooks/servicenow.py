from __future__ import annotations

from typing import Any, Tuple

import requests
import json
from requests.auth import HTTPBasicAuth

from airflow.hooks.base import BaseHook
from pysnc import ServiceNowClient,GlideRecord


class ServiceNowHook(BaseHook):
    """
    servicenow Hook that interacts with an ServiceClient by python pysnc lib.

    :param servicenow_conn_id: connection that has the base API url i.e https://devxxxxx.service-now.com
        and optional authentication credentials. Default headers can also be specified in
        the Extra field in json format.
    :type servicenow_conn_id: str
    """

    conn_name_attr = "servicenow_conn_id"
    default_conn_name = "servicenow_default"
    conn_type = "ServiceNow"
    hook_name = "servicenow"

    @staticmethod
    def get_connection_form_widgets() -> dict[str, Any]:
        """Returns connection widgets to add to connection form"""
        from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
        from flask_babel import lazy_gettext
        from wtforms import PasswordField, StringField

        return {
            "account": StringField(lazy_gettext("Account"), widget=BS3TextFieldWidget()),
            "secret_key": PasswordField(lazy_gettext("Secret Key"), widget=BS3PasswordFieldWidget()),
        }

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Returns custom field behaviour"""
        import json

        return {
            "hidden_fields": ["port", "password", "login", "schema"],
            "relabeling": {},
            "placeholders": {
                "extra": json.dumps(
                    {
                        "proxy": "http://proxy:8080",
                        "verify": "false",
                    },
                    indent=4,
                ),
                "account": "API Token",
                "secret_key": "API Secret",
                "host": "https://devxxx.service-now.com",
            },
        }

    def __init__(
        self,
        servicenow_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.servicenow_conn_id = servicenow_conn_id

    def get_conn(self) -> ServiceNowClient:
        """
        Returns ServceNow client to use with requests.

        :param headers: additional headers to be passed through as a dictionary
        :type headers: dict
        """

        if self.servicenow_conn_id:
            conn = self.get_connection(self.servicenow_conn_id)
            extra_params = conn.extra_dejson
            if conn.host and "://" in conn.host:
                self.servier_now_PDI = conn.host
            if extra_params["account"] and extra_params["secret_key"]:
                self.username = extra_params["account"]
                self.password = extra_params["secret_key"]
            else:
                self.log.error("No account or secret key supplied.")
            if conn.extra:
                try:
                    self.extra_params = json.loads(conn.extra)
                except TypeError:
                    self.log.warning("Connection to %s has invalid extra field.", conn.host)
            client = ServiceNowClient(
                self.servier_now_PDI,
                (self.username, self.password),
                proxy=self.extra_params.get("proxy"),
                verify=self.extra_params.get("verify"),
                )
        return client

    def Get(
        self,
        table:str,
        sys_id: str,
        batch_size: int = 100,
        display_value: bool = False,
        feilds: list[str] = None,
        **kwargs,
    ) -> GlideRecord:
        """
        Performs the request

        :param table: the table to be called, i.e. alm_asset
        :type table: str
        :param sys_id: service now table primary key
        :type sys_id: str
        :param batch_size: the number of records to be returned in a single request
        :type batach_size: int
        :return: GlideRecord object
        """

        session = self.get_conn().GlideRecord(table, batch_size)
        if sys_id:
            session.get("sys_id", sys_id)
        else:
            raise ValueError("sys_id is required")
        return session.serialize(display_value, feilds)
    
    def SearchRecord(
        self,
        table:str,
        query: list,
        or_condition: list = None,
        join_querys: list[dict] = None,
        batch_size: int = 100,
        display_value: bool = False,
        feilds: list[str] = None,
    )-> GlideRecord:
        session = self.get_conn().GlideRecord(table, batch_size)
        # if join_querys:
        #     for join_query in join_querys:
        #         session.add_join_query(join_table=join_query['table'],join_table_field=join_query['join_table_field'])
        
        for q in range(len(query)):
            if len(query[q])==2:
                o = session.add_query(query[q][0], query[q][1])
            elif len(query[q])==3:
                o = session.add_query(query[q][0], query[q][1], query[q][2])
            else:
                raise ValueError("query is required")
        session.query()
        return session.serialize_all(display_value, feilds)
    
    def Insert(
        self,
        table:str,
        data: dict,
        batch_size: int = 100,
    )-> str:
        session = self.get_conn().GlideRecord(table, batch_size)
        session.initialize()
        for k,v in data.items():
            session.set_value(k,v)
        insert_id = session.insert()
        return insert_id
    
    def Update(
        self,
        table:str,
        sys_id: str,
        data: dict,
        batch_size=100,
    )-> str:
        session = self.get_conn().GlideRecord(table, batch_size)
        if session.get("sys_id", sys_id):
            for k,v in data.items():
                session.set_value(k,v)
            update_sys_id = session.update()
            return update_sys_id
        return None
    def test_connection(self) -> Tuple[bool, str]:
        """Test a connection"""
        try:
            gr = self.Get(table="xxx", sys_id="x")
        except Exception as e:
            if str(e).find("Invalid table xxx") != -1:
                return True, "Connection successfully tested"
            return False, str(e)
