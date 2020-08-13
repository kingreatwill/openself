import hashlib


def __sha1(f):
    sha1obj = hashlib.sha1()
    sha1obj.update(f.read())
    return sha1obj.hexdigest()


def __md5(f):
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    return md5obj.hexdigest()


# 一定要是rb
def sha1(file):
    if isinstance(file, str):
        with open(file, 'rb') as f:
            return __sha1(f)
    return __sha1(file)


# 一定要是rb
def md5(file):
    if isinstance(file, str):
        with open(file, 'rb') as f:
            return __md5(f)
    return __md5(file)
