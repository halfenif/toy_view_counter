podman container kill toy_view_counter
podman container rm toy_view_counter
# podman builder prune -af

podman-compose build
podman-compose up --detach