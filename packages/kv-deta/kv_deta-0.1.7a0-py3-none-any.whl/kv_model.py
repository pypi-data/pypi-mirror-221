####
##
#
#


__version__ = "0.1.7-alpha"

import re

import more_itertools as mit
from deta import Base as DetaBase
from deta import Deta

# from pydantic import BaseModel, Field


# class KVModel(dict, BaseModel):
class KVModel(dict):
    class Config:  # (BaseModel.Config):
        arbitrary_types_allowed: bool = True
        deta_key: str = DETA_BASE_KEY if "DETA_BASE_KEY" in globals() else None
        deta = (
            Deta(DETA_BASE_KEY)
            if "Deta" in globals() and "DETA_BASE_KEY" in globals()
            else None
        )
        orm_mode: bool = False
        property_set_methods: dict = {}
        table_name: str = None
        underscore_attrs_are_private: bool = False
        # validate_assignment: bool = True

        # def __init__(self, *args, **kwargs):
        #    super(__class__, BaseModel).__init__(*args, **kwargs)
        #    self._set_table_name()
        #    self._set_db()

        # for name, field in cls.__fields__.items():
        #    setattr(cls, name, DetaField(field=field))

        pass

    @property
    # def __db(cls):
    # @classmethod
    def _db(cls):
        return getattr(cls.Config, "deta", cls._set_db())

    @classmethod
    def _set_db(cls, dbname: DetaBase = None):
        cls.Config.deta = (Deta(cls.Config.deta_key)).Base(
            getattr(cls.Config, "table_Name", cls._set_table_name())
        )
        return cls.Config.deta

    @classmethod
    def _set_table_name(cls, table_name: str = None) -> str:
        if table_name:
            setattr(cls.Config, "table_Name", table_name)
        if getattr(cls.Config, "table_name", None) is None:
            setattr(
                cls.Config,
                "table_name",
                re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower(),
            )
        return cls.Config.table_name

    def __read__(self):
        pass

    # def __getattr__(self, key: str):
    #    print('__getattr__', key)
    #    print(hasattr(super(), key))
    #    print(key in super(), dir(self))
    #    return getattr(self, key, default=self.setdefault(key, None))

    def __setattr__(self, name: str, data=None):
        print("setatr base model", self.__class__, name, data)

        method = (
            self.Config.property_set_methods.get(name)
            if (
                hasattr(self.Config, "property_set_methods")
                and isinstance(self.Config.property_set_methods, (list, dict))
            )
            else None
        )
        if method is not None:
            print("getattr(self, method)(data)", data)
            data = getattr(self, method)(data)
        #   метод-сеттер должен возвращать данные, которые вносим в текущую модель

        try:
            super().__data = self.__db__.put(
                self.__read__(self.key) if self.key else {}, **{name: data}
            )
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        return data

    def __delattr__(self, name: str):
        print("__delattr__", name)
        pass

    def get(self, key: str, default=None):
        key = str(key)
        if self.setdefault(key, self._db.get(key)) is None and default is not None:
            self[key] = default

        return self[key]

    def inc(self, key):
        pass

    def dec(self, key):
        pass

    def save(self):
        [  # instead map()
            self._db.put_many(chunk)
            for chunk in mit.chunked(
                [{"key": str(k), "value": v} for k, v in self.items()], 25
            )
        ]

        return self

    @classmethod
    def put_many(cls, *args, **kwargs) -> None:
        raise Exception(
            (
                f"class {cls.__name__} have not put many data, use method `.save()` instead"
            )
        )
        pass
