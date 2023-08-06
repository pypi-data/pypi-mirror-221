import logging
import re
from json import loads, dumps
from typing import Optional, Union, Dict, List, Any, overload

try:  # TODO: Remove after Python 3.7
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from urllib.parse import urlparse, urljoin, quote

from httpx import HTTPStatusError, InvalidURL

from ipfabric.api import IPFabricAPI
from ipfabric.models import Technology, Inventory, Jobs, Intent, Devices
from ipfabric.tools import TIMEZONES

logger = logging.getLogger("ipfabric")

RE_PATH = re.compile(r"^/?(api/)?v\d(\.\d)?/")
RE_TABLE = re.compile(r"^tables/")
EXPORT_FORMAT = Literal["json", "csv"]


class IPFClient(IPFabricAPI):
    def __init__(
        self,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        snapshot_id: Optional[str] = None,
        auth: Optional[Any] = None,
        unloaded: bool = False,
        streaming: bool = False,
        **kwargs,
    ):
        """Initializes the IP Fabric Client

        Args:
            base_url: IP Fabric instance provided in 'base_url' parameter, or the 'IPF_URL' environment variable
            api_version: [Optional] Version of IP Fabric API
            auth: API token, tuple (username, password), or custom Auth to pass to httpx
            snapshot_id: IP Fabric snapshot ID to use by default for database actions - defaults to '$last'
            streaming: Stream table requests instead of paging results, see documentation for important information.
            **kwargs: Keyword args to pass to httpx
        """
        super().__init__(
            base_url=base_url,
            api_version=api_version,
            auth=auth,
            snapshot_id=snapshot_id,
            unloaded=unloaded,
            **kwargs,
        )
        self.streaming = streaming
        if self.streaming and self.os_version.split("+")[0] < "6.3.1":
            logger.warning(
                f"Setting `streaming=True` is not recommended until 6.3.1: "  # TODO: 6.3.1
                f"IP Fabric OS Version is {self.os_version}."
            )
        self.technology = Technology(client=self)
        self.jobs = Jobs(client=self)
        self._devices = list()

    @property
    def snapshot_id(self) -> str:
        """get snapshot Id"""
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        super(self.__class__, self.__class__).snapshot_id.fset(self, snapshot_id)
        self.intent = Intent(client=self)
        self.api_to_web = {intent.api_endpoint: intent.web_endpoint for intent in self.intent.intent_checks}
        self.inventory = Inventory(client=self)

    @property
    def devices(self) -> Devices:
        """get devices"""
        if not self._devices:
            logger.info("Devices not loaded, loading devices.")
            self._devices = self.load_devices()
        return self._devices

    @devices.setter
    def devices(self, devices):
        self._devices = devices

    def load_devices(self, device_filters: dict = None, device_attr_filters: dict = None):
        if self._no_loaded_snapshots:
            logger.warning("No loaded snapshots, cannot load devices.")
        else:
            if not device_attr_filters and self.attribute_filters:
                logger.warning(
                    f"Global `attribute_filters` is set; only pulling devices matching:\n{self.attribute_filters}."
                )
            try:
                self.devices = self.inventory.devices.all(
                    export="object", filters=device_filters, attr_filters=device_attr_filters
                )
                return self.devices
            except HTTPStatusError:
                logger.warning(self._api_insuf_rights + 'on POST "/tables/inventory/devices". Will not load Devices.')
        return list()

    @staticmethod
    def _check_url(url):
        path = urlparse(url).path
        r = RE_PATH.search(path)
        url = path[r.end():] if r else path  # fmt: skip
        url = url[1:] if url[0] == "/" else url
        return url

    def _check_url_payload(self, url, snapshot_id, filters, reports, sort, attr_filters, export, csv_tz):
        url = self._check_url(url)
        payload = dict()
        if self.api_version >= "v6.3":
            payload = {"format": {"dataType": "json"}}
        if filters and isinstance(filters, str):
            payload["filters"] = loads(filters)
        elif filters and isinstance(filters, dict):
            payload["filters"] = filters
        if snapshot_id:
            payload["snapshot"] = snapshot_id
        if sort:
            payload["sort"] = sort
        if RE_TABLE.match(url) and (attr_filters or self.attribute_filters):
            payload["attributeFilters"] = attr_filters or self.attribute_filters

        if export != "csv":
            # CSV does not return "reports" (intent checks)
            if isinstance(reports, (str, list)):
                payload["reports"] = reports
            elif reports is True and "/" + url in self.api_to_web:
                payload["reports"] = self.api_to_web["/" + url]
            elif reports is True and "/" + url not in self.api_to_web:
                logger.warning(
                    f"Could not automatically discover Web Endpoint for Intent Data for table '/{url}'.\n"
                    f"Table may not have any Intent Checks, please manually verify and enter to reports.\n"
                    f"Returning results without Intent Rules."
                )
        else:
            if self.api_version <= "v6.3":
                raise NotImplementedError(f"CSV export is implemented in v6.3.0; IPF version: {self.os_version}.")
            if reports:
                logger.warning("CSV export does not return reports, parameter has been excluded.")
            payload["format"] = {"exportToFile": True, "dataType": "csv"}
            if csv_tz and csv_tz.lower() not in TIMEZONES:
                raise ValueError(
                    f"CSV timezone '{csv_tz}' not in available timezones; see `ipfabric.tools.shared.TIMEZONES`"
                )
            elif csv_tz:
                payload["format"]["options"] = {"timezone": TIMEZONES[csv_tz.lower()]}
        return url, payload

    @overload
    def fetch(
        self,
        url,
        export: Literal["json"] = ...,
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        limit: Optional[int] = 1000,
        start: Optional[int] = 0,
        snapshot_id: Optional[str] = None,
        reports: Optional[Union[bool, list, str]] = False,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
    ) -> List[dict]:
        ...

    @overload
    def fetch(
        self,
        url,
        export: Literal["csv"],
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        limit: Optional[int] = 1000,
        start: Optional[int] = 0,
        snapshot_id: Optional[str] = None,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
        csv_tz: Optional[str] = None,
    ) -> bytes:
        ...

    def fetch(
        self,
        url,
        export: EXPORT_FORMAT = "json",
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        limit: Optional[int] = 1000,
        start: Optional[int] = 0,
        snapshot_id: Optional[str] = None,
        reports: Optional[Union[bool, list, str]] = False,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
        csv_tz: Optional[str] = None,
    ):
        """Gets data from IP Fabric for specified endpoint

        Args:
            url: Example tables/vlan/device-summary
            export: str: Export format to return [json, csv]; default is json.
            columns: Optional list of columns to return, None will return all
            filters: Optional dictionary of filters
            limit: Default to 1,000 rows
            start: Starts at 0
            snapshot_id: Optional snapshot_id to override default
            reports: String of frontend URL where the reports are displayed or a list of report IDs
            sort: Dictionary to apply sorting: {"order": "desc", "column": "lastChange"}
            attr_filters: Optional dictionary to apply an Attribute filter
            snapshot: Set to False for some tables like management endpoints.
            csv_tz: str: Default None, set a timezone to return human-readable dates when using CSV;
                         see `ipfabric.tools.shared.TIMEZONES`
        Returns:
            Union[List[dict], str]: List of dict if json, bytes string if CSV
        """
        snapshot_id = snapshot_id or self.snapshot_id if snapshot else None
        url, payload = self._check_url_payload(url, snapshot_id, filters, reports, sort, attr_filters, export, csv_tz)
        payload["columns"] = columns or self.get_columns(url, snapshot=snapshot)
        payload["pagination"] = dict(start=start, limit=limit)
        if export == "csv" or self.streaming:
            return self._stream(url, payload, export)
        else:
            res = self.post(url, json=payload)
            res.raise_for_status()
            return res.json()["data"]

    @overload
    def fetch_all(
        self,
        url: str,
        export: Literal["json"] = ...,
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        snapshot_id: Optional[str] = None,
        reports: Optional[Union[bool, list, str]] = False,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
    ) -> List[dict]:
        ...

    @overload
    def fetch_all(
        self,
        url: str,
        export: Literal["csv"],
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        snapshot_id: Optional[str] = None,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
        csv_tz: Optional[str] = None,
    ) -> bytes:
        ...

    def fetch_all(
        self,
        url: str,
        export: EXPORT_FORMAT = "json",
        columns: Optional[List] = None,
        filters: Optional[Union[dict, str]] = None,
        snapshot_id: Optional[str] = None,
        reports: Optional[Union[bool, list, str]] = False,
        sort: Optional[dict] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot: bool = True,
        csv_tz: Optional[str] = None,
    ):
        """Gets all data from IP Fabric for specified endpoint

        Args:
            url: Example tables/vlan/device-summary
            export: str: Export format to return [json, csv]; default is json.
            columns: Optional list of columns to return, None will return all
            filters: Optional dictionary of filters
            snapshot_id: Optional snapshot_id to override default
            reports: String of frontend URL where the reports are displayed or a list of report IDs
            sort: Optional dictionary to apply sorting: {"order": "desc", "column": "lastChange"}
            attr_filters: Optional dictionary to apply an Attribute filter
            snapshot: Set to False for some tables like management endpoints.
            csv_tz: str: Default None, set a timezone to return human-readable dates when using CSV;
                         see `ipfabric.tools.shared.TIMEZONES`
        Returns:
            Union[List[dict], str]: List of dict if json, bytes string if CSV
        """
        snapshot_id = snapshot_id or self.snapshot_id if snapshot else None
        url, payload = self._check_url_payload(url, snapshot_id, filters, reports, sort, attr_filters, export, csv_tz)
        payload["columns"] = columns or self.get_columns(url, snapshot=snapshot)
        if export == "csv" or self.streaming:
            return self._stream(url, payload, export)
        return self._ipf_pager(url, payload)

    def _reports_stream_bug(self, payload):
        """Bug NIM-11915"""
        if getattr(self, "intent", None) and "reports" in payload and isinstance(payload["reports"], str):
            reports = self.intent.intent_ids_by_web_endpoint[payload["reports"]]
            if not reports:
                logger.warning(
                    f"Could not find Intent Report IDs for web endpoint '{payload['reports']}' or none defined."
                )
                del payload["reports"]
            else:
                payload["reports"] = reports
        return payload

    def _get_payload(self, url, payload):
        snapshot_id = payload.pop("snapshot", None)
        p = "&".join([f"{k}={quote(dumps(v, separators=(',', ':')))}" for k, v in payload.items()])
        if snapshot_id:
            p += f"&snapshot={snapshot_id}"
        url = urljoin(str(self.base_url), url + f"?{p}")
        if len(url) > 4096:
            raise InvalidURL(f"URL exceeds max character limit of 4096: length={len(url)}.")
        return url

    def _stream(self, url, payload, export):
        if export != "csv":  # Bug NIM-11915
            payload = self._reports_stream_bug(payload)
        url = self._get_payload(url, payload)
        with self.stream("GET", url) as stream_resp:
            stream_resp.raise_for_status()
            data = stream_resp.read()
        return loads(data)["data"] if export in ["json"] else data

    def query(self, url: str, payload: Union[str, dict], get_all: bool = True) -> Union[List[dict], bytes]:
        """Submits a query, does no formatting on the parameters.  Use for copy/pasting from the webpage.

        Args:
            url: Example: https://demo1.ipfabric.io/api/v1/tables/vlan/device-summary or tables/vlan/device-summary
            payload: Dictionary to submit in POST or can be JSON string (i.e. read from file).
            get_all: Default use pager to get all results and ignore pagination information in the payload

        Returns:
            list or bytes: List of Dictionary objects or bytes if csv.
        """
        url = self._check_url(url)
        if isinstance(payload, str):
            payload = loads(payload)
        export = payload.get("format", {}).get("dataType", "json")
        if (export == "csv" or self.streaming) and get_all:
            return self._stream(url, payload, export)
        elif get_all:
            return self._ipf_pager(url, payload)
        else:
            res = self.post(url, json=payload)
            res.raise_for_status()
            return res.json()["data"]

    def _get_columns(self, url: str):  # TODO: Remove in v7
        logger.warning("""Use of _get_columns will be deprecated in a future release, please use get_columns""")
        return self.get_columns(url=url)

    def get_columns(self, url: str, snapshot: bool = True) -> List[str]:
        """Submits malformed payload and extracts column names from it

        Args:
            url: API url to post
            snapshot: Set to False for some tables like management endpoints.

        Returns:
            list: List of column names
        """
        snapshot_id = self.snapshot_id if snapshot else None
        url, payload = self._check_url_payload(url, snapshot_id, None, None, None, None, None, None)
        payload["columns"] = ["*"]
        r = self.post(url, json=payload)
        if r.status_code == 422:
            msg = r.json()["errors"][0]["message"]
            return [x.strip() for x in re.match(r"\".*\".*\[(.*)]$", msg).group(1).split(",")]
        else:
            r.raise_for_status()

    def get_count(
        self,
        url: str,
        filters: Optional[Union[dict, str]] = None,
        attr_filters: Optional[Dict[str, List[str]]] = None,
        snapshot_id: Optional[str] = None,
        snapshot: bool = True,
    ) -> int:
        """Get a total number of rows
        Args:
            url: API URL to post to
            filters: Optional dictionary of filters
            attr_filters: Optional dictionary of attribute filters
            snapshot_id: Optional snapshot_id to override default
            snapshot: Set to False for some tables like management endpoints.
        Returns:
            int: a count of rows
        """
        snapshot_id = snapshot_id or self.snapshot_id if snapshot else None
        url, payload = self._check_url_payload(url, snapshot_id, filters, None, None, attr_filters, None, None)
        payload.update({"columns": ["id"], "pagination": {"limit": 1, "start": 0}})
        res = self.post(url, json=payload)
        res.raise_for_status()
        return res.json()["_meta"]["count"]
