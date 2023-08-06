# VeilCord.
<img src="https://img.shields.io/pypi/v/veilcord?style=for-the-badge&logo=python">
<img alt="followers" src="https://img.shields.io/github/followers/imvast?color=f429ff&style=for-the-badge&logo=github&label=Follow"/>

```less
              > Custom Discord Tools Going To Be Used For My Projects
                    And Available To Anyone Else Who Wants To Use <
```

---

### Installation
```yaml
! package NOT FULLY available for non-personal use !
```

### Example Usage
```py
from veilcord import VeilCord

veilcord = VeilCord(
    session = None, # for custom tls_client sessions
    device_type = "browser", # types : browser, mobile, app
    user_agent = None # for custom user agent
)

# GETTING X-Super-Properties
xsup = veilcord.generateXProp()
print(f"(+) Retrieved XSup: {xsup}")


# GETTING ALL THE COOKIES AND FINGERPRINT
fp, cookies = veilcord.getFingerprint(xsup, cookieType="json")
print(f"(+) Retrieved Fingerprint: {fp}")
print(f"(+) Retrieved Cookies: {cookies}")
# returns a set.  [0] - Fingerprint  |  [1] - COOKIESJAR or JSON


# GET THE NEW SESSION ID BS
session = veilcord.openSession()

token = ""
sessionID = veilcord.getSession(
    session = session, # the session returned from veilcord.openSession()
    token = token, # obv the token
    keep_alive = False,  # keep the session alive | only needed if ur code is slow (avg. session is live for ~40 seconds.)
    show_hb = False # prints when it sends the heartbeat and when the next one is
)
print(f"(+) Got Session ID: {sessionID}")

# close the session, if keepAlive is enabled.
# veilcord.closeSession(session)

```

---

## * [imvast@discord](https://discord.com/users/1118654675898617891) | [imvast@github](https://github.com/imvast) | [vast.sh](https://vast.sh) *