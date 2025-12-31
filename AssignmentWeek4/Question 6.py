from collections import namedtuple

StreamConfig = namedtuple(
    "StreamConfig",
    [
        "batch_size",
        "environment"
    ]
)

config = StreamConfig(
    batch_size=100,
    environment="DEV"
)

class DataStreamer:
    def __init__(self, config):
        self.config = config

    def process_batch(self, data):
        print(f"Environment: {self.config.environment}")
        print(f"Processing {self.config.batch_size} records")

        for item in data[:self.config.batch_size]:
            print(f"Processing item: {item}")

streamer = DataStreamer(config)
streamer.process_batch(range(1, 10))
