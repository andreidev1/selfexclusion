from dataclasses import dataclass
from typing import List
from stopgambling.globals.functions.utils import verify_cnp, verify_phone, verify_email, hash_image_name

@dataclass
class User:
    name: str
    cnp: str
    number_phone: str
    email_address: str
    selfie_kyc: str
    number_phone: str
    email_address: str
    selfie_kyc: str
    verified: any
    selected_casinos: List
    period: str
    timestamp: str


def test_new_user():
    pass