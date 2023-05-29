import os
import requests
from requests import Response
from requests.exceptions import RequestException
from typing import Tuple, Union

from apis.exceptions import CredentialsNotFoundError


MIA_API_BASE_URL = "https://modernism-in-architecture.org/"
MIA_API_VERSION_PATH = "api/v1/twitter/"
MIA_API_PATH_BUILDING_DETAILS = "get_building_details/"
MIA_API_PATH_PUBLISHED = "/published_on_twitter/"


try:
    MIA_API_TOKEN = os.environ["MIA_API_TOKEN"]
except KeyError as e:
    raise CredentialsNotFoundError(e)


class MiaAPI:
    @staticmethod
    def get_mia_building_details() -> Tuple[Union[RequestException, Response], bool]:
        building_details_url = (
            f"{MIA_API_BASE_URL}{MIA_API_VERSION_PATH}{MIA_API_PATH_BUILDING_DETAILS}"
        )
        try:
            response = requests.get(
                building_details_url,
                headers={"Authorization": f"Token {MIA_API_TOKEN}"},
            )
        except requests.exceptions.RequestException as err:
            return err, False

        return response, True

    @staticmethod
    def set_building_published_on_twitter(
        building_id: int,
    ) -> Tuple[Union[RequestException, Response], bool]:
        published_on_twitter_url = f"{MIA_API_BASE_URL}{MIA_API_VERSION_PATH}{building_id}{MIA_API_PATH_PUBLISHED}"

        try:
            response = requests.patch(
                published_on_twitter_url,
                headers={"Authorization": f"Token {MIA_API_TOKEN}"},
            )
        except RequestException as err:
            return err, False

        return response, True
