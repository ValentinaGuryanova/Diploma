import re
from fastapi import HTTPException, Query


async def check_phone(phone_number: str = Query(length=12)):
    """ Функция проверки маски телефона """

    if phone_number[:2] == "+7" and len(phone_number) == 12:
        return {phone_number}
    else:
        raise HTTPException(status_code=400,
                            detail=f"Телефон {phone_number} не соответствует заданному формату")


async def check_password(password: str = Query(min_length=8), password2: str= Query(min_length=8)):
    """ Функция проверки надежности пароля """

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[$%&!:.]", password):
        if password2 == password:
            return {"message": "Пароль создан успешно!"}
    else:
        raise HTTPException(status_code=400,
                            detail=f"Пароль не соответствует заданному формату")

