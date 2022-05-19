from typing import Optional, Any, Callable


def object_property(obj: object, property_name: str) -> Optional[Any]:
    return obj.__dict__.get(property_name)


def value_exists(prop) -> bool:
    return False if prop is None else True


def property_matches_condition(prop, predicate: Callable[[Any], bool]) -> bool:
    if value_exists(prop) is False:
        return False
    else:
        return predicate(prop)


def gt(x, val):
    return x > val


def eq(x, val):
    return x == val


def lt(x, val):
    return x < val
