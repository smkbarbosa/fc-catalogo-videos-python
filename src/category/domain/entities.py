from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Optional

from __seedwork.entities.entities import Entity


# implementa o init, repr, eq
@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())

    def update(self, name: str, description: Optional[str] = None):
        self._set('name', name)
        self._set('description', description)

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)
   