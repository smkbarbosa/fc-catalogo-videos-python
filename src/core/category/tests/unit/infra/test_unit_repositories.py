import unittest
from core.category.domain.entities import Category

from core.category.infra.in_memory.repositories import CategoryInMemoryRepository


class TestCategoryInMemoryRepositoryUnit(unittest.TestCase):

    repo: CategoryInMemoryRepository

    def setUp(self):
        self.repo = CategoryInMemoryRepository()

    def test_if_filter_is_null(self):
        et = Category(name='Animação')  # pylint: disable=invalid-name

        items = [et]
        # pylint: disable=protected-access
        result = self.repo._apply_filter(items, None)
        self.assertEqual(items, result)

    def test_filter(self):

        items = [
            Category(name='terror'),
            Category(name='TERROR'),
            Category(name='Comédia'),
        ]

        result = self.repo._apply_filter(items, 'TERROR')  # pylint: disable=protected-access
        self.assertEqual(result, [items[0], items[1]])

    def test_sort_by_created_at_is_null(self):
        items = [
            Category(name='terror', created_at='2021-01-02'),
            Category(name='TERROR', created_at='2021-01-01'),
            Category(name='Comédia', created_at='2022-01-02'),
        ]

        result = self.repo._apply_sort(items, None, None)  # pylint: disable=protected-access
        self.assertEqual(result, [items[2], items[0], items[1]])

    def test_sort_by_name(self):
        items = [
            Category(name='terror'),
            Category(name='Animação'),
            Category(name='Comédia'),
            Category(name='Anime'),
            Category(name='Ficção'),
            Category(name='Infantil'),
        ]

        result = self.repo._apply_sort(items, 'name', 'asc')  # pylint: disable=protected-access
        self.assertEqual(result, [items[1], items[3],
                         items[2], items[4], items[5], items[0]])

        result = self.repo._apply_sort(items, 'name', 'desc')  # pylint: disable=protected-access
        self.assertEqual(result, [items[0], items[5],
                         items[4], items[2], items[3], items[1]])
