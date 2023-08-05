from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError, conint, constr, root_validator
import re

class TransactionPayment(BaseModel):
    reference_id: str
    amount: float
    customer_id: str
    transaction_date: str
    store_name: Optional[str]
    billing_descriptor: str
    siret: Optional[str]
    payment: Optional[dict]
    currency: Optional[str]
    pos_name: Optional[str]
    merchant_name: Optional[str]

    @validator('amount')
    def amount_positive(cls, value):
        if value <= 0:
            raise ValueError('Amount must be positive')
        return value

    @validator('transaction_date')
    def validate_transaction_date(cls, value):
        if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', value):
            raise ValueError('Invalid date format. Expected format: YYYY-MM-DDTHH:mm:ss')
        return value

class ReceiptPayload(BaseModel):
    reference_id: str
    amount: float
    total_tax_amount: Optional[float]
    currency: str
    date: str
    covers: Optional[int]
    table: Optional[str]
    invoice: Optional[int]
    total_discount: Optional[float]
    mode: Optional[int]
    partner_name: str
    merchant: Optional[dict]
    store: Optional[dict]
    taxes: Optional[List[dict]]
    items: Optional[List[dict]]
    payments: Optional[List[dict]]

    @validator('amount')
    def amount_non_negative(cls, value):
        if value < 0:
            raise ValueError('Amount cannot be negative')
        return value

    @validator('currency')
    def validate_currency(cls, value):
        if value not in ['EUR', 'USD']:
            raise ValueError('Invalid currency. Expected currency: EUR or USD')
        return value

    @validator('date')
    def validate_date(cls, value):
        if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', value):
            raise ValueError('Invalid date format. Expected format: YYYY-MM-DDTHH:mm:ss')
        return value

    @validator('siret')
    def validate_siret(cls, value):
        if value and (len(value) != 14 or not value.isdigit()):
            raise ValueError('Invalid SIRET number. Expected 14 digits.')
        return value

    @validator('taxes', 'items', 'payments')
    def validate_list_items(cls, value):
        if value is not None and not isinstance(value, list):
            raise ValueError('Expected a list')
        return value

    @root_validator
    def validate_tax_rate(cls, values):
        taxes = values.get('taxes', [])
        for tax in taxes:
            if 'rate' in tax and tax['rate'] not in [550, 1000, 2000]:
                raise ValueError('Invalid tax rate. Expected 550, 1000, or 2000')
        return values


def validate_transaction_payload(payload):
    if not payload:
        raise ValueError('No payload to validate')
    TransactionPayment(**payload)
    return True



def validate_receipt_payload(payload):
    if not payload:
        raise ValueError('No payload to validate')
    ReceiptPayload(**payload)
    return True

