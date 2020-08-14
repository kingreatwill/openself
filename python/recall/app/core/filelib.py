import hashlib
import magic


# pip install python-magic-bin
# pip install python-magic

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
    result = __sha1(file)
    file.seek(0)
    return result


# 一定要是rb
def md5(file):
    if isinstance(file, str):
        with open(file, 'rb') as f:
            return __md5(f)
    result = __md5(file)
    file.seek(0)
    return result


f = magic.Magic(mime=True, uncompress=True)


def mime(file):
    if isinstance(file, str):
        return f.from_file(file)
    buff = file.read(2048)
    file.seek(0)
    return f.from_buffer(buff)
