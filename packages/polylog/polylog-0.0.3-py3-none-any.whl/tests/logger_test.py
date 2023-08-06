import unittest
from io import StringIO
from contextlib import redirect_stdout
import logging
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from polylog import setup_logger, TRACE_ID, SPAN_ID     # noqa: E402
from polylog.logger import CustomFormatter              # noqa: E402


class LoggerTests(unittest.TestCase):
    def setUp(self):
        self.stream = StringIO()
        self.log = logging.getLogger('test_logger')
        self.log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(self.stream)
        handler.setFormatter(CustomFormatter())
        self.log.addHandler(handler)
        os.environ["LOG_LEVEL"] = "DEBUG"

    def test_setup_logger(self):
        logger = setup_logger(self.log.name)
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, self.log.name)

    def test_trace_id(self):
        TRACE_ID.set('12345')
        SPAN_ID.set(None)
        self.log.debug('Test log message.')
        log_output = self.stream.getvalue()
        self.assertIn('traceId=12345', log_output)
        self.assertNotIn('spanId', log_output)

    def test_span_id(self):
        TRACE_ID.set(None)
        SPAN_ID.set('67890')
        self.log.debug('Test log message.')
        log_output = self.stream.getvalue()
        self.assertNotIn('traceId', log_output)
        self.assertIn('spanId=67890', log_output)

    def test_both_ids(self):
        TRACE_ID.set('12345')
        SPAN_ID.set('67890')
        self.log.debug('Test log message.')
        log_output = self.stream.getvalue()
        self.assertIn('traceId=12345', log_output)
        self.assertIn('spanId=67890', log_output)

    def test_neither_id(self):
        TRACE_ID.set(None)
        SPAN_ID.set(None)
        self.log.debug('Test log message.')
        log_output = self.stream.getvalue()
        self.assertNotIn('traceId', log_output)
        self.assertNotIn('spanId', log_output)

    def test_log_levels(self):
        logger = setup_logger(self.log.name)

        with redirect_stdout(self.stream):
            logger.debug('Debug log message.')
            logger.info('Info log message.')
            logger.warning('Warning log message.')
            logger.error('Error log message.')
            logger.critical('Critical log message.')

        log_output = self.stream.getvalue()
        self.assertIn('Debug log message.', log_output)
        self.assertIn('Info log message.', log_output)
        self.assertIn('Warning log message.', log_output)
        self.assertIn('Error log message.', log_output)
        self.assertIn('Critical log message.', log_output)

    def test_environment_variable_configuration(self):
        os.environ["LOG_LEVEL"] = "WARNING"
        logger = setup_logger(self.log.name)

        # Ensure that debug and info messages are not logged
        with redirect_stdout(self.stream):
            logger.debug('Debug log message should not appear.')
            logger.info('Info log message should not appear.')

        log_output = self.stream.getvalue()
        self.assertNotIn('Debug log message', log_output)
        self.assertNotIn('Info log message', log_output)

        # Ensure that warning, error, and critical messages are logged
        with redirect_stdout(self.stream):
            logger.warning('Warning log message should appear.')
            logger.error('Error log message should appear.')
            logger.critical('Critical log message should appear.')

        log_output = self.stream.getvalue()
        self.assertIn('Warning log message', log_output)
        self.assertIn('Error log message', log_output)
        self.assertIn('Critical log message', log_output)


if __name__ == '__main__':
    unittest.main()
