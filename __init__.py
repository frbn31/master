from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

routers = []

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    new_routers = getattr(module, "routers", None)
    if new_routers:
        routers = routers + new_routers
globals()["routers"] = routers


models = []

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    new_models = getattr(module, "models", None)
    if new_models:
        models = models + new_models
globals()["models"] = models

