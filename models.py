from pydantic import BaseModel

class BaseClientConfig(BaseModel):
    """
    ...
    """

class BaseKafkaClientConfig(BaseClientConfig):
    """
    ...
    """
    kafka_topic: str
