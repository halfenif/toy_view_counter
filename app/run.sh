#!/bin/bash
docker container kill toy_view_counter
uvicorn app:app --port 9050 --host 0.0.0.0