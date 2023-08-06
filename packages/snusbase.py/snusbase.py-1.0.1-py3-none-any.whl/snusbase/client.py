import aiohttp
import orjson
from typing import List, Dict, Union
from pydantic import BaseModel
from .errors import NoResponse


class SearchResult(BaseModel):
    """A class representing a search result."""

    username: str
    email: str
    name: str
    created: str
    followers: str
    hash: str
    uid: str
    regdate: str
    lastip: str
    id: str
    date: str
    salt: str


class SearchResults(BaseModel):
    """A class representing a collection of search results."""

    results: Dict[str, List[SearchResult]]


class SnusbaseAPI:
    """A class for interacting with the Snusbase API."""

    def __init__(self, api_key: str):
        """
        Initialize the SnusbaseAPI instance.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.base_url = 'https://api-experimental.snusbase.com'
        self.headers = {
            'Auth': self.api_key,
            'Content-Type': 'application/json',
        }

    async def _request(
        self, method: str, endpoint: str, params=None, data=None
    ) -> Dict[str, Union[str, List[SearchResult]]]:
        """
        Send a request to the Snusbase API.

        Args:
            method (str): The HTTP method for the request (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to access.
            params (dict, optional): Query parameters for the request.
            data (dict, optional): JSON data for the request payload.

        Returns:
            dict: The response data as a dictionary.

        Raises:
            aiohttp.ClientError: If there is an error in the request.
        """
        url = f'{self.base_url}{endpoint}'
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, url, headers=self.headers, params=params, json=data
            ) as response:
                if not response:
                    raise NoResponse(
                        "The API didn't return anything or got no response."
                    )
                return await response.json(loads=orjson.loads)

    async def search(self, term: str, search_type: str) -> SearchResults:
        """
        Search Snusbase for data related to a term.

        Args:
            term (str): The term to search for.
            search_type (str): The type of search to perform (e.g., 'username', 'password').

        Returns:
            SearchResults: The response data containing the search results.
        """
        endpoint = '/data/search'
        data = {'terms': [term], 'types': [search_type]}
        return SearchResults(
            results=await self._request('POST', endpoint, data=data)
        )

    async def hash_lookup(self, _hash: str) -> SearchResults:
        """
        Lookup a hash in the Snusbase database.

        Args:
            hash (str): The hash to lookup.

        Returns:
            SearchResults: The response data containing the hash lookup results.
        """
        endpoint = '/tools/hash-lookup'
        data = {
            'terms': [_hash],
            'types': ['hash'],
        }
        return SearchResults(
            results=await self._request('POST', endpoint, data=data)
        )

    async def ip_lookup(self, ip: str) -> SearchResults:
        """
        Lookup an IP address in the Snusbase database.

        Args:
            ip (str): The IP address to lookup.

        Returns:
            SearchResults: The response data containing the IP address lookup results.
        """
        endpoint = '/tools/ip-whois'
        data = {
            'terms': [ip],
        }
        return SearchResults(
            results=await self._request('POST', endpoint, data=data)
        )

    async def search_by_username(self, username: str) -> SearchResults:
        """
        Search Snusbase for data related to a username.

        Args:
            username (str): The username to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(username, 'username')

    async def search_by_password(self, password: str) -> SearchResults:
        """
        Search Snusbase for data related to a password.

        Args:
            password (str): The password to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(password, 'password')

    async def search_by_email(self, email: str) -> SearchResults:
        """
        Search Snusbase for data related to an email address.

        Args:
            email (str): The email address to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(email, 'email')

    async def search_by_ip(self, ip: str) -> SearchResults:
        """
        Search Snusbase for data related to an IP address.

        Args:
            ip (str): The IP address to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(ip, 'lastip')

    async def search_by_name(self, name: str) -> SearchResults:
        """
        Search Snusbase for data related to a name.

        Args:
            name (str): The name to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(name, 'name')

    async def search_by_hash(self, _hash: str) -> SearchResults:
        """
        Search Snusbase for data related to a hash.

        Args:
            hash (str): The hash to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(_hash, 'hash')

    async def search_by_wildcard(self, wildcard: str) -> SearchResults:
        """
        Search Snusbase for data related to a wildcard.

        Args:
            wildcard (str): The wildcard to search for.

        Returns:
            SearchResults: The response data containing the search results.
        """
        return await self.search(wildcard, 'wildcard')
