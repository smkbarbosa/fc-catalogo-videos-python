from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass() #implementa o init, repr, eq
class Category:

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())


    # Piramide de testes
    # - Unidade
    # - Integração
    # - e2e