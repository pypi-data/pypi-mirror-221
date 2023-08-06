from .__session__ import SessionManager

from base64       import b64encode
from json         import dumps
from tls_client   import Session
from typing       import Optional, Literal, List, Union
from json         import dumps, loads
from time         import sleep, time
from httpx        import get
from re           import search
from asyncio      import run



class HTTPClient:
    def __init__(self):
        self.session = Session(client_identifier="firefox_113", random_tls_extension_order=True)


class Globals:
    session_id = None
    sessionThread = None
    sessionOn = True


class VeilCord:
    def __init__(
        self, 
        session:        Optional[Session] = HTTPClient().session,
        device_type:    Literal["browser", "mobile", "app"] = "browser", 
        user_agent:     Optional[str] = None,
        device_version: Optional[str] = None
    ) -> None:
        self.session = HTTPClient().session if session is None else session
        self.user_agent_browser = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
        self.user_agent_mobile  = "Discord-Android/170014;RNA"
        self.user_agent_app     = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36"
        self.device_type_browser = "Windows"
        self.device_type_mobile  = "Android"
        self.currentBuildNUM = 199933
        if user_agent and not device_version:
            raise SyntaxError("If using custom useragent you must provide the version. Such as: 113.0")
        if device_type == "browser":
            self.device_type = "browser"
            self.user_agent = self.user_agent_browser if user_agent is None else user_agent
        elif device_type == "mobile":
            self.device_type = "mobile"
            self.user_agent = self.user_agent_mobile if user_agent is None else user_agent
        elif device_type == "app":
            self.device_type = "app"
            self.user_agent = self.user_agent_app if user_agent is None else user_agent
        else:
            raise ValueError("An invalid device_type was provided. Acceptable values: ['browser', 'mobile', 'app']")
        
    
    def generateXProp(
        self,
        browser_name: Optional[str] = None, 
        browser_vers: Optional[str] = None,
        build_num:    Optional[int] = None
    ):
        if self.device_type == "mobile":
            xsup = {
                "os": self.device_type_mobile,
                "browser": "Discord Android",
                "device": "RMX2117L1",
                "system_locale": "en-US",
                "client_version": "177.21 - rn",
                "release_channel": "googleRelease",
                "device_vendor_id": "c3c29b3e-4e06-48ff-af49-ec05c504c63e",
                "os_version": "31",
                "client_build_number": 1750160087099,
            }
        elif self.device_type == "browser":
            xsup = {
                "os": self.device_type_browser,
                "browser": browser_name if browser_name else "Firefox",
                "system_locale": "en-US",
                "browser_user_agent": self.user_agent,
                "browser_version": browser_vers if browser_vers else "113.0.0.0",
                "os_version": "10",
                "release_channel": "stable",
                "client_build_number": build_num if build_num else self.currentBuildNUM,
            }
        elif self.device_type == "app":
            xsup = {
                "os": self.device_type_browser,
                "browser": "Discord Client",
                "release_channel": "stable",
                "client_version": browser_vers if browser_vers else "1.0.9013",
                "os_version": "10.0.22621",
                "os_arch": "x64",
                "system_locale": "en-US",
                "browser_user_agent": self.user_agent_app,
                "browser_version": "22.3.2",
                "client_build_number": build_num if build_num else self.currentBuildNUM,
                "native_build_number": 32266,
            }
        else:
            raise ValueError("An invalid type for generateXProp() was provided. Acceptable values: ['browser', 'mobile', 'app']")
        
        xsup["client_event_source"] = None
        xsup["design_id"] = 0
        xsup["referrer"] = ""
        xsup["referring_domain"] = ""
        xsup["referrer_current"] = ""
        xsup["referring_domain_current"] = ""
        
        return b64encode(dumps(xsup, separators=(',', ':')).encode()).decode()


    def getFingerprint(
        self,
        xsup: Optional[str] = None,
        withCookies: Optional[bool] = True,
        cookieType: Literal["json", "cookiejar"] = "cookiejar"
    ) -> Union[str, List[str]]:
        if not xsup:
            xsup = self.generateXProp()
        if self.device_type == "mobile":
            headers = {
                'Host': 'discord.com',
                'X-Super-Properties': xsup,
                'Accept-Language': 'en-US',
                'X-Discord-Locale': 'en-US',
                'X-Debug-Options': 'bugReporterEnabled',
                'User-Agent': self.user_agent,
                'Content-Type': 'application/json',
            }
        elif self.device_type == "browser":
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.5",
                "connection": "keep-alive",
                "host": "discord.com",
                "referer": "https://discord.com/register",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": self.user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": xsup
            }
        elif self.device_type == "app":
            headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US",
                "connection": "keep-alive",
                "content-type": "application/json",
                "origin": "https://discord.com",
                "referer": "https://discord.com/",
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                "user-agent": self.user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-discord-timezone": "America/New_York",
                "x-super-properties": xsup,
            }
        else: raise ValueError("An invalid type for getFingerprint() was provided. Acceptable values: ['browser', 'mobile', 'app']")
        response = self.session.get('https://discord.com/api/v9/experiments', headers=headers)
        if withCookies:
            cookies = response.cookies if cookieType == "cookiejar" else dumps(response.cookies.get_dict())
            return response.json().get("fingerprint"), cookies
        return response.json().get("fingerprint")


    
    # non self #
    
    def getBuildNum():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Alt-Used': 'discord.com',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'trailers',
        }
        html = get(f"https://discord.com/app?_={(time() * 1000)}", headers=headers).text

        last_index = html.rfind('/assets/')
        closing_quote_index = html.find('"', last_index)
        prefetched_script = html[last_index:closing_quote_index]

        response = get(f'https://discord.com{prefetched_script}', headers=headers).text

        buildnum = response.split("buildNumber:\"")[1].split("\"")[0]
        
        return buildnum
    
    
    def extractCode(invite):
        """Extracts the invite code from a Discord invite link"""
        code_regex = r"(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)"
        match = search(code_regex, invite)
        if match:
            try:
                return match.group(1)
            except:
                return match.group(0)
        else:
            return None
        
        
        
    def openSession(self):
        session_manager = SessionManager(self.user_agent, self.currentBuildNUM, self.device_type)
        return session_manager
        
    def getSession(
        self, 
        session, 
        token: str, 
        keep_alive: bool = False, 
        show_hb: bool = False
    ) -> Union[str, None]:
        if session is None:
            session = SessionManager(self.user_agent, self.currentBuildNUM, self.device_type)
            if keep_alive:
                raise SyntaxError("Session cannot be null with keepAlive enabled.")
        session_id = run(session.get_session(token, keep_alive, show_hb))
        return session_id

    def closeSession(self, session):
        session.close_session()
        return True
    
    

      
        
        
        
        
## out of the class for old projects use

def extractCode(invite):
    """Extracts the invite code from a Discord invite link"""
    code_regex = r"(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)"
    match = search(code_regex, invite)
    if match:
        try:
            return match.group(1)
        except:
            return match.group(0)
    else:
        return None