# scrapy minio feed exports

## How to Running

* init venv

```code
python -m venv venv
source venv/bin/activate
```

* starting container service

```code
docker-compose up -d

create s3 bucket mydemo (localhost:9000)
```

* running

```code
pip install requirements.txt

cd dalongdemo

scrapy crawl blogs

```

