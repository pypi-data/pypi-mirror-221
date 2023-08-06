#!/usr/bin/env python
#
# Author: Gwansuk Oh
# Description:
# Short and ill written script for extracting a transcript of a YouTube Video.
# Too many unnecessary  dependencies, but does the job.
#
# Usage:
# $> yt-pull "https://www.youtube.com/watch?v=some-ytvideo-id"

import sys
import click
from typing import List, Dict, Union, Optional, Literal, Any
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi as YTApi
import clipboard
import logging
import logging.config
import traceback
import copy


class ColorizedFormatter(logging.Formatter):
    level_name_colors = {
        logging.DEBUG: lambda level_name: click.style(str(level_name), fg="cyan"),
        logging.INFO: lambda level_name: click.style(str(level_name), fg="green"),
        logging.WARNING: lambda level_name: click.style(str(level_name), fg="yellow"),
        logging.ERROR: lambda level_name: click.style(str(level_name), fg="red"),
        logging.CRITICAL: lambda level_name: click.style(str(level_name), fg="bright_red"),
    }

    def __init__(
        self,
        fmt: Optional[str] = None,
        datefmt: Optional[str] = None,
        style: Literal["%", "{", "$"] = "%",
        use_colors: Optional[bool] = None,
    ) -> None:
        if use_colors in (True, False):
            self.use_colors = use_colors
        else:
            self.use_colors = sys.stdout.isatty()
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

    def color_level_name(self, level_name: str, level_no: int) -> str:
        def default(level_name: str) -> str:
            return str(level_name)  # pragma: no cover
        func = self.level_name_colors.get(level_no, default)
        return func(level_name)

    def formatMessage(self, record: logging.LogRecord) -> str:
        recordcopy = copy.copy(record)
        levelname = recordcopy.levelname
        seperator = " " * (8 - len(recordcopy.levelname))
        if self.use_colors:
            levelname = self.color_level_name(levelname, recordcopy.levelno)
        recordcopy.getMessage()
        recordcopy.__dict__["levelprefix"] = levelname + ":" + seperator
        return super().formatMessage(recordcopy)


LOGGING_CONFIG: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": ColorizedFormatter,
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "stdout": {
            "()": ColorizedFormatter,
            "fmt": "%(message)s",
            "use_colors": None,
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "stdout": {
            "formatter": "stdout",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "yt-pull": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "yt-pull.stdout": {"handlers": ["stdout"], "level": "INFO", "propagate": False},
    },

}


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('yt-pull')
stdout = logging.getLogger('yt-pull.stdout')


def extract_yt_transcript(
    url: str,
    output: Optional[str] = None,
    sep: str = " ",
    lang: str = "en",
    verbose: bool = False,
    ) -> str:

    try:
        logger.disabled, logger_disabled = not verbose, logger.disabled
        stdout.disabled, stdout_disabled = not verbose, stdout.disabled

        logger.info(f"URL: {url}")
        video_id: str = parse_qs(urlparse(url).query)['v'][0]
        logger.info(f"Video ID: {video_id}")
        lang = lang.strip().lower()
        logger.info(f"Selected language: {lang}")
        logger.info(f"Retrieving the transcript...")
        transcript: List[Dict[str, Union[float, str]]] = \
            YTApi.get_transcript(video_id, languages=[lang])
        text = sep.join([t.get('text', '').replace('\n', sep) for t in transcript])
        logger.info(f"Extracted {len(text)} characters.")
        text = f"Transcript of ID-{video_id} in {lang}:\n\n" + text

        if output:
            logger.info(f"Writing the output file to: {output}")
            with open(output, 'w+') as f:
                f.write(text)
            logger.info(f"Finished writing file: {output}")

        else:
            stdout.info("\n" + text + "\n")
            clipboard.copy(text)
            logger.info("Transcript is coppied to the clipboard.")

        logger.info(f"Done.")

        return text

    except Exception as e:
        msg = "[Exception Details]\n" + str(e) + '\n' + str(traceback.format_exc())
        logger.error(
            f" Cannot extract the video or the transcript in the selected language.\n" + msg)
        raise e

    finally:
        logger.disabled, stdout.disabled = logger_disabled, stdout_disabled


@click.command()
@click.argument('url', type=str)
@click.option('-o', '--output', type=str, default=None, help="Path for saving the transcript to a file.", show_default=True)
@click.option('-s', '--sep', type=str, default=" " , help="Seperator for joining lines.", show_default=True)
@click.option('-l', '--lang', type=str, default="en", help="Transcript language; must be provided by the source otherwise, error will occur.", show_default=True)
def main(
    url: str,
    output: Optional[str] = None,
    sep: str = " ",
    lang: str = "en",
    ) -> None:
    try:
        extract_yt_transcript(url, output, sep, lang, True)
    except:
        exit(1)


__all__ = [
    'extract_yt_transcript',
    'main',
]

if __name__ == '__main__':
    main()
