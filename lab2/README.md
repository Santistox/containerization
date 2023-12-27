# Spark docker compose

run docker

```bash
docker compose up -d
```

open master bash

```bash
docker exec -it < master container name > bash
```

start task

```bash
/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
--driver-memory 1G \
--executor-memory 1G \
/opt/spark-apps/my_spark.py
```
