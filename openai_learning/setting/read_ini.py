from configparser import ConfigParser

__all__ = ["read_config_ini"]

def read_config_ini(
    ini_path: str = r"./openai_learning/setting/setting.ini", encoding: str = "UTF-8"
) -> ConfigParser:
    from os.path import exists
    
    assert exists(ini_path), FileExistsError(f"{ini_path} is not exists")
    config = ConfigParser()
    
    config.read(filenames=ini_path, encoding=encoding)
    return config


if __name__ == "__main__":
    print(read_config_ini()["OPENAPI_SETTING"]["api_key"])
