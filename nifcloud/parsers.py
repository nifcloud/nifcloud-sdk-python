from botocore import parsers, utils


class ComputingQueryParser(parsers.QueryParser):

    def __init__(self, timestamp_parser=None, blob_parser=None):
        super(ComputingQueryParser, self).__init__(
            self.parse_timestamp, blob_parser
        )

    def parse_timestamp(self, value):
        if value == "":
            return None
        else:
            return utils.parse_timestamp(value)

    @parsers._text_content
    def _handle_integer(self, shape, text):
        if text == "":
            return None
        return super(ComputingQueryParser, self)._handle_integer(shape, text)


parsers.PROTOCOL_PARSERS.update({
    'computing': ComputingQueryParser,
    'script': parsers.QueryParser,
    'rdb': parsers.QueryParser,
    'nas': parsers.QueryParser
})
