from fastapi import APIRouter
# dominio/auth/
auth_router = APIRouter(prefix='/auth', tags=["Auth"])

@auth_router.get('/')
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem": "Area de autenticacao",
            "Autenticado": False}