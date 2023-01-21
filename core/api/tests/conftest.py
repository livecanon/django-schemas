import pytest
from api.models import Location, Character, Episode
from unittest.mock import MagicMock
from django.core.files import File


@pytest.fixture
def sample_location(db):
    return Location.objects.create(
        name="foo",
        type="bar",
        dimension="foo_bar",
    )


@pytest.fixture
def sample_character(db, sample_location):
    character = Character.objects.create(
        name="foo_2",
        status="bar",
        gender="foo_bar",
        species="bar_foo",
        type="foobar",
        origin=sample_location,
    )

    character.image = MagicMock(spec=File, name="filemock")

    return character


@pytest.fixture
def sample_episode(db, sample_character):
    episode = Episode.objects.create(
        title="space odyssey",
        release="1789-9-5",
        season=5,
        episode=3,
    )

    episode.characters.add(sample_character)

    return episode
