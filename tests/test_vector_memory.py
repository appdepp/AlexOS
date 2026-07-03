import pytest

from app.services.vector_memory import VectorMemory


def test_vector_memory_is_abstract():

    with pytest.raises(TypeError):
        VectorMemory()
