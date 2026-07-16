from typing import List, Optional
from .models import CustomUser

class UserRepository:
    def __init__(self):
        self.model = CustomUser

    def get_by_id(self, user_id: int) -> Optional[CustomUser]:
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None

    def create(self, username, email, password) -> CustomUser:
        return self.model.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
