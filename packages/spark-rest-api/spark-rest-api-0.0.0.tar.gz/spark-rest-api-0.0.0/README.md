<p align="center">
    <a href="https://bit.ly/spark-ra"><img src="https://bit.ly/sra-logo" alt="SRA"></a>
</p>
<p align="center">
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/v/spark-rest-api.svg?style=flat-square&logo=appveyor" alt="Version"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/l/spark-rest-api.svg?style=flat-square&logo=appveyor&color=blueviolet" alt="License"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/pyversions/spark-rest-api.svg?style=flat-square&logo=appveyor" alt="Python"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/status/spark-rest-api.svg?style=flat-square&logo=appveyor" alt="Status"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/format/spark-rest-api.svg?style=flat-square&logo=appveyor&color=yellow" alt="Format"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/pypi/wheel/spark-rest-api.svg?style=flat-square&logo=appveyor&color=red" alt="Wheel"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://img.shields.io/bitbucket/pipelines/deploy-me/spark-rest-api/master?style=flat-square&logo=appveyor" alt="Build"></a>
    <a href="https://pypi.org/project/spark-rest-api"><img src="https://bit.ly/sra-cov" alt="Coverage"></a>
    <a href="https://pepy.tech/project/spark-rest-api"><img src="https://static.pepy.tech/personalized-badge/spark-rest-api?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="Downloads"></a>
    <br><br><br>
</p>

# SPARK-REST-API

Async wrapper for [Spark REST API](https://bit.ly/sra-docs). See more in [documentation](https://deploy-me.bitbucket.io/spark-rest-api/index.html)

## INSTALL

```bash
pip install spark-rest-api
```

## USAGE

```python
import asyncio
import io
import zipfile
import aiohttp
import pandas as pd
from spark_rest_api import SparkRestApi


sra = SparkRestApi(spark_host="https://<host>:<port>")
sra.show_templates()


async def main(sra):
    base_app_id = "application_XXXXXXXXXXXXX_XXXXXX"
    async with aiohttp.ClientSession() as session:
        resp = (
            await sra.execute(
                session=session,
                url=sra.render_url(template_id=0)
            )
        )
        assert resp.status == 200
        df = resp.to_df()
        attempts = df[df["id"] == base_app_id].attempts.tolist()
        if attempts:
            urls = map(
                lambda x: sra.render_url(3, app_id=f"{base_app_id}/{x['attemptId']}"),
                attempts[0]
                )
            df_result = pd.concat(
                map(
                    lambda x: x.to_df(),
                    (
                        await asyncio.gather(*(sra.execute(session, url) for url in urls))
                        )
                    )
                )
            print(df_result)


        log_data = await sra.execute(session, sra.render_url(template_id=13, base_app_id=base_app_id))
        with zipfile.ZipFile(io.BytesIO(log_data.raw), "r") as zip_file:
            for f in zip_file.infolist():
                print(zip_file.read(f).decode())


loop = asyncio.get_event_loop()
loop.run_until_complete(main(sra))
```
