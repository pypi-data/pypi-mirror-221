from huhk.case_project.version import version as _version
from huhk.init_project import GetApi


def get_version():
    k = str(GetApi.get_main_key())
    v = str(GetApi.get_main_name())
    out_str = f"版本：{_version}\n--key：{k}\n--name：{v}"
    return out_str


def set_key_name(key, name):
    if key and name:
        GetApi.set_main_key(key)
        GetApi.set_main_name(name)
    elif key or name:
        key_list = GetApi.get_key_name_list()
    return True