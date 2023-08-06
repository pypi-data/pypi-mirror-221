from dataclasses import dataclass
from typing import Optional

from .base_table import BaseTable


@dataclass
class CloudPATUsers(BaseTable):
    user_id: Optional[str] = None  # key
    contact_email: Optional[str] = None
