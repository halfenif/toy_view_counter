# toy_view_counter
Counter Service for Static Web (Ex Jekylle Blog)
> Jekyll로 만든 블로그의 조회수용으로 만들었습니다.

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
- ORIGINS = [""] # Allow List Request Origin
