import unittest
from src.monitoring import monitor_pipeline

class TestMonitorPipeline(unittest.TestCase):

    def test_monitor_pipeline_success(self):
        monitor_pipeline(success=True)
        # No assertion, just checking for any exceptions

    def test_monitor_pipeline_failure(self):
        monitor_pipeline(success=False)
        # No assertion, just checking for any exceptions
