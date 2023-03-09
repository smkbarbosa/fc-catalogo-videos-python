from typing import List
from __seedwork.domain.repositories import InMemorySearchableRepository
from category.domain.entities import Category
from category.domain.repositories import CategoryRepository


class CategoryInMemoryRepository(CategoryRepository, InMemorySearchableRepository):
    # Poderemos filtrar categorias por seu nome, qualquer termo passado deverá ser pesquisa
    # do começo ao fim do valor do nome
    # Se no filtro não existir um parâmetro de ordenação,
    # precisa ordenar por padrão pelo created_at.
    sortable_fields: List[str] = ["name", "created_at"]

    def _apply_filter(self, items: List[Category], filter_param: str = None) -> List[Category]:
        if filter_param:
            obj = filter(
                lambda x: x.name.lower() in filter_param.lower(), items
            )
            return list(obj)
        return items

    def _apply_sort(self, items: List[Category],
                    sort: str = None, sort_dir: str = None) -> List[Category]:
        return super()._apply_sort(items, sort, sort_dir) \
            if sort \
            else super()._apply_sort(items, 'created_at', 'desc')
