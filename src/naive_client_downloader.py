import re
import io
import tarfile
import requests

github_api_url = "https://api.github.com/repos/klzgrad/naiveproxy/releases/latest"
search_pattern = re.compile(r"naiveproxy.+-linux-x64\.tar\.xz")

release_resp = requests.get(github_api_url)
if release_resp.status_code >= 200 and release_resp.status_code < 300:
    release_meta: dict = release_resp.json()
else:
    for key, value in release_resp.headers.items():
        print(f"{key}: {value}")
    print(release_resp.content)
    raise RuntimeError("Failed to call github api.")

print(f"Got naiveproxy client version: {release_meta['name']}")
print(f"Updates @ {release_meta['published_at']}")

tar_data = None
for asset in release_meta["assets"]:
    name = asset.get("name", None)
    download_url = asset.get("browser_download_url", None)
    if search_pattern.match(name):
        download_resp = requests.get(download_url)
        if download_resp.status_code >= 200 and download_resp.status_code < 300:
            tar_data = io.BytesIO(download_resp.content)

if tar_data is None:
    raise RuntimeError("Failed to download the archive file.")

tar = tarfile.open(fileobj=tar_data)
for member in tar.getmembers():
    if member.name.endswith("/naive"):
        member.name = "naive"
        tar.extract(member, path="/app")
