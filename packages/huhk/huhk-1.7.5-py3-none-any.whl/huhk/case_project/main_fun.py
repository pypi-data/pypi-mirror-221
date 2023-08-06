from case_project.version import version as _version
from init_project import GetApi


def get_version():
    k = str(GetApi.get_main_key())
    v = str(GetApi.get_main_name())
    print(k)
    print(v)
    out_str = f"版本：{_version}\n--key：{k}\n--name：{v}"
    return out_str
