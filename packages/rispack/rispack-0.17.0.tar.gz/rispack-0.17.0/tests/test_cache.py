from uuid import uuid4
from rispack.cache import GlobalCache


class TestGlobalCache:
    def test_set_cache(self, cache_table):
        cache_key = "PROFILE#1234-1234-1234-1234"
        random_value = str(uuid4())

        GlobalCache.instance().set(cache_key, {"random": random_value})

        db_key = f"CACHE#{cache_key}"
        item = cache_table.get_item(Key={"PK": db_key, "SK": "CURRENT"})["Item"]

        assert item["data"]["random"] == random_value

    def test_set_cache_with_interpolation(self, cache_table):
        interpolation_cache_key = "PROFILE#{profile_id}"
        random_value = str(uuid4())
        profile_id = "1234-1234-1234-1234"
        cache_key = f"PROFILE#{profile_id}"
        db_key = f"CACHE#{cache_key}"

        GlobalCache.instance().set(
            interpolation_cache_key, {"random": random_value, "profile_id": profile_id}
        )

        item = cache_table.get_item(Key={"PK": db_key, "SK": "CURRENT"})["Item"]

        assert item["data"]["random"] == random_value

    def test_set_invalidates_current_cache(self, cache_table):
        cache_key = "PROFILE#1234-1234-1234-1234"
        random_value = str(uuid4())
        db_key = f"CACHE#{cache_key}"

        GlobalCache.instance().set(cache_key, {"random": random_value})

        new_value = "SATOSHI"

        GlobalCache.instance().set(cache_key, {"random": new_value})

        item = cache_table.get_item(Key={"PK": db_key, "SK": "CURRENT"})["Item"]

        assert item["data"]["random"] == new_value

    def test_get_cache(self, cache_table):
        invalid_cache_key = "INVALID"
        valid_cache_key = "PROFILE#1234-1234-1234-1234"

        GlobalCache.instance().set(valid_cache_key, {})

        assert GlobalCache.instance().get(invalid_cache_key) is None
        assert GlobalCache.instance().get(valid_cache_key) is not None
        assert (
            GlobalCache.instance().get(valid_cache_key).cache_key
            == "CACHE#" + valid_cache_key
        )
