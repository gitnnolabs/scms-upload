from lxml import etree

from .file_utils import numbered_lines

import re


PATTERN_START_END_LINE_NUMBERS = r'.* line (?P<start>\d*) and .*, line (?P<end>\d*),'
PATTERN_START_LINE_NUMBER = r'.* line (?P<start>\d*),'


class XMLFormatError(Exception):
    def __init__(self, start_row, end_row, column, message):
        self.start_row = start_row
        self.end_row = end_row
        self.column = column
        self.message = message

    def __str__(self):
        return self.msg


def _extract_start_row_number(msg):
    for ptn in [
        PATTERN_START_END_LINE_NUMBERS,
        PATTERN_START_LINE_NUMBER,
    ]:
        match = re.search(ptn, msg)
        if match and 'start' in match.groupdict():
            return int(match.groupdict()['start'])


def convert_xml_str_to_etree(xml_str):
    try:
        return etree.fromstring(xml_str)

    except etree.XMLSyntaxError as e:
        end_row, col = e.position
        msg = e.msg

        start_row = _extract_start_row_number(msg)

        raise XMLFormatError(
            start_row=start_row,
            end_row=end_row,
            column=col,
            message=msg,
        )


def get_snippet(xml_data, start_row, end_row):
    lines = []

    if not start_row:
        return lines

    if not end_row:
        end_row = start_row

    for line_number, content in numbered_lines(xml_data):
        if line_number >= start_row and line_number <= end_row:
            lines.append(content.encode())

    return lines
