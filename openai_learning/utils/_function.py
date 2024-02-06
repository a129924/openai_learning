__all__ = ["set_env"]

def set_env(key:str, value:str):
    from os import environ
    
    environ[key] = value