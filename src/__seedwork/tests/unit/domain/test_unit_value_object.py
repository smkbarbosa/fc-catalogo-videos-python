import unittest
import uuid
from abc import ABC
from dataclasses import FrozenInstanceError, dataclass, is_dataclass
from unittest.mock import patch

from __seedwork.domain.exceptions import InvalidUuidException
from __seedwork.domain.value_objects import UniqueEntityId, ValueObject


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        value_object = StubOneProp(prop="some value")
        self.assertEqual(value_object.prop, "some value")

        value_object2 = StubTwoProp(prop1="some value", prop2="some value 2")
        self.assertEqual(value_object2.prop1, "some value")
        self.assertEqual(value_object2.prop2, "some value 2")

    def test_convert_to_string(self):
        value_object = StubOneProp(prop="some value")
        self.assertEqual(value_object.prop, str(value_object))
        value_object2 = StubTwoProp(prop1="some value", prop2="some value 2")
        self.assertEqual(
            '{"prop1": "some value", "prop2": "some value 2"}', str(
                value_object2)
        )

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop="some value")
            value_object.prop = "some id"


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,  # pylint: disable=protected-access
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId("some invalid uuid")
                mock_validate.assert_called_once()
            self.assertEqual(str(assert_error.exception),
                             "ID must be a valid UUID")

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,  # pylint: disable=protected-access
        ) as mock_validate:
            value_object = UniqueEntityId(
                "6b9d8a6c-6c3d-4b3f-9c9d-2c9d68a6c6d3")
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, "6b9d8a6c-6c3d-4b3f-9c9d-2c9d68a6c6d3")

        uuid_value = uuid.uuid4()
        value_object = UniqueEntityId(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_uuid_when_not_passed_in_constructor(self):  # pylint: disable=no-self-use
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,  # pylint: disable=protected-access
        ) as mock_validate:
            value_object = UniqueEntityId()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = "some id"
