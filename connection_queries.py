import mysql.connector
import pandas as pd

def connect_queries(year , month , file_name) : 
    
    conn = mysql.connector.connect(
        host="host",         
        user="DB_username",    
        password="DB_Password", 
        database="BOOK_SHOP" )


    query1 = f"""  select SUM( quantity) as total_sales from orders where 
    year(order_date) = {year} and month(order_date) = {month}"""

    query2 = f"""select COALESCE(SUM(price * quantity), 0) as total_revnue  from orders as total_sales where 
    year(order_date) = {year} and month(order_date) = {month}"""

    query3 = f"""select  COALESCE(SUM(orders.price * orders.quantity), 0)
    as sales , books.titel as best_selers  from orders inner join books 
    on orders.book_id = books.book_id where year(orders.order_date) = {year} 
    and month(order_date) = {month}  group by orders.book_id , books.titel order by 
    COALESCE(SUM(orders.price * orders.quantity), 0) desc"""

    query4 = f"""SELECT 
        c.cat_id,
        c.name as category ,
        coalesce(SUM(o.price * o.quantity),0)  AS total_sales,
        COUNT(DISTINCT o.order_id) AS order_count
    FROM orders o
    JOIN book_categories bc ON o.book_id = bc.book_id
    JOIN categories c ON bc.cat_id = c.cat_id
    where year(o.order_date) = {year} and month(o.order_date) = {month}
    GROUP BY c.cat_id, c.name
    ORDER BY total_sales DESC"""

    df1 = pd.read_sql(query1, conn)
    df2 = pd.read_sql(query2, conn)
    df3 = pd.read_sql(query3, conn)
    df4 = pd.read_sql(query4, conn)



    print(df1 ,df2 , df3 , df4 )
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
        df1.to_excel(writer, sheet_name="Total Books Sold", index=False)
        df2.to_excel(writer, sheet_name="Total Revenue", index=False)
        df3.to_excel(writer, sheet_name="Top Books", index=False)
        df4.to_excel(writer, sheet_name="Sales by Category", index=False)

    conn.close()