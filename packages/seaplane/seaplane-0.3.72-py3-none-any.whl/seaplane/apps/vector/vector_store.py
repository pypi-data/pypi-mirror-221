       
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, PointVectors

from ...configuration import config 
from typing import Optional, List
from ...model.vector import Vectors, Distance as SPDistance
import uuid

class VectorStore():
    def __init__(self) -> None:
        self.client: Optional[QdrantClient] = None
        self.TIME_OUT_IN_SECONDS = 30        
        pass
    
    def connect(self) -> None:        
        ret = QdrantClient(
          url=config.vector_db_endpoint,
          port=443,
          timeout=self.TIME_OUT_IN_SECONDS
        )

        token = config._token_api.access_token
        if not token:
            token = config._token_api.get_token()

        http_client = ret.http.client
        header_val = f'Bearer {token}'
        
        def auth_middleware(request, call_next):
            request.headers['Authorization'] = header_val
            return call_next(request)        
        
        http_client.add_middleware(auth_middleware)
        
        self.client = ret

    def map_status(self, status) -> str:
        return str(status).lstrip("UpdateStatus.")

    def check_connection(self) -> None:
        if not self.client:
          self.connect()

    def create_index(self, name: str, vector_size: int = 1024, distance: SPDistance = SPDistance.COSINE) -> bool:        
        self.check_connection()

        return self.client.recreate_collection(
          collection_name=name,
          vectors_config=VectorParams(size=vector_size, distance=self._map_to_qdrant_distance(distance)),
          timeout=self.TIME_OUT_IN_SECONDS  
        )
    
    def delete_index(self, name: str) -> bool:
        self.check_connection()

        return self.client.delete_collection(
          collection_name=name,        
          timeout=self.TIME_OUT_IN_SECONDS  
        )

    def list_indexes(self) -> List[str]:
        self.check_connection()

        collections = self.client.get_collections()        
        return [idx.name for idx in collections.collections]
    
    def insert(self, index_name: str, vectors: Vectors) -> str:        
        self.check_connection()

        ids = [vector.id for vector in vectors]

        result = self.client.upsert(
          collection_name=index_name,
          points=[
              PointStruct(
                  id=vector.id,
                  vector=vector.vector,
                  payload=vector.metadata
              )
              for vector in vectors
          ]
        )

        return {"id": ids, "status": self.map_status(result.status)}
    
    def delete(self, index_name: str, id: List[str]) -> None:
        result = self.client.delete_vectors(
            collection_name = index_name,
            vectors = [""],
            points = id
        )

        return self.map_status(result.status)
    
    def update(self, index_name: str, vectors: Vectors) -> None:
        self.check_connection()

        ids = [vector.id for vector in vectors]

        result = self.client.update_vectors(
          collection_name=index_name,          
          vectors=[
              PointVectors(
                  id=vector.id,
                  vector=vector.vector
              )
              for vector in vectors
          ]
        )

        return {"id": ids, "status": self.map_status(result.status)}

    def _map_to_qdrant_distance(self, distance: SPDistance) -> Distance:
        if distance == SPDistance.COSINE:
            return Distance.COSINE
        elif distance == SPDistance.EUCLID:
            return Distance.EUCLID
        elif distance == SPDistance.DOT:
            return Distance.DOT

    

vector_store = VectorStore()