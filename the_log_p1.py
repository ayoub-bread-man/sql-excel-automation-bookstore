from datetime import datetime
def write_log(message):
    with open("log.txt", "a") as log_file:
        #time stamping you could use it in varing situations 
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{message} [{timestamp}]\n")