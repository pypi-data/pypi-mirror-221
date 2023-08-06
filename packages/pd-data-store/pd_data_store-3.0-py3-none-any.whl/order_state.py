from dataclasses import asdict, dataclass
from typing import Mapping, Optional
from .base_table import BaseTable
from . import pd_data_store
from enum import Enum
import json


OrderStates = Enum(
    "OrderStates",
    [
        "pending_payment",

        # Should have a healthie user and the zendesk phone number. Intake form should be on it's way.
        "paid",

        # Zoho should have the intake form pdf, NPF tag, New_Patient_Form field checked, consult type as "Openloop HST Pre-Test Consult" and appointment date.
        # And shopify should have the tag NPF.
        "intake_form_filled",

        # shopify order should have tag (Good To Ship), CloudPAT should have the user, Zoho should have HST-RX form, HST tag, consultation complete checked and
        # has_HST_rx set to yes.
        "HST_Rx_form_locked",

        # CloudPAT user should have a serial number and it should be subscribed to Patient Reports. Zoho should have the serial number.
        "shipment_updated",

        # Telemetry form should be stored on CloudPAT, Healthie and Zoho.
        "telemetry_ready",
    ],
)


@dataclass
class OrderState(BaseTable):
    order_id: Optional[str] = None  # Key
    order_name: Optional[str] = None
    state: Optional[OrderStates] = None

    def to_str(self) -> str:
        dict_repr = asdict(self)
        return json.dumps(dict_repr | {"state": dict_repr["state"].name})

    @classmethod
    def from_str(cls: "OrderState", raw: str) -> "OrderState":
        dict_repr = json.loads(raw)
        return cls(**(dict_repr | {"state": OrderStates[dict_repr["state"]]}))

    @classmethod
    def load(cls: "OrderState", key: str, data_store: Mapping) -> "OrderState":
        store_at = f"OrderState:{key}"
        str_repr = pd_data_store.load(data_store, store_at)
        return cls.from_str(str_repr)

    def store(self, key: str, data_store: Mapping):
        str_repr = self.to_str()
        load_from = f"OrderState:{key}"
        pd_data_store.store(data_store, load_from, str_repr)
