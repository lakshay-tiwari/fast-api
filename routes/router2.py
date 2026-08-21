from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_msg(): 
    return {
        "msg": "admin"
    }