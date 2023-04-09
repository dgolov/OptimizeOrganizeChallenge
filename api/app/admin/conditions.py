from sqladmin import ModelView
from starlette.requests import Request

from app.models.object import Condition
import humanize


class ConditionView(ModelView, model=Condition):
    icon = "fa-thin fa-bookmark"
    name_plural = "Состояния объектов"
    column_list = (
        Condition.created_at,
        Condition.value,
        Condition.updated_at,
    )
    column_labels = {
        Condition.created_at: "Создано",
        Condition.updated_at: "Обновлено",
        Condition.id: "Идентификатор",
        Condition.value: "Состояние",
    }
    column_formatters = {
        Condition.created_at: lambda m, a: humanize

    }

    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True

