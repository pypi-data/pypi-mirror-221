# -*- coding: utf-8 -*-
from spark_rest_api.data_classes import Response
from spark_rest_api.templates import TemplatesRepository


__all__ = ("SparkRestApi", )


class SparkRestApi:
    """API interface for Spark REST API
    """

    def __init__(self, spark_host, spark_api="/api/v1"):
        """Init params

        Parameters
        ----------
        spark_host : str
            Spark host
        spark_api : str, optional
            Spark api path, by default "/api/v1"
        """
        self.__templates_repository = TemplatesRepository()
        self.default_kwargs = {
            "spark_host": spark_host, "spark_api": spark_api}

    def __repr__(self):
        """Return SparkRestApi representation

        Returns
        -------
        str
            SparkRestApi representation
        """
        return f"{self}(templates={self.templates})"

    def __str__(self):
        """Str method

        Returns
        -------
        str
            String representation
        """
        return self.__class__.__name__

    @property
    def templates(self):
        """Return set of templates identifieres

        Returns
        -------
        set
            Templates identifieres
        """
        return self.__templates_repository.ids

    def render_url(self, template_id, **template_vars):
        """Render url

        Parameters
        ----------
        template_id : int
            Template's identifier

        Returns
        -------
        str
            Rendered url
        """
        return self.__templates_repository.render_template(
            template_id, **{**self.default_kwargs, **template_vars}
            )

    def find_template(self, search_pattern):
        """Find templates by pattern

        Parameters
        ----------
        search_pattern : str
            Regex or usual string

        Returns
        -------
        generator
            Templates generator
        """
        return self.__templates_repository.find_template_id(search_pattern)

    def get_template(self, template_id):
        """Get template by template identifier

        Parameters
        ----------
        template_id : int
            Template's identifier

        Returns
        -------
        Template
            Template dataclass
        """
        return self.__templates_repository.get_template(template_id)

    def show_templates(self):
        """Print markdown table with templates
        """
        print(self.__templates_repository.df_md)

    async def execute(self, session, url, method="GET", **kwargs):
        """Call requested uri

        Parameters
        ----------
        session : aiohttp.ClientSession
            Client session
        url : str
            Api url
        method : str, optional
            HTTP method, by default "GET"

        Returns
        -------
        spark_rest_api.data_classes.Response
            Dataclass instance
        """
        async with session.request(method, url, **kwargs) as resp:
            status, content_type = resp.status, resp.headers["Content-Type"]
            if content_type == "application/json":
                raw = await resp.json()
            elif content_type == "text/plain":
                raw = await resp.text()
            elif content_type == "application/octet-stream":
                raw = await resp.content.read()
            else:
                raw = None
            return Response(status=status, raw=raw)
