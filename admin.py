"""
Kafka Admin Client
"""
from kafka.admin.client import KafkaAdminClient

_ADMIN_BROKER_URL = "localhost:9092"

def get_admin_config() -> dict:
    """
    Returns a dict of admin configs
    """
    config = dict(bootstrap_servers=_ADMIN_BROKER_URL)
    return config


ADMIN_CLIENT = KafkaAdminClient(**get_admin_config())
