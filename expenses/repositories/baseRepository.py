# repositories/base.py
from typing import Type, Generic, TypeVar, Optional, List
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

T = TypeVar('T', bound=models.Model)

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_by_id(self, obj_id: int) -> Optional[T]:
        try:
            return self.model.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self) -> List[T]:
        return list(self.model.objects.all())

    def create(self, **kwargs) -> T:
        return self.model.objects.create(**kwargs)
