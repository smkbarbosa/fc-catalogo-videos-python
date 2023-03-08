import unittest
from abc import ABC
from dataclasses import dataclass, is_dataclass

from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.entities import Entity


@dataclass(frozen=True, kw_only=True)
class StubEntity(Entity):
    prop1: str
    prop2: str


class TestEntityUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_props(self):
        entity = StubEntity(prop1="some id", prop2="some prop")
        self.assertEqual(entity.prop1, "some id")
        self.assertEqual(entity.prop2, "some prop")
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)

    def test_accept_a_valid_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                id="a4a7d7e0-5c1e-4b5d-8e0d-2d3b0d2b0d2b"),
            prop1="some id",
            prop2="some prop",
        )
        self.assertEqual(entity.id, "a4a7d7e0-5c1e-4b5d-8e0d-2d3b0d2b0d2b")

    def test_to_dict_method(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                id="a4a7d7e0-5c1e-4b5d-8e0d-2d3b0d2b0d2b"),
            prop1="some id",
            prop2="some prop",
        )
        self.assertDictEqual(
            entity.to_dict(),
            {
                "id": "a4a7d7e0-5c1e-4b5d-8e0d-2d3b0d2b0d2b",
                "prop1": "some id",
                "prop2": "some prop",
            },
        )
