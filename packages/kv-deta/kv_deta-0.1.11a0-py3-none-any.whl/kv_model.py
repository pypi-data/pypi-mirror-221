####
##
#
#


__version__ = "0.1.11-alpha"

import re

import more_itertools as mit
from deta import Base as DetaBase
from deta import Deta


# class KVModel(dict, BaseModel):
class KVModel(dict):
    class Config:  # (BaseModel.Config):
        deta_key: str = DETA_BASE_KEY if "DETA_BASE_KEY" in globals() else None
        deta = (
            Deta(DETA_BASE_KEY)
            if "Deta" in globals() and "DETA_BASE_KEY" in globals()
            else None
        )
        table_name: str = None

        # def __init__(self, *args, **kwargs):
        #    super(__class__, BaseModel).__init__(*args, **kwargs)
        #    self._set_table_name()
        #    self._set_db()

        # for name, field in cls.__fields__.items():
        #    setattr(cls, name, DetaField(field=field))

        pass

    @property
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

    # def __delitem__(self, name: str):
    #    print("__del__item__", name)
    #    pass

    def get(self, key: str, default=None):
        key = str(key)
        item = self._db.get(key)
        self.setdefault(key, default if item is None else item["value"])

        # return self[key]
        return super().get(key)

    def incr(self, key: str, quantity=1):
        key = str(key)
        try:
            item = self._db.put(
                {"key": key, "value": self._db.get(key)["value"] + quantity}
            )

        except TypeError as e:
            emessage = str(e)

            if emessage.find("subscriptable") > -1:
                # TypeError: 'NoneType' object is not subscriptable
                item = self._db.put({"key": key, "value": quantity})
            if (
                emessage.find("concatenate") > -1
                # TypeError: can only concatenate str (not "NoneType") to str
                or emessage.find("unsupported operand") > -1
                # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
                # or 1
                # smthng else
            ):
                raise ValueError()
                return
            # print(e)
            pass
        except Exception as e:  # NoneTyoe
            print("Unknown Exception", str(e))
            return

        self[key] = item["value"]
        return self[key]

    def decr(self, key: str, quantity=1):
        return self.incr(key, -quantity)

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
