# Logger specific - good for production
import logging

def setup_logger():
    """Configure a basic logger"""
    logger = logging.getLogger("Web UI Automation")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger