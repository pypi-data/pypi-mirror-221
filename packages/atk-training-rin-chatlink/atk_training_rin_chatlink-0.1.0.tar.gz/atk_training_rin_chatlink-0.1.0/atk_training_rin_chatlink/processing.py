import re
import yaml


def extract_url(msg_list: list):
    urls = []
    for message in msg_list:
        urls.extend(re.findall(r'https?://\S+', message))
    return urls


def get_target(config_path: str, target: str = "space"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file.read())
    return config.get(target)
