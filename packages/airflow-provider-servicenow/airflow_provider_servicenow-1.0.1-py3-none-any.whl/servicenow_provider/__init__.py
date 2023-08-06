__version__ = "1.0.1"

## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features.
def get_provider_info():
    return {
        "package-name": "airflow-provider-servicenow",  # Required
        "name": "ServiceNow",  # Required
        "description": "A Service Now for Apache Airflow providers.",  # Required
        "connection-types": [
            {
                "connection-type": "ServiceNow",
                "hook-class-name": "servicenow_provider.hooks.servicenow.ServiceNowHook"
            }
        ],
        "task-decorators": [
            {
                "name": "servicenowrecord",
                "class-name": "servicenow_provider.operators.servicenow.servicenowrecord",
            },
            {
                "name": "servicenowinsert",
                "class-name": "servicenow_provider.operators.servicenowinsert.servicenowinsert",
            },
            {
                "name": "servicenowupdate",
                "class-name": "servicenow_provider.operators.servicenowupdate.servicenowupdate",
            },
            {
                "name": "servicenowsearch",
                "class-name": "servicenow_provider.operators.servicenowsearch.servicenowsearch",
            },
        ],
        "extra-links": ["servicenow_provider.operators.servicenow.ServiceNowOperatorExtraLink"],
        "versions": [__version__],  # Required
    }
