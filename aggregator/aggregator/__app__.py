"""
Aggregator Application
"""

from os.path import dirname
from pathlib import Path

from harp import get_logger
from harp.config import Application, OnBindEvent, OnBoundEvent

from .settings import AgregatorSettings

logger = get_logger(__name__)


async def on_bind(event: OnBindEvent):
    # Load service definitions, bound to our settings.
    event.container.load(
        Path(dirname(__file__)) / "services.yml",
        bind_settings=event.settings["aggregator"],
    )


async def on_bound(event: OnBoundEvent):

    event.resolver.add_controller(
        event.provider.get(AgregatorSettings).port,
        event.provider.get("aggregator.controller"),
    )


application = Application(
    settings_type=AgregatorSettings,
    on_bind=on_bind,
    on_bound=on_bound,
    dependencies=["proxy"],
)
