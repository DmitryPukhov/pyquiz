import re
from typing import List


class ReorderLogFiles:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        out = sorted(logs, key=self.getsortkey)
        return out

    def getsortkey(self, str: str) -> str:
        m = re.match(r'^([\w\d]+)\s+(.*)$', str)
        id = m.group(1)
        val = m.group(2)
        # Do not sort digit logs
        key = (1,) if val.replace(' ', '').isdigit() else (0, val, id)
        return key
