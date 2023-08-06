<h1></h1>
Gets all links from a given Google Space and stores them in a text file.
<hr>
<h1>Usage</h1>
To install the package, run 

```
pip install atk-training-rin-chatlink
```

The command can be used by running the following in a terminal.
```
atk-training-rin-chatlink path/to/config.yaml
```

Ensure your config.yaml has the following fields:
```yaml
space: name of space to get links from
save_to: folder/to/save/url.txt/to/
```

If downloaded from GitHub, add your ```client_secrets.json``` file from <a href="https://console.cloud.google.com/">Google Cloud Console</a> to ```atk_training_rin_chatlink```. Make sure it has the following scopes enabled:<br>
<ul>
<li>.../auth/chat.spaces.readonly</li>
<li>.../auth/chat.messages.readonly</li>
</ul>