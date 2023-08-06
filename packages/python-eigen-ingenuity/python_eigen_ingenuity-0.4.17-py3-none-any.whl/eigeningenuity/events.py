import requests,json

from eigeningenuity.core import get_default_server, EigenServer
from eigeningenuity.util import get_eigenserver, divide_chunks, parseEvents, urlquote, _do_eigen_json_request, force_list

from typing import Union

class EventLog (object):
    """An elasticsearch instance which talks the Eigen elastic endpoint.
    """
    def __init__(self, baseurl):
        """This is a constructor. It takes in a URL like http://infra:8080/ei-applet/search/"""
        self.baseurl = baseurl
        self.eigenserver = get_eigenserver(baseurl)

    def _testConnection(self):
        """Preflight Request to verify connection to ingenuity"""
        try:
            status = requests.get(self.baseurl, verify=False).status_code
        except (ConnectionError):
            raise ConnectionError ("Failed to connect to ingenuity instance at " + self.eigenserver + ". Please check the url is correct and the instance is up.")
        

    def pushToEventlog(self, events):
        """
        Push one or more events to the ingenuity eventlog, accepts any event structure

        Args:
            events: A single event as dict, many events as a list of dicts, or the string filepath of a file containing events

        Returns:
            A boolean representing the successful push of all events. False if at least one event failed to be created
        """
        events = parseEvents(events)
        url = self.baseurl + "events/save-multiple"
        event_chunks = list(divide_chunks(events, 500))
        success = []
        for chunk in event_chunks:
            data = {"events": chunk}
            resp = requests.post(url, json=data, verify=False)
            success.append(resp)

        return success

    def pushTo365(self, events:Union[dict,list,str]) -> bool:
        """
        Push one or more events to the office 365 connector, only accepts pre-defined event structures

        Args:
            events: Can only accept event structures that have been pre-defined in ingenuity. A single event as dict, many events as a list of dicts, or the string filepath of a file containing events

        Returns:
            A boolean representing the successful push of all events. False if at least one event failed to be created
        """
        events = parseEvents(events)
        url = self.baseurl + "eventbus/publish-multiple"
        event_chunks = list(divide_chunks(events, 500))
        success = []
        for chunk in event_chunks:
            data = {"events": chunk}
            success.append(requests.post(url, json=data, verify=False))
        return all(success)
    

class EventScanner (object):
    """An elasticsearch instance which talks the Eigen elastic endpoint.
    """
    def __init__(self, baseurl):
        """This is a constructor. It takes in a URL like http://infra:8080/ei-applet/search/"""
        self.baseurl = baseurl
        self.eigenserver = get_eigenserver(baseurl)

    def _testConnection(self):
        """Preflight Request to verify connection to ingenuity"""
        try:
            status = requests.get(self.baseurl, verify=False).status_code
        except (ConnectionError):
            raise ConnectionError ("Failed to connect to ingenuity instance at " + self.eigenserver + ". Please check the url is correct and the instance is up.")

    def createUserLimit(self, name, tag, threshold_type, threshold, recovery, notify=False, emails="", mobiles=""):
        if emails != "":
            emails = force_list(emails)
            for email in emails:
                email = "email/" + email
            emails = ", ".join(emails)

        if mobiles != "":
            mobiles = force_list(mobiles)
            for mobile in mobiles:
                mobile = "mobile/" + mobile
            mobiles = ", ".join(mobiles)

        if mobiles != "" and emails != "":
            notifyees = emails + ", " + mobiles
        elif emails != "":
            notifyees = email
        else: 
            notifyees = mobiles

        if notify:
            notify = "ONCHANGE"
        else:
            notify = "NEVER"
        args = {}

        name = name.replace("-","")

        # x = json.dumps({"id": {tag + "-" + name}, "event": { "datatag": tag, "thresholdtype": threshold_type,"recoverythreshold": recovery,"type": "co.eigen.eventscanner.util.DataTagThresholdCheck", "threshold": threshold,"notifyrule": notify, "notifyees": emails + ", " + mobiles}})
        # cmd = "?repository=eventcheckrepository"
        url = self.baseurl + "eventcheckrepo/WRITECHECK?repository=eventcheckrepository"
        # args["repository"] = "eventcheckrepository"
        args["checkid"] = tag + "-" + name
        args["checkdef"] = json.dumps({"id": tag + "-" + name, "event": { "datatag": tag, "thresholdtype": threshold_type,"recoverythreshold": recovery,"type": "co.eigen.eventscanner.util.DataTagThresholdCheck", "threshold": threshold,"notifyrule": notify, "notifyees": notifyees}})
        for arg in args:
            url += f'&{arg}={args[arg]}'
        success = (requests.get(url, verify=False))
        return success
    
    def batchCreateUserLimits(self, limits):
        successes = []
        limits = force_list(limits)
        for limit in limits:
            successes.append(self.createUserLimit(
                limit["name"],
                limit["tag"],
                limit["type"],
                limit["threshold"],
                limit.get("recovery", ""),
                limit.get("emails", ""),
                limit.get("mobiles", "")
            ))
        return successes
    
    def deleteUserLimit(self,tag,name):
        url = self.baseurl + "eventcheckrepo/REMOVECHECK?repository=eventcheckrepository"
        # args["repository"] = "eventcheckrepository"
        checkID = [tag + "-" + name, tag + "-" + name.replace("-","")]
        for id in checkID:
            checkUrl = url + f"&checkid={id}"
            success = requests.get(checkUrl, verify=False)
        return success
    
    def batchDeleteUserLimits(self, limits):
        successes = []
        limits = force_list(limits)
        for limit in limits:
            self.deleteUserLimit(limit["tag"],limit["name"])
        return successes
    
    def deleteMatchingLimits(self, filter):
        limits = self.listUserLimits(filter)
        limits = force_list(limits)
        self.batchDeleteUserLimits(limits)
        return limits
    
    def listUserLimits(self,filter="**"):
        url = self.baseurl + "eventcheckrepo/LISTCHECKS?repository=eventcheckrepository"
        # args["repository"] = "eventcheckrepository"
        if "*" not in filter:
            filter = f"*{filter}*"
        url += f"&filter={filter}"
        limits = requests.get(url, verify=False).json()
        return limits


def get_eventlog(eigenserver:EigenServer=None):
    """
    Connect to Eventlog of eigenserver. If eigenserver is not provided this will default to the EIGENSERVER environmental variable

    Args:
        eigenserver: An instance of EigenServer() to query

    Returns:
        An object defining a connection to the Eventlog
    """
    if eigenserver is None:
            eigenserver = get_default_server()

    return EventLog(eigenserver.getEigenServerUrl() + "eventlog-servlet" + "/")

def get_eventscanner(eigenserver:EigenServer=None):
    """
    Connect to Eventscanner of eigenserver. If eigenserver is not provided this will default to the EIGENSERVER environmental variable

    Args:
        eigenserver: An instance of EigenServer() to query

    Returns:
        An object defining a connection to the Eventscanner
    """
    if eigenserver is None:
            eigenserver = get_default_server()

    return EventScanner(eigenserver.getEigenServerUrl() + "eventscanner-servlet" + "/")
