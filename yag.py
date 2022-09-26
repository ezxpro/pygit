import os

# empty yag file
def init(repo):
    """Criar diretório para o repositório e inicializa
    o diretório .git"""
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))