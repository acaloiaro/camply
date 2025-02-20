"""
API Searching Configuration
"""

from os import getenv
from typing import Union

from dotenv import load_dotenv

from camply.config.file_config import FileConfig

load_dotenv(FileConfig.DOT_CAMPLY_FILE, override=False)

STANDARD_HEADERS: dict = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


class RIDBConfig:
    """
    RIDB API Configuration

    https://ridb.recreation.gov/docs
    """

    _camply_ridb_service_account_api_token: bytes = (
        b"YTc0MTY0NzEtMWI1ZC00YTY0LWFkM2QtYTIzM2U3Y2I1YzQ0"
    )
    _api_key: Union[str, bytes] = getenv(
        "RIDB_API_KEY", _camply_ridb_service_account_api_token
    )
    API_KEY = _camply_ridb_service_account_api_token if _api_key == "" else _api_key

    RIDB_SCHEME: str = "https"
    RIDB_NET_LOC: str = "ridb.recreation.gov"
    RIDB_BASE_PATH: str = "api/v1/"

    # FACILITIES_API_PATH FIELDS
    FACILITIES_API_PATH: str = "facilities"
    CAMPGROUND_FACILITY_FIELD_QUALIFIER: str = "Campground"
    TICKET_FACILITY_FIELD_QUALIFIER: str = "Ticket Facility"
    TIMED_ENTRY_FACILITY_FIELD_QUALIFIER: str = "Timed Entry"
    # RECREATION AREA FIELDS
    REC_AREA_API_PATH: str = "recareas"
    # CAMPSITE DETAILS
    CAMPSITE_API_PATH: str = "campsites"
    # TOUR DETAILS
    TOUR_API_PATH: str = "tours"


class RecreationBookingConfig:
    """
    Variable Storage Class for Recreation.gov Booking API
    """

    API_SCHEME: str = "https"
    API_NET_LOC = "www.recreation.gov"
    API_BASE_PATH: str = "api/camps/availability/campground/"
    API_MONTH_PATH: str = "month"
    API_REFERRERS: dict = {"Referer": "https://www.recreation.gov/"}

    CAMPSITE_UNAVAILABLE_STRINGS: list = [
        "Reserved",
        "Not Available",
        "Not Reservable",
        "Not Reservable Management",
        "Not Available Cutoff",
        "Lottery",
        "Open",
        "NYR",
    ]

    CAMPSITE_LOCATION_LOOP_DEFAULT: str = "Default Loop"
    CAMPSITE_LOCATION_SITE_DEFAULT: str = "Default Site"

    CAMPSITE_BOOKING_URL: str = "https://www.recreation.gov/camping/campsites"

    RATE_LIMITING = (1.01, 1.51)
