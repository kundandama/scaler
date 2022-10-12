from typing import Dict, Any


class Registry:
    __map: dict[str, Any] = {}

    @classmethod
    def register(cls, prototype_name, class_obj):
        cls.__map.__setitem__(prototype_name, class_obj)

    @classmethod
    def get_prototype(cls, prototype_name):
        return cls.__map.get(prototype_name)
