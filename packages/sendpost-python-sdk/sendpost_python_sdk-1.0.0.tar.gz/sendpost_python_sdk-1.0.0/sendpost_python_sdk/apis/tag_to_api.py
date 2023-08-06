import typing_extensions

from sendpost_python_sdk.apis.tags import TagValues
from sendpost_python_sdk.apis.tags.email_api import EmailApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMAIL: EmailApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMAIL: EmailApi,
    }
)
