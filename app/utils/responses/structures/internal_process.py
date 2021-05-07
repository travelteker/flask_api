from dataclasses import dataclass
from typing import Optional


@dataclass
class InternalProcess:

    """Class to manage structure data for internal communications"""

    operation: bool
    message: Optional[str] = None


