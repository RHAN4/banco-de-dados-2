import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um usuário:
    service.criar_usuario("Marta", "marta@gmail.com", "123")

    # Listando todos os usuários:
    print("\nLista de todos os usuários registrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nID: {usuario.id} \nNome: {usuario.nome} \nEmail: {usuario.email} Senha:{usuario.senha}")


if __name__ == "__main__":
    main() # Chamada para função