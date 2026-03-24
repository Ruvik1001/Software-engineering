from dataclasses import dataclass


@dataclass
class AuthUser:
    login: str
    password: str
    first_name: str
    last_name: str
