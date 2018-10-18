import hashlib


def encrypt_password(origin: str, salt: int) -> str:
    """
    md5随机数加密用户密码
    :param origin: 原始密码
    :param salt:
    :return:
    """
    string = origin + str(salt)
    return hashlib.md5(string.encode(encoding='utf-8')).hexdigest()
