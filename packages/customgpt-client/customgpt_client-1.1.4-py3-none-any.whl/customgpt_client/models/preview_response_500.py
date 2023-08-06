from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preview_response_500_status import PreviewResponse500Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_response_500_data import PreviewResponse500Data


T = TypeVar("T", bound="PreviewResponse500")


@attr.s(auto_attribs=True)
class PreviewResponse500:
    """
    Attributes:
        status (Union[Unset, PreviewResponse500Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, PreviewResponse500Data]):
    """

    status: Union[Unset, PreviewResponse500Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "PreviewResponse500Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        url = self.url
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.preview_response_500_data import PreviewResponse500Data

        _status = src_dict.get("status")
        status: Union[Unset, PreviewResponse500Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PreviewResponse500Status(_status)

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, PreviewResponse500Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PreviewResponse500Data.from_dict(_data)

        preview_response_500 = cls(
            status=status,
            url=url,
            data=data,
        )

        preview_response_500.additional_properties = src_dict
        return preview_response_500

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
