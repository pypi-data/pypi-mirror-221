# -*- coding: utf-8 -*-
__author__ = "Michael R. Kisel"
__license__ = "MIT"
__version__ = "0.0.0"
__maintainer__ = "Michael R. Kisel"
__email__ = "deploy-me@yandex.ru"
__status__ = "Stable"


__all__ = (
    "SparkRestApi",
    "TemplateRenderError",
    "TemplateSearchError",
)

from spark_rest_api.api import SparkRestApi
from spark_rest_api.exceptions import (
    TemplateRenderError,
    TemplateSearchError
)
