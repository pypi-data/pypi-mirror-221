from dataclasses import dataclass
from typing import Mapping, Optional

from .base_table import BaseTable


@dataclass
class ShopifyOrder(BaseTable):
    order_id: Optional[str] = None # key
    order_name: Optional[str] = None
    shipping_address: Optional[Mapping[str, str]] = None
    contact_email: Optional[str] = None
    order_at: Optional[str] = None
