import falcon
from falcon_cors import CORS
from temphum_core.sensor import StreamDataSensor

cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True)
api = application = falcon.API(middleware=[cors.middleware])
api.add_route('/stream/', StreamDataSensor())
