# toy_view_counter
Counter Service for Jekylle Blog

## Concept
- request id (UUID) and response read count (SVG Format)

## Installation
**Requirements**
- Docker, Docker-Compose or Podman

### Clone
```bash
git clone https://github.com/halfenif/toy_view_counter.git
```

## Change Config
```bash
cp .app/.env.sample .app/.env
```
- REFFER_CHECK = bool # Allow any request or NOT
- ORIGINS = [""] # Allow List Request Origin
