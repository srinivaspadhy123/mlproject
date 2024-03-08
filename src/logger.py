import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Logging file name
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # log file name structure to be added with current working directory with starting logs<LOGFILENAME>
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # The file path to the log file

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


if __name__=="__main__":
    logging.info("Logging has started")




