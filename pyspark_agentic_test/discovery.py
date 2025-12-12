import inspect
import importlib

def discover_functions(module_name):
    module = importlib.import_module(module_name)
    funcs = []
    for name, fn in inspect.getmembers(module):
        if inspect.isfunction(fn):
            sig = inspect.signature(fn)
            if sig.parameters:
                first = next(iter(sig.parameters.values()))
                if first.name in ["df", "dataframe"]:
                    funcs.append(fn)
    return funcs
