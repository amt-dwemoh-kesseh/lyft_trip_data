from typing import Any, Callable, List, Tuple, Union

def get_func_args(func: Callable[..., Any]) -> List[str]: ...
def get_func_full_args(func: Callable[..., Any]) -> List[Union[Tuple[str, str], Tuple[str]]]: ...
def func_accepts_kwargs(func: Callable[..., Any]) -> bool: ...
def func_accepts_var_args(func: Callable[..., Any]) -> bool: ...
def method_has_no_args(meth: Callable[..., Any]) -> bool: ...
def func_supports_parameter(func: Callable[..., Any], name: str) -> bool: ...
