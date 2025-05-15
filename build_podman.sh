podman stop toy_view_counter
podman container rm toy_view_counter
podman image rm localhost/toy_view_counter_toy_view_counter
# podman builder prune -af

podman-compose build
podman-compose up --detach