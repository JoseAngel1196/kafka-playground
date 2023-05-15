%:
	@:

.PHONY: create-topic
create-topic:
	PYTHONPATH=. poetry run python topic/create_topic.py $(filter-out $@, $(MAKECMDGOALS))

.PHONY: list-topic
list-topic:
	docker exec broker kafka-topics --bootstrap-server broker:9092 --list

.PHONY: publish-message
publish-message:
	# ./bin/kafka-console-producer --bootstrap-server broker:9092 --topic topic_name
	PYTHONPATH=. poetry run python producer.py playground

.PHONY: consume-message
consume-message:
	# ./bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic topic_name