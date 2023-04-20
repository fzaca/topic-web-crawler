import logging
import colorlog

# Configuración del logger para archivo
logging.basicConfig(
    filename='logs/crawler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración del logger para los errores
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_logger_file_handler = logging.FileHandler('logs/error.log')
error_logger_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
error_logger.addHandler(error_logger_file_handler)

# Configuración del logger para la consola
console_info_handler = colorlog.StreamHandler()
console_info_handler.setLevel(logging.INFO)
formatter = colorlog.ColoredFormatter(
    "%(cyan)s%(asctime)s %(log_color)s%(bold)s%(levelname)s:%(reset)s %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)
console_info_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_info_handler)

console_error_handler = colorlog.StreamHandler()
console_error_handler.setLevel(logging.ERROR)
console_error_formatter = colorlog.ColoredFormatter(
    "%(cyan)s%(asctime)s %(red)s%(bold)s%(levelname)s:%(reset)s %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)
console_error_handler.setFormatter(console_error_formatter)
error_logger.addHandler(console_error_handler)