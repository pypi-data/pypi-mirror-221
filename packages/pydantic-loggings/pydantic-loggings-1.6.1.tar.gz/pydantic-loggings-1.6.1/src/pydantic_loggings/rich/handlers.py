import logging
import typing as t

from pydantic import Field

from .. import not_set
from .. import utils
from .formatters import Formatter


class Handler(not_set.Handler):
    NAME: t.ClassVar[str] = 'rich'
    class_: str = Field(default='rich.logging.RichHandler', alias='()')
    level: t.Optional[str] = utils.get_level_name(logging.DEBUG)
    formatter: t.Optional[str] = Formatter.NAME
    #
    omit_repeated_times: t.Optional[bool] = False
    log_time_format: t.Optional[str] = '%m-%d %H:%M:%S'
    show_path: t.Optional[bool] = False
    keywords: t.Optional[list[str]] = []
