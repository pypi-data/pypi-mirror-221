from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdInfoEndpoint import CompanyEntitytypesIdInfoEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import EntityType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyEntitytypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyEntitytypesIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EntityType]:
        """
        Performs a GET request against the /company/entityTypes/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EntityType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            EntityType,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EntityType:
        """
        Performs a GET request against the /company/entityTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EntityType: The parsed response data.
        """
        return self._parse_one(EntityType, super()._make_request("GET", data=data, params=params).json())
