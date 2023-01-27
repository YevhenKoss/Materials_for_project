import re
from datetime import datetime


def phone_number_validation(phone):
    if isinstance(phone, str):
        phone = phone
    else:
        phone = str(phone)
    phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if phone.isdigit() and len(phone) == 12:
        phone = phone
    else:
        raise ValueError(
            f"Phone {phone} is not saved!\nWrong phone number format! Try '+XX(XXX)XXX-XX-XX'"
        )
    return phone


def birthday_validation(birthday):
    try:
        return datetime.strptime(str(birthday), "%d.%m.%Y").date()
    except ValueError:
        return f"Date of birth {birthday} is not saved!\nYou have to enter numbers separated by a dot: DD.MM.YYYY"


def mail_validation(mail):
    mail = mail.lower()
    if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mail):
        raise ValueError(
            f"Email {mail} is not saved!\nWrong email format!"
        )
    return mail
