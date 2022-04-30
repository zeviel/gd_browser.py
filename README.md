# gdbrowser.py
Web-API for [gdbrowser.com](https://gdbrowser.com) website that lets you browse all of Geometry Dash's online features

## Example
```python3
import gdbrowser
gdBrowser = gdbrowser.GDBrowser()
user_info = gdBrowser.get_user_profile(username="")
print(f"-- User accountID is::: {user_info['accountID']")
```
