"""
Producer
"""
from argparse import ArgumentParser
import json
from typing import Any
from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor
from kafka.producer.kafka import KafkaProducer

from admin import get_admin_config
from data import get_fake_data

_PARTITION_STRATEGY = (RoundRobinPartitionAssignor,)

def _get_producer_config() -> dict:
    """
    Get producer config
    """
    kafka_config = get_admin_config()
    return kafka_config

def _json_serializer(data: Any) -> bytes:
    return json.dumps(data).encode("utf-8")

_producer = KafkaProducer(**_get_producer_config(), value_serializer=_json_serializer)

def publish_message(*, topic_name: str, value: str):
    """
    Publish message.
    """
    try:
        print("Publishing message to local buffer...")
        _producer.send(topic_name, value)
        print("Published message to local buffer.")
    except Exception as error:
        print(f"Unknown error: {error}")
        raise error

if __name__ == "__main__":
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('topic_name', type=str)
    args = parser.parse_args()

    # Get fake data
    fake_data = get_fake_data()
    print("Got fake data", fake_data)

    # Create topic
    publish_message(topic_name=args.topic_name, value=fake_data)