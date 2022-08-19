import requests

import logging
import os

logger = logging.getLogger(__name__)

MIA_API_BASE_URL = "https://modernism-in-architecture.org/"
MIA_API_VERSION_PATH = "api/v1/twitter/"
MIA_API_PATH_BUILDING_DETAILS = "get_building_details/"
MIA_API_PATH_PUBLISHED = "/published_on_twitter/"


try:
    MIA_API_TOKEN = os.environ["MIA_API_TOKEN"]
except KeyError:
    logger.info("MIA_API_TOKEN not available!")
    raise


class MiaAPI:
    def get_mia_building_details() -> requests.Response:
        
        building_details_url = (
            f"{MIA_API_BASE_URL}{MIA_API_VERSION_PATH}{MIA_API_PATH_BUILDING_DETAILS}"
        )

        response = requests.get(
            building_details_url, headers={"Authorization": f"Token {MIA_API_TOKEN}"}
        )

        return response

    def set_building_published_on_twitter(building_id: int) -> requests.Response:

        published_on_twitter_url = f"{MIA_API_BASE_URL}{MIA_API_VERSION_PATH}{building_id}{MIA_API_PATH_PUBLISHED}"

        response = requests.patch(
            published_on_twitter_url,
            headers={"Authorization": f"Token {MIA_API_TOKEN}"},
        )

        return response
