# yck
请求 clickhouse集群，结果返回pandas.DataFrame/polars.DataFrame

### 安装
```shell
pip install git+https://github.com/link-yundi/yck.git
```

### 示例

```python
import yck

# 集群配置
config = dict(
    urls=["<host1>:<port>", "<host2>:<port>", ....],
    user="<user_name>", 
    password="xxxxxx", 
)

sql = "select * from <db_name>.<tb_name> where date='2024-10-23';"
with connect(**config) as conn:
    # 请求 polars 
    df_pl = query_polars(sql, conn)
    # 请求 pandas
    df_pd = query_pandas(sql, conn)