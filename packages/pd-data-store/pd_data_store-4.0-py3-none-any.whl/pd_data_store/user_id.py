from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from .base_table import BaseTable


@dataclass
class UserID(BaseTable):
    user_email: Optional[str] = None # Key
    healthie_id: Optional[str] = None
    shopify_id: Optional[str] = None
    zoho_id: Optional[str] = None
    zendesk_id: Optional[str] = None
    cloudpat_id: Optional[str] = None
    cloudpat_subscription_id: Optional[str] = None
    updated_at: Optional[datetime] = None
