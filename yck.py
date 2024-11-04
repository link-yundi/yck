# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2024/11/4 上午9:01
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""

from clickhouse_driver import Client
import polars as pl
from random import randint
import pandas as pd

def connect(urls: list[str], user: str, password: str) -> Client:
    i = randint(0, len(urls) - 1)
    url_ini = urls[i]
    [host, port] = url_ini.split(":")
    return Client(host, port=port, round_robin=True, alt_hosts=",".join(urls), user=user, password=password)

def query_pandas(sql, conn) -> pd.DataFrame:
    return conn.query_dataframe(sql)

def query_polars(sql, conn) -> pl.DataFrame:
    data, columns = conn.execute(sql, columnar=True, with_column_types=True)
    columns = [name for name, type_ in columns]
    return pl.DataFrame(
        {col: d for d, col in zip(data, columns)},
    )
