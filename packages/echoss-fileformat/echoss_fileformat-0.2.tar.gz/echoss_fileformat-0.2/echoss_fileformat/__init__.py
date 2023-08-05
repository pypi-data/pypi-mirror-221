from .csv_handler import CsvHandler
from .json_handler import JsonHandler
from .xml_handler import XmlHandler
from .excel_handler import ExcelHandler
from .feather_handler import FeatherHandler
from .dataframe_util import print_table, reduce_memory_usage

import logging

logger = logging.getLogger(__name__)

# if the logger have not handlers, set a logger handler to console stdout logging
if logger.handlers:
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s - %(message)s"
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

__all__ = ['CsvHandler', 'JsonHandler', 'XmlHandler', 'ExcelHandler', 'FeatherHandler',
           'print_table', 'reduce_memory_usage']