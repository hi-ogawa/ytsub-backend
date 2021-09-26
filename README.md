Backend for https://github.com/hi-ogawa/ytsub

```bash
# Setup database
docker-compose up
make db/reset db/reset/test

# Pip install
make install

# Lint
make lint

# Add dependency
make add package=mypy

# Testing
make test
```
