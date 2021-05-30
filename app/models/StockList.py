from app import db
import pandas as pd
from flask import request, render_template, abort


sql_cmd = """
        select 產業別, 股票代碼, 股票名稱, 市場別
        from stock_list
        """

# query_data = db.engine.execute(sql_cmd).fetchall()

stocklist = pd.read_sql_query(sql_cmd, db.engine).sort_values(by=['股票代碼','產業別']).to_numpy().tolist()
