from apis.twitter_api import TwitterAPI
from apis.mia_api import MiaAPI
import logging
import logging.handlers


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


def main() -> bool:

    mia_response, was_successful = MiaAPI.get_mia_building_details()

    if not was_successful:
        logger.error(
            f"Retrieving building details failed. API error occured. ERROR: {mia_response}"
        )
        return False

    if mia_response.status_code != 200:
        logger.error(
            f"Retrieving building details was not successful. STATUS: {mia_response.status_code}",
        )
        return False

    building_details = mia_response.json().get("data")

    building_id = building_details.get("id")
    title = building_details.get("name")
    year = building_details.get("yearOfConstruction")
    city = building_details.get("city")
    country = building_details.get("country")
    architect = building_details.get("architect")
    url = building_details.get("absoluteURL")

    tweet_content = f"""New on MIA: {title} by {architect} ({year}) in {city}, {country}\n#modernism #architecture #bauhaus #neuesbauen #internationalstyle #interwararchitecture #{"".join(city.split(" "))} #{country}\n{url}"""

    if not architect:
        tweet_content = f"""New on MIA: {title} ({year}) in {city}, {country}\n#modernism #architecture #bauhaus #neuesbauen #internationalstyle #interwararchitecture #{"".join(city.split(" "))} #{country}\n{url}"""
    
    twitter_response, was_successful = TwitterAPI.tweet_mia_building(tweet_content)

    if not was_successful:
        logger.error(f"Post tweet failed. API error occured. ERROR: {twitter_response}")
        return False

    mia_response, was_successful = MiaAPI.set_building_published_on_twitter(building_id)

    if not was_successful:
        logger.error(
            f"Set building published failed. API error occured. ERROR: {mia_response}"
        )
        return False

    logger.info(f"Successfully published {title} on twitter.")

    return True


if __name__ == "__main__":
    main()
