import os
import json
import subprocess

# Build config.json with environments
local_addr = "0.0.0.0:1080"
proto = os.environ.get("APP_PROTO", "socks")
proxy = os.environ.get("APP_PROXY", None)
if proxy is None:
    raise RuntimeError("APP_PROXY does not specified.")
with open("/app/config.json", "w", encoding="utf-8") as f:
    json.dump({"listen": f"{proto}://{local_addr}", "proxy": proxy}, f)

# Build up command line
cmd = ["/app/naive", "--log"]
subprocess.run(cmd)
