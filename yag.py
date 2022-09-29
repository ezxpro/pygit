import os

def read_file(path):
    """Lê os conteúdos dos arquivos, dado um caminho em bytes"""

def write_file(path, data):
    """"""

def init(repo):
    """Criar diretório para o repositório e inicializa
    o diretório .git"""
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for name in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', name))
    write_file(os.path.join(repo, '.git', 'HEAD'))