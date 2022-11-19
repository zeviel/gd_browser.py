# gd_browser.py
Web-API for [gdbrowser.com](https://gdbrowser.com) website that lets you browse all of Geometry Dash's online features

## Example
```python3
import gd_browser
gd_browser = gd_browser.GDBrowser()
user_info = gd_browser.get_user_profile(username="")
print(user_info)
```
