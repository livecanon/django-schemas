import pytest
from django.db import IntegrityError

from api.models import Location


def test_location_model_str_repr(sample_location):
    assert str(sample_location) == "foo"


def test_character_model_str_repr(sample_character):
    assert str(sample_character) == "foo_2"


def test_episode_model_str_repr(sample_episode):
    assert str(sample_episode) == "space odyssey"


@pytest.mark.usefixtures("sample_location")
def test_create_location_with_name_that_already_exists():
    with pytest.raises(IntegrityError):
        Location.objects.create(name="foo")
