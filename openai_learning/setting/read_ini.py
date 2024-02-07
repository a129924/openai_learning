from configparser import ConfigParser

__all__ = ["read_config_ini"]


def read_config_ini(
    ini_path: str = r"./openai_learning/setting/setting.ini", encoding: str = "UTF-8"
) -> ConfigParser:
    """
    read_config_ini 讀取ini file

    Args:
        ini_path (str, optional): ini file路徑. Defaults to r"./openai_learning/setting/setting.ini".
        encoding (str, optional): 編碼 Defaults to "UTF-8".

    Returns:
        ConfigParser: 回傳ConfigParser
    """
    from os.path import exists

    assert exists(ini_path), FileExistsError(f"{ini_path} is not exists")
    config = ConfigParser()

    config.read(filenames=ini_path, encoding=encoding)

    return config


if __name__ == "__main__":
    print(read_config_ini()["OPENAPI_SETTING"]["api_key"])
