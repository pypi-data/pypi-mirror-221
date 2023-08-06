import requests  # assuming you're using the requests library to make HTTP requests
from typing import Dict, Any
import promptlabs.chain as Chain
from promptlabs.pipeline import Pipeline


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint_url = "https://pops.up.railway.app/api/package"


    def _fetch(self, url):
        try:
            response = requests.get(
                self.endpoint_url + url,
                headers={"Authorization": "Bearer " + self.api_key},
            )
        except Exception as exc:
            raise Exception("Could not fetch data from API") from exc

        if response.status_code != 200:
            raise Exception("Could not fetch data from API")
    
        return response
    
    def chain(self, chain_name) -> Chain:
        data = self._fetch(
            f"/chain/{chain_name}",
        ).json()
        
        print(data)
        
        try:
            chain_class = getattr(Chain, data['type'])
            print(chain_class)
            return chain_class(config=data)
        except Exception as e:
            print(e)
            raise ValueError(f"Invalid chain type: {data['type']}")
        
    def chain_init_data(self, chain_name) -> Dict[str, Any]:
        data = self._fetch(
            f"/chain/{chain_name}",
        ).json()
        
        return data
        
    def pipeline(self, pipeline_name) -> Pipeline:
        data = self._fetch(
            f"/pipeline/{pipeline_name}",
        ).json()
        
        # get the chain configs
        chains_data = self._fetch(
            f"/pipeline_chains/{pipeline_name}"
        ).json()
        
        data['chain_configs'] = chains_data
        
        return Pipeline(config=data)
    
    def pipeline_init_data(self, pipeline_name) -> Dict[str, Any]:
        data = self._fetch(
            f"/pipeline/{pipeline_name}",
        ).json()
        
        # get the chain configs
        chains_data = self._fetch(
            f"/pipeline_chains/{pipeline_name}"
        ).json()
        
        data['chain_configs'] = chains_data
        return data

def create_client(api_key):
    return Client(api_key)
