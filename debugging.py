import logging

import config


_handler_paths = set()


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
            _handler_paths.add(filepath)
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
    raise NotImplementedError


def _is_my_handler(h):
    return isinstance(h, logging.FileHandler) \
           and h.baseFilename == debug_filepath