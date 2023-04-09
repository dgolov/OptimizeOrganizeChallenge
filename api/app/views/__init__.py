from fastapi import APIRouter
from .users import router as users_router
from .objects import router as objects_router
from .solutions import router as solutions_router
from .tasks import router as tasks_router
from .work_groups import router as work_groups_router
from .conditions import router as conditions_router

router = APIRouter()

router.include_router(prefix="/users", router=users_router, tags=["Users"])
router.include_router(prefix="/objects", router=objects_router, tags=["Objects"])
router.include_router(prefix="/solutions", router=solutions_router, tags=["Solutions"])
router.include_router(prefix="/tasks", router=tasks_router, tags=["Tasks"])
router.include_router(prefix="/work_groups", router=work_groups_router, tags=["WorkGroups"])
router.include_router(prefix="/conditions", router=conditions_router, tags=["Conditions"])
