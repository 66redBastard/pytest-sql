import logging

from colorama import Fore, Style, init

init(autoreset=True)


def get_logger():
    logger = logging.getLogger("pytest_sql")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


logger = get_logger()


def log_database_connection_attempt(db_name, user, host, port):
    logger.info(
        f"{Fore.YELLOW}Attempting to connect to database '{db_name}' as user '{user}' at '{host}:{port}'{Style.RESET_ALL}"
    )


def log_database_connection_success(db_name):
    logger.info(
        f"{Fore.GREEN} Successfully connected to database '{db_name}'{Style.RESET_ALL}"
    )


def log_database_connection_failure(db_name, error):
    logger.error(
        f"{Fore.RED} Failed to connect to database '{db_name}': {error}{Style.RESET_ALL}"
    )


def log_error_insertion(exc):
    logger.error(f"{Fore.RED}Error inserting data: {exc}{Style.RESET_ALL}")


def log_database_disconnection(db_name):
    logger.info(f"{Fore.CYAN}Disconnected from database '{db_name}'{Style.RESET_ALL}")


def log_api_request(url, status_code):
    logger.info(
        f"{Fore.MAGENTA}API request to '{url}' returned status code {status_code}{Style.RESET_ALL}"
    )


def log_api_request_failure(url, error):
    logger.error(f"{Fore.RED}API request to '{url}' failed: {error}{Style.RESET_ALL}")
