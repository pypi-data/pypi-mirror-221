import typing_extensions

from sendpost_py_sdk.paths import PathValues
from sendpost_py_sdk.apis.paths.subaccount_email_ import SubaccountEmail
from sendpost_py_sdk.apis.paths.subaccount_email_template import SubaccountEmailTemplate

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SUBACCOUNT_EMAIL_: SubaccountEmail,
        PathValues.SUBACCOUNT_EMAIL_TEMPLATE: SubaccountEmailTemplate,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SUBACCOUNT_EMAIL_: SubaccountEmail,
        PathValues.SUBACCOUNT_EMAIL_TEMPLATE: SubaccountEmailTemplate,
    }
)
