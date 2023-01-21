import pytest
from api.serializers import LocationSerializer


@pytest.mark.django_db
def test_location_serializer_result():
    location_name = "foo"
    location_type = "bar"
    location_dimension = "foo_bar"

    serializer = LocationSerializer(
        data={
            "name": location_name,
            "type": location_type,
            "dimension": location_dimension,
        }
    )

    assert serializer.is_valid()
    location = serializer.save()
    assert location.name == location_name
    assert location.type == location_type
    assert location.dimension == location_dimension
    assert location.createdAt
    assert location.editedAt
