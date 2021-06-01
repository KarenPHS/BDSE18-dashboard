from app import db
import pandas as pd

sql_cmd = """
        select TSE_industry_new, company, abbr
        from stock_list
        """

sql_cmd_ae = """
        select TSE_industry_new, company, abbr
        from ae_bankruptcy_list
        """
# query_data = db.engine.execute(sql_cmd).fetchall()

all_df = pd.read_sql_query(sql_cmd, db.engine)
all_df.columns = ["產業別", "股票代碼", "公司名稱"]
stocklist = all_df.sort_values(by=['股票代碼','產業別']).to_numpy().tolist()

ae_bankruptcy_df = pd.read_sql_query(sql_cmd_ae, db.engine)
ae_bankruptcy_df.columns = ["產業別", "股票代碼", "公司名稱"]
bankruptcy_stocklist = ae_bankruptcy_df.sort_values(by=['股票代碼','產業別']).to_numpy().tolist()
