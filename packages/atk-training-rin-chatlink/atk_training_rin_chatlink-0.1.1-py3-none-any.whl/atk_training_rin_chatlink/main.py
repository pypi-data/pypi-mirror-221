from typer import Typer

from atk_training_rin_chatlink.auth_commands import ChatApp
from atk_training_rin_chatlink.processing import get_target, extract_url

app = Typer()


@app.command()
def save_url_to_file(path: str):
    sp_name = get_target(path, "space")
    chat = ChatApp(sp_name)
    messages = chat.get_messages()

    urls = extract_url(messages)
    write_url = [url + "\n" for url in urls]

    write_path = get_target(path, "save_to")
    with open(write_path+"urls.txt", "w") as file:
        file.writelines(write_url)
    print("file created")
