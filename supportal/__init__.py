# In a lambda environment, AWS python does some strangeness to the log handlers
# Instead, we blow away their root handler and set our own
import logging

# from ew_common.telemetry import Telemetry

root = logging.getLogger()

if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(name)s] [%(levelname)s] [%(funcName)s] [line: %(lineno)s] - %(message)s",
)

# t = Telemetry.default("supportal").as_global()
