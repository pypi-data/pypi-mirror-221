#!/usr/bin/env python

import importlib
import signal
from functools import partial
from multiprocessing.connection import Listener
from pprint import pprint

import numpy as np

BASIC_TYPES = (int, float, str, bool, bytes, type(None))

OBJECT_PROXY = 1
ND_ARRAY = 2
PICKLED = 3


class ClientObjectMapper:
    def __init__(self):
        self.map_ = {}

    def register(self, data):
        id_ = id(data)
        if id_ not in self.map_:
            # print("REGISTER", hex(id_), data)
            self.map_[id_] = data
        return id_

    def get_registered(self, id_):
        try:
            return self.map_[id_]
        except KeyError:
            pprint({hex(id_): value for id_, value in self.map_.items()})
            raise

    def unwrap(self, data):
        try:
            type_, item = data
        except Exception:
            traceback.print_stack()
            raise
        if type_ is OBJECT_PROXY:
            return self.get_registered(item)

        if type_ is ND_ARRAY:
            bytes_, shape, dtype = item
            return np.ndarray(shape, dtype, bytes_)

        if isinstance(item, BASIC_TYPES):
            return item

        if isinstance(item, list):
            return [self.unwrap(ii) for ii in item]
        if isinstance(item, tuple):
            return tuple(self.unwrap(ii) for ii in item)
        if isinstance(item, set):
            return set(self.unwrap(ii) for ii in item)
        if isinstance(item, dict):
            return {self.unwrap(key): self.unwrap(value) for key, value in item.items()}

        if type_ == PICKLED:
            return item

        raise NotImplementedError(f"don't know how to unwrap {type(item)} {repr(item)}")

    def wrap(self, data):
        if isinstance(data, BASIC_TYPES):
            return 0, data

        if isinstance(data, list):
            return 0, [self.wrap(ii) for ii in data]
        if isinstance(data, tuple):
            return 0, tuple(self.wrap(ii) for ii in data)
        if isinstance(data, set):
            return 0, set(self.wrap(ii) for ii in data)
        if isinstance(data, dict):
            return 0, {self.wrap(key): self.wrap(value) for key, value in data.items()}

        if isinstance(data, np.ndarray):
            return ND_ARRAY, (data.tobytes(), data.shape, data.dtype.name)

        return OBJECT_PROXY, self.register(data)


optimizations = {}
oo = ClientObjectMapper()
map_, register, unwrap, wrap = oo.map_, oo.register, oo.unwrap, oo.wrap


def main(pipe):
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    commands = {
        "DELETE": delete_command,
        "SETITEM": setitem_command,
        "GETITEM": getitem_command,
        "GETATTR": getattr_command,
        "CALL": call_command,
        "ITER": iter_command,
        "NEXT": next_command,
        "DIR": dir_command,
        "INIT_OPTIMIZATIONS": init_optimizations_command,
    }

    KILLPILL = "KILLPILL"

    while True:
        try:
            command, args = pipe.recv()
        except EOFError:
            break
        if command == KILLPILL:
            break
        if command == "IMPORT":
            try:
                module = importlib.import_module(args)
                id_ = register(module)
            except ImportError:
                id_ = None
            pipe.send(id_)
            continue
        args = unwrap(args)
        commands[command](pipe, *args)


def init_optimizations_command(conn, path):
    global optimizations
    error = None
    try:
        module = {}
        exec(open(path).read(), module)
        optimizations.update(module["optimizations"])
    except Exception as e:
        error = e

    result = wrap(None)
    conn.send((error, result))


def delete_command(conn, id_):
    del map_[id_]


def call_command(conn, obj, args, kwargs):
    error = None
    result = None
    try:
        r = obj(*args, **kwargs)
        # handle pyopnms style "call by ref":
        result = (r, args)
    except Exception as e:
        error = e

    result = wrap(result)
    conn.send((error, result))


def getattr_command(conn, obj, name):
    key = f"{obj.__class__.__name__}.{name}"
    if key in optimizations:
        result = optimizations[key]
        if not key.startswith("module."):
            result = partial(result, obj)
        conn.send((None, wrap(result)))
        return

    error = None
    result = None
    try:
        result = getattr(obj, name)
    except Exception as e:
        error = e

    result = wrap(result)
    conn.send((error, result))


def dir_command(conn, obj):
    error = None
    result = None
    try:
        result = dir(obj)
    except Exception as e:
        error = e

    result = wrap(result)
    conn.send((error, result))


def setitem_command(conn, obj, key, value):
    _call(conn, obj, "__setitem__", key, value)


def getitem_command(conn, obj, key):
    _call(conn, obj, "__getitem__", key)


def iter_command(conn, obj):
    _call(conn, obj, "__iter__")


def next_command(conn, obj):
    _call(conn, obj, "__next__")


def _call(conn, obj, method, *args, **kwargs):
    error = None
    result = None
    try:
        result = getattr(obj, method)(*args, **kwargs)
    except Exception as e:
        error = e.__class__(
            f"calling {obj}.{method} with args {args} {kwargs} failed: {e}"
        )

    result = wrap(result)
    conn.send((error, result))
