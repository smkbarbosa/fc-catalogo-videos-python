import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime
from unittest.mock import patch

from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):  # sourcery skip: extract-duplicate-method
        with patch.object(Category, 'validate') as mock_validate_method:
            category = Category(name="Movie")
            mock_validate_method.assert_called_once()
            self.assertEqual(category.name, "Movie")
            self.assertEqual(category.description, None)
            self.assertEqual(category.is_active, True)
            self.assertIsInstance(category.created_at, datetime)

            created_at = datetime.now()
            category1 = Category(
                name="Terror",
                description="some description",
                is_active=False,
                created_at=created_at,
            )

            self.assertEqual(category1.name, "Terror")
            self.assertEqual(category1.description, "some description")
            self.assertEqual(category1.is_active, False)
            self.assertEqual(category1.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        with patch.object(Category, 'validate'):
            category1 = Category(name="Animação")
            category2 = Category(name="Terror")
            self.assertNotEqual(
                category1.created_at.timestamp(), category2.created_at.timestamp()
            )

    def test_if_is_immutable(self):
        with patch.object(Category, 'validate'):
            with self.assertRaises(FrozenInstanceError):
                category = Category(name="Movie")
                category.name = "some name"

    def test_update_category(self):
        with patch.object(Category, 'validate'):
            category = Category(name="Movie")
            category.update(name="some name", description="some description")
            self.assertEqual(category.name, "some name")
            self.assertEqual(category.description, "some description")

    def test_activate(self):
        with patch.object(Category, 'validate'):
            category = Category(name="Movie")
            category.activate()
            self.assertTrue(category.is_active)

    def test_deactivate(self):
        with patch.object(Category, 'validate'):
            category = Category(name="Movie")
            category.deactivate()
            self.assertFalse(category.is_active)
