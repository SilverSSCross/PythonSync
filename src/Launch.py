from cli import cli_main
from config import ini_checker

ini_checker.find_iniconfig()
cli_main.main()