import logging as lg

# Console logging

print "+ print: standard console message"

#INFO 20
lg.info("+ log: things running normally")

# DEBUG 10
lg.debug("+ debug: Things running normally, more details for diagnostics")

# WARNING 30
lg.warn("+ warn: in lib code when client app can be modified to eliminate the warning")
lg.warning("+ warning: to still note event when client app can do nothing about it")

# ERROR 40
lg.error("+ error: report suppression of an error without raising an exception")
lg.exception("exception: meh")
# report an error regarding a particular runtime event
# ===> raise an exception

# CRITICAL 50
lg.critical("critical: erf")

# Default level: WARNING => INFO and DEBUG not displayed on console
