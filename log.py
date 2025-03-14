import sys

from loguru import logger

logger_format: str = (
    '<dim>File <cyan>"{file.path}"</>, line <cyan>{line}</>, in <cyan>{function}</></>\n'
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</> "
    "[<level>{level}</>] "
    "<level><normal>{message}</></>"
)

logger.remove()
logger.add(
    sys.stderr,
    level=0,
    format=logger_format,
)
