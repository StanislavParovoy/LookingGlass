
import config
from core.css import css


# GLOBALS
OKAY                    = 0
ERR                     = -1
DELAY_BETWEEN_THREADS   = 0.002
PROGRESS_PRINT          = 100
WRITE_BINARY            = 'wb'
REPORT_FOLER            = "Report/"
OUTPUT_FILE             = REPORT_FOLER + "Report.csv"
SEPARATOR               = " ; "
TEMP_MARKDOWN_LOC       = 'temp.md'
HTML_REPORT             = REPORT_FOLER + "Report.html"
HARCODED_FUCKING_CSS    = css
READ                    = 'r'
READ_BINARY             = 'rb'
WRITE_BINARY            = 'wb'
WRITE                   = 'w'


# SHARED
config.PACKETS          = []
FALSE_POSITIVES         = False
VERBOSITY               = False
config.USER_REQUESTS    = []


# VERSION INFORMATION
NAME                    = "LookingGlass"
NUMERIC_VERSION         = "1.6.0"
NAME_VERSION            = "GEN"
AUTHORS                 = ["Yuval tisf Nativ", "Dagan Pasternak"]
THIS_YEAR               = 2016


# REGEXES:
SINGLE_COORD            = r'^(([\+\-])?\d{1,3}\.\d{2,17})$'
COORDINATES             = r'^(([\+\-])?\d{1,3}\.\d{2,17})[\,\s](([\+\-])?\d{1,3}\.\d{2,17})$'
EMAIL                   = r'([a-zA-Z0-9\-\.\_]+(\@| at )[a-zA-Z0-9\-\.\_]{3,16}(\.|dot| dot )[a-zA-Z0-9\-\.\_]{2,3})'
MAC_ADDR                = r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
IMEI_NOT_REALLY_REGEX   = r'(\d{15})'
IP_ADDR                 = r'((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))'
