from datetime import datetime
from time     import time
from colorama import Fore, init
from .colors  import *

from .console import Settings


class log:
    def __init__(self) -> None:
        init(autoreset=True)

    @staticmethod
    def _get_timestamp():
        if Settings.timestamp:
            timestamp = f"[{Settings.c_SECO}{datetime.fromtimestamp(time()).strftime('%H:%M:%S')}{Fore.RESET}]"
            if not Settings.wrapTime:
                timestamp = timestamp[1:-1]
        else:
            timestamp = ""
        return timestamp
    
    @staticmethod
    def success(text: str, sep: str = " "):
        timestamp = log._get_timestamp()
        print(f"{timestamp} {Fore.GREEN}YES {Fore.LIGHTBLACK_EX}{sep}{Fore.RESET}{text}")
        
    @staticmethod
    def info(text: str, sep: str = " "):
        timestamp = log._get_timestamp()
        print(f"{timestamp} {Fore.LIGHTMAGENTA_EX}INF {Fore.LIGHTBLACK_EX}{sep}{Fore.RESET}{text}")

    @staticmethod
    def error(text: str, sep: str = " "):
        timestamp = log._get_timestamp()
        print(f"{timestamp} {Fore.LIGHTRED_EX}ERR {Fore.LIGHTBLACK_EX}{sep}{Fore.RESET}{text}")

    @staticmethod
    def fatal(text: str, sep: str = " "):
        timestamp = log._get_timestamp()
        print(f"{timestamp} {Fore.RED}FTL {Fore.LIGHTBLACK_EX}{sep}{Fore.RESET}{text}")

