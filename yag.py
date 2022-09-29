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