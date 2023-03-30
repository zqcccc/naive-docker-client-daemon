docker build -t naive-client-daemon:tests -f Dockerfile .
docker run \
  -e APP_PROTO="socks" \
  -e APP_PROXY="https://****:***@****" \
  -p 1080 \
  -t naive-client-daemon:tests
