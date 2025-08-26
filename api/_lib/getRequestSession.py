import requests
from bs4 import BeautifulSoup
import lxml

def getRequestSession(username, password):
    requestSession = requests.session()

    loginScreenResponse = requestSession.get("https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%3fSiteCode%3dumtlive&SiteCode=umtlive").text

    parser =  BeautifulSoup(loginScreenResponse, "lxml")

    requestVerificationToken = parser.find('input', attrs={'name': '__RequestVerificationToken'})["value"]

    requestHeaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'esp41pehac.eschoolplus.powerschool.com',
        'Origin': 'esp41pehac.eschoolplus.powerschool.com',
        'Referer': "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%3fSiteCode%3dumtlive&SiteCode=umtlive",
        '__RequestVerificationToken': requestVerificationToken
    }

    requestPayload = {
        "__RequestVerificationToken" : requestVerificationToken,
        "SCKTY00328510CustomEnabled" : "False",
        "SCKTY00436568CustomEnabled" : "False",
        "Database" : "10",
        "VerificationOption" : "UsernamePassword",
        "LogOnDetails.UserName": username,
        "tempUN" : "",
        "tempPW" : "",
        "LogOnDetails.Password" : password
    }

    pageDOM = requestSession.post(
        "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%3fSiteCode%3dumtlive&SiteCode=umtlive",
        data=requestPayload,
        headers=requestHeaders
    )

    return requestSession

