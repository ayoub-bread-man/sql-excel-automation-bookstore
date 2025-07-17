from datetime import datetime 
from connection_queries import connect_queries
from formatings import formating_logging
from sendemail import send_mail 
import os 



now = datetime.now()
year = now.year
month = now.month 
#enter the directory you usally store your .xlsx files at  
folder = "C:/Users/..... 'file_path'"
file_name = f"monthly_report_{year}_{month:02}.xlsx"
file_path = os.path.join(folder, file_name) 

connect_queries(year , month , file_name)
formating_logging( file_path )
send_mail(year , month , file_name , file_path )

