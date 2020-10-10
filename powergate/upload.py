from pygate_grpc.client import PowerGateClient
from pygate_grpc.ffs import get_file_bytes, bytes_to_chunks
import os

api = os.getenv('POWERGATE_API')
powergate = PowerGateClient(api, False)
ffs = os.getenv('POWERGATE_FFS')
token = os.getenv('POWERGATE_TOKEN')

upload_file = "/home/peter/open-images/pipeline/source_data/packages/deplatformr-open-images-2.tar"

print("Uploading file...")
iter = get_file_bytes(upload_file)
res = powergate.ffs.stage(bytes_to_chunks(iter), token)
print(res)

push = powergate.ffs.push(res.cid, token)
print(push)

check = powergate.ffs.info(res.cid, token)
print(check)
