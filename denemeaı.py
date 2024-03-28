from pprint import pprint

import replicate
from dotenv import load_dotenv

load_dotenv()

output = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
input={"prompt": "Şükrü Saraçoğlu Stadium is also a football player, pointillism"}

)

print(output)
# ['https://replicate.delivery/pbxt/VJyWBjIYgqqCCBEhpkCqdevTgAJbl4fg62aO4o9A0x85CgNSA/out-0.png']