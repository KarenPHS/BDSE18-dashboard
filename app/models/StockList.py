from app import db
import pandas as pd
from flask import request, render_template, abort


sql_cmd = """
        select TSE_industry_new, company, abbr
        from stock_list
        """

# query_data = db.engine.execute(sql_cmd).fetchall()

df = pd.read_sql_query(sql_cmd, db.engine)
df.columns = ["產業別", "股票代碼", "公司名稱"]
stocklist = df.sort_values(by=['股票代碼','產業別']).to_numpy().tolist()
