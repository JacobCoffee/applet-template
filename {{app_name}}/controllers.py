"""Controllers for {{app_name}} routes."""

from dotenv import load_dotenv
from litestar import Controller, get
from structlog import get_logger

from .{{app_name}} import urls

__all__ = ("{{app_name}}Controller",)

logger = get_logger()
load_dotenv()


class CoreController(Controller):
    """{{app_name}} Controller."""

    @get([urls.HEALTH]
        operation_id="{{app_name}}Health",
        name="{{app_name}}:health",
        status_code=HTTP_200_OK,
    )
    async def {{app_name}}_health(self) -> bool:
        """Is {{app_name}} alive?"""
        return True
