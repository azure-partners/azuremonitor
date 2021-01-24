from config import connection_string
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

logger.addHandler(AzureLogHandler(
    connection_string=connection_string)
)

def valuePrompt():
    line = input("Enter a value: ")
    logger.warning(line)

def main():
    while True:
        valuePrompt()

if __name__ == "__main__":
    main()
