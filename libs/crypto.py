import hashlib


def encrypt_password(origin: str, salt: int) -> str:
    """
    md5随机数加密用户密码
    :param values:
    :param salt:
    :return:
    """
    string = origin + str(salt)
    return hashlib.md5(string.encode(encoding='utf-8')).hexdigest()
