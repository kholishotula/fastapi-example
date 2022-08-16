from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def encrypt(password: str):
        hashed_pwd = pwd_ctx.hash(password)
        return hashed_pwd

    def verify(hashed_pwd: str, plain_pwd: str):
        return pwd_ctx.verify(plain_pwd, hashed_pwd)
