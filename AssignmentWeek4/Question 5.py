class DataStreamer:

    def __init__(self, list_of_data):
        self.list_of_data = list_of_data
        self.index = 0

    def stream(self):
        while self.index < len(self.list_of_data):
            value = self.list_of_data[self.index] * 2
            self.index += 1
            yield value

    def partial_stream(self, generator, max_items):
        for _ in range(min(max_items, len(self.list_of_data) - self.index)):
            print(f"Partial Stream :- {next(generator)}")


streamer = DataStreamer(range(1, 1000000))
generator = streamer.stream()
streamer.partial_stream(generator, 4)
for _ in range(3):
    print(next(generator))
