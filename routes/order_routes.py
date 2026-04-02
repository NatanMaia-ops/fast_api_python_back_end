from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["Order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema. 
    Todas as rotas de pedidos precisam de autenticação
    """
    return {"Mensagem": "Voce acessou a rota de pedidos"}

