import falcon
from kafka import KafkaConsumer


class StreamDataSensor:
    def on_get(self, req, resp):
        self.consumer = KafkaConsumer('temphum',
                                      bootstrap_servers='kafka1:9614',
                                      request_timeout_ms=50000)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/event-stream'
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Credentials', 'true')
        resp.stream = self.stream()

    def stream(self):
        for msg in self.consumer:
            a = b'data:'
            b = msg.value
            c = b'\n\n'
            yield b''.join([a, b, c])
