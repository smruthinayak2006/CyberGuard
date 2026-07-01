from database.db_manager import create_scan
from database.db_manager import complete_scan


class ScanManager:

    def __init__(self, hostname):

        self.scan_id = create_scan(hostname)

    def finish(self):

        complete_scan(self.scan_id)