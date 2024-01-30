from configparser import ConfigParser

__all__ = ["read_config_ini"]

def read_config_ini(
    ini_path: str = r"./setting.ini", encoding: str = "UTF-8"
) -> ConfigParser:
    config = ConfigParser()

    config.read(filenames=ini_path, encoding=encoding)
    return config


if __name__ == "__main__":
    print(read_config_ini()["OPENAPI_SETTING"]["api_key"])
