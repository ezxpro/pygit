import os

def ler_arquivo(caminho):
    """Lê como bytes o conteúdo do arquivo especificado no caminho"""
    with open(caminho, 'rb') as f:
        return f.read()


def escrever_arquivo(caminho, dados):
    """Escreve dados (bytes) em arquivo especificado no caminho"""
    with open(caminho, 'wb') as f:
        return f.write(dados)


def init(repo):
    """Criar diretório para o repositório e inicializa
    o diretório .git"""
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for nome in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', nome))
    escrever_arquivo(os.path.join(repo, '.git', 'HEAD'))


def hash_object(data, obj_type, write=True):
    """Compute hash of object data of given type and write to object store
    if "write" is True. Return SHA-1 object hash as hex string.
    """
    header = '{} {}'.format(obj_type, len(data)).encode()
    full_data = header + b'\x00' + data
    sha1 = hashlib.sha1(full_data).hexdigest()
    if write:
        path = os.path.join('.git', 'objects', sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            write_file(path, zlib.compress(full_data))
    return sha1