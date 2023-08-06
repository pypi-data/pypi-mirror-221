import json
from typing import Dict, Union

import marketplace_standard_app_api.models.object_storage as object_storage
from fastapi import UploadFile

from ..utils import check_capability_availability
from .base import _MarketPlaceAppBase
from .utils import _decode_metadata, _encode_metadata


class MarketPlaceObjectStorageApp(_MarketPlaceAppBase):
    @check_capability_availability
    def list_collections(
        self, limit: int = 100, offset: int = 0
    ) -> object_storage.CollectionResponseModel:
        response = self._client.get(
            self._proxy_path("listCollections"),
            params={"limit": limit, "offset": offset},
        )
        try:
            return object_storage.CollectionResponseModel.parse_obj(
                response.json()
            ).dict()
        except Exception:
            return "Error: Server returned {} while fetching collections: {}".format(
                response.status_code, response.text
            )

    @check_capability_availability
    def list_datasets(
        self,
        collection_name: object_storage.CollectionName,
        limit: int = 100,
        offset: int = 0,
    ) -> object_storage.DatasetResponseModel:
        response = self._client.get(
            self._proxy_path("listDatasets"),
            params={
                "collection_name": collection_name,
                "limit": limit,
                "offset": offset,
            },
        )
        try:
            return object_storage.DatasetResponseModel.parse_obj(response.json()).dict()
        except Exception:
            return "Error: Server returned {} while fetching datasets: {}".format(
                response.status_code, response.text
            )

    @check_capability_availability
    def create_or_update_collection(
        self,
        metadata: dict = None,
        collection_name: object_storage.CollectionName = None,
    ) -> str:
        return self._client.put(
            self._proxy_path("createOrUpdateCollection"),
            params={"collection_name": collection_name} if collection_name else {},
            headers=_encode_metadata(metadata) if metadata else {},
        ).text

    @check_capability_availability
    def delete_collection(self, collection_name: object_storage.CollectionName):
        return self._client.delete(
            self._proxy_path("deleteCollection"),
            params={"collection_name": collection_name},
        ).text

    # NOTE: change to GET for the meeting if proxy doesn't support HEAD requests
    @check_capability_availability
    def get_collection_metadata(
        self, collection_name: object_storage.CollectionName
    ) -> Union[Dict, str]:
        response_headers: dict = self._client.head(
            self._proxy_path("getCollectionMetadata"),
            params={"collection_name": collection_name},
        ).headers
        return json.dumps(_decode_metadata(headers=response_headers))

    @check_capability_availability
    def create_collection(
        self,
        collection_name: object_storage.CollectionName = None,
        metadata: dict = None,
        config: dict = None,
    ) -> object_storage.CollectionCreateResponse:
        data = {"collection_name": collection_name} if collection_name else {}
        if config is not None:
            data.update(config)
        response = self._client.put(
            self._proxy_path("createCollection"),
            data=data,
            headers=_encode_metadata(metadata) if metadata else {},
        )
        try:
            return object_storage.CollectionCreateResponse.parse_obj(
                response.json()
            ).dict()
        except Exception:
            return "Error: Server returned {} while creating collection {}: {}".format(
                response.status_code, collection_name, response.text
            )

    @check_capability_availability
    def create_dataset(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName = None,
        metadata: dict = None,
        file: UploadFile = None,
        config: dict = None,
    ) -> object_storage.DatasetCreateResponse:
        params = {"collection_name": collection_name}
        data = {}
        if dataset_name:
            data.update({"dataset_name": dataset_name})
        if config is not None:
            data.update(config)
        response = self._client.put(
            self._proxy_path("createDataset"),
            data=data,
            params=params,
            files=file,
            headers=_encode_metadata(metadata) if metadata else {},
        )
        try:
            return object_storage.DatasetCreateResponse.parse_obj(
                response.json()
            ).dict()
        except Exception:
            return "Error: Server returned {} while creating dataset {}: {}".format(
                response.status_code, dataset_name, response.text
            )

    @check_capability_availability
    def create_dataset_metadata(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName = None,
        metadata: dict = None,
    ) -> str:
        params = {"collection_name": collection_name}
        if dataset_name:
            params.update({"dataset_name": dataset_name})
        return self._client.post(
            self._proxy_path("createDatasetMetadata"),
            params=params,
            headers=_encode_metadata(metadata) if metadata else {},
        ).text

    @check_capability_availability
    def get_dataset(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
    ) -> Union[Dict, str]:
        return self._client.get(
            self._proxy_path("getDataset"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
        ).content

    def create_or_replace_dataset(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName = None,
        metadata: dict = None,
        file: UploadFile = None,
    ) -> object_storage.DatasetCreateResponse:
        params = {"collection_name": collection_name}
        if dataset_name:
            params.update({"dataset_name": dataset_name})
        return object_storage.DatasetCreateResponse(
            **self._client.put(
                self._proxy_path("createOrReplaceDataset"),
                params=params,
                headers=_encode_metadata(metadata),
                data=file.file,
            )
        )

    @check_capability_availability
    def create_or_replace_dataset_metadata(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
        metadata: dict = None,
    ) -> str:
        return self._client.put(
            self._proxy_path("createOrReplaceDatasetMetadata"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
            headers=_encode_metadata(metadata) if metadata else {},
        ).text

    @check_capability_availability
    def delete_dataset(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
    ):
        return self._client.delete(
            self._proxy_path("deleteDataset"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
        ).text

    # NOTE: change to GET for the meeting if proxy doesn't support HEAD requests
    @check_capability_availability
    def get_dataset_metadata(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
    ) -> Union[Dict, str]:
        response_headers: dict = self._client.head(
            self._proxy_path("getDatasetMetadata"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
        ).headers
        return json.dumps(_decode_metadata(headers=response_headers))

    @check_capability_availability
    def list_semantic_mappings(
        self, limit: int = 100, offset: int = 0
    ) -> object_storage.SemanticMappingListResponse:
        return object_storage.SemanticMappingListResponse(
            **self._client.get(
                self._proxy_path("listSemanticMappings"),
                params={"limit": limit, "offset": offset},
            ).json()
        )

    @check_capability_availability
    def get_semantic_mapping(
        self, semantic_mapping_id: str
    ) -> object_storage.SemanticMappingModel:
        return object_storage.SemanticMappingModel.parse_obj(
            self._client.get(
                self._proxy_path("getSemanticMapping"),
                params={"semantic_mapping_id": semantic_mapping_id},
            ).json()
        )

    @check_capability_availability
    def get_collection_metadata_dcat(
        self, collection_name: object_storage.CollectionName
    ) -> Union[Dict, str]:
        response: dict = self._client.get(
            self._proxy_path("getCollectionMetadataDcat"),
            params={"collection_name": collection_name},
        ).text
        return response

    @check_capability_availability
    def get_dataset_metadata_dcat(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
    ) -> Union[Dict, str]:
        response: dict = self._client.get(
            self._proxy_path("getDatasetMetadataDcat"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
        ).text
        return response

    @check_capability_availability
    def query_dataset(
        self,
        collection_name: object_storage.CollectionName,
        dataset_name: object_storage.DatasetName,
        query: str,
    ) -> Union[Dict, str]:
        response: dict = self._client.post(
            self._proxy_path("queryDataset"),
            params={"collection_name": collection_name, "dataset_name": dataset_name},
            json={"query": query},
        ).text
        return response

    @check_capability_availability
    def query(self, query: str, meta_data: bool = False) -> Union[Dict, str]:
        response: dict = self._client.post(
            self._proxy_path("query"), json={"query": query, "meta_data": meta_data}
        ).text
        return response
