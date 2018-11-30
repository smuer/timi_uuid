# coding: utf-8

from timi_uuid import timi_uuid


class TestTimiUUID(object):

    def test_get_id(self):
        self.id = timi_uuid.get_id()
        assert len(self.id) == 36

    def test_get_id_info(self):
        self.id_info = timi_uuid.get_id_info(timi_uuid.get_id())
        assert isinstance(self.id_info, dict)

