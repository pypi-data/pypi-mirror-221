from ClickHouse import ClickHouse

ch = ClickHouse(login='click', password='click')

t  = ch.check_connection_to_database()
print(t)


# from PostgreSQL import PostgreSQL
# 
# pg = PostgreSQL(port=1)
# 
# on_conflict = pg.generate_on_conflict_sql_query(
#     source_table_schema_name='stg', target_table_schema_name='dm',
#     source_table_name='tmp_fct_sales', target_table_name='fct_sales',
#     list_columns=['id', 'date', 'amount'],
#     pk=['id','date'],
#     replace=False
# )
# 
# print(on_conflict)
