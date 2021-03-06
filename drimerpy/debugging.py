import logging

from drimerpy import config

__all__ = ('enable_logging_to_file',)

_handler_paths = {}


def enable_logging_to_file(filepath=config.logging_file_path):
    """
    Starts intercepting calls to all loggers and duplicates the lines into the
    specified file.

    :param filepath: Path to file we want to direct all logs to.
    :return:
    """

    if filepath not in _handler_paths:
        new_handler = logging.FileHandler(filepath)
        try:
            logging.root.addHandler(new_handler)
            _handler_paths[filepath] = new_handler
        except:
            raise


def disable_logging_to_file(filepath=config.logging_file_path):
    """
    Stop intercepting call to loggers that are being redirected to specified
    file. Note that if there are more duplicatins being done to other files,
    those will not be affected.

    :param filepath: File path for which we want to stop duplicating logs to.
    :return:
    """

    handler = _handler_paths.get(filepath)
    if handler is None:
        return

    logging.root.removeHandler(handler)
