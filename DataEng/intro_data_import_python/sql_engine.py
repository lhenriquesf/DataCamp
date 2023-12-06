#%%
from sqlalchemy import create_engine, text
import pandas as pd
#%%
engine = create_engine('sqlite:///Northwind.db')

select_stmt = text("SELECT CategoryID, CategoryName, Description FROM Categories;")

#%%
df = pd.read_sql_query(select_stmt, engine)

# with engine.connect() as conn:
#     with conn.begin():
#         rs = conn.execute(select_stmt)
#         df = pd.DataFrame(rs.fetchall())
#         df.columns = rs.keys()
# %%
print(len(df))
