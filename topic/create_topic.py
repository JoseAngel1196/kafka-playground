"""
Create topic.
"""
from argparse import ArgumentParser
from typing import Optional
from kafka.admin.new_topic import NewTopic

from admin import ADMIN_CLIENT

_TOPIC_PARTITION_COUNT = 1
_TOPIC_REPLICATION_FACTOR = 1

def create_topic(topic_name: str, num_partitions: Optional[int] = _TOPIC_PARTITION_COUNT, replication_factor: Optional[int] = _TOPIC_REPLICATION_FACTOR):
    """
    Create topic.
    """
    new_topic = NewTopic(topic_name, num_partitions, replication_factor)

    try:
        ADMIN_CLIENT.create_topics(new_topics=[new_topic], timeout_ms=5000)
        print(f"Topic {topic_name} created")
    except Exception as error:
        print(f"Unknown error {topic_name}: {error}")
        raise error
    
if __name__ == "__main__":
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('topic_name', type=str)
    args = parser.parse_args()

    # Create topic
    create_topic(args.topic_name)