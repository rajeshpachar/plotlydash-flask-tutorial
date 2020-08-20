import importlib
import pkgutil


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages
    :param recursive: bool
    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name

        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def get_modules(package):
    results = import_submodules(package, recursive=True)
    modules = {}
    for key, module in results.items():
        parts = key.split('.')
        filename = parts[len(parts)-1]
        if filename in ['callbacks', 'layout', 'index_html']:
            path = "/".join(parts[1:len(parts)-1])
            modules[path] = modules.get(path) or {}
            modules[path][filename] = module

    return modules