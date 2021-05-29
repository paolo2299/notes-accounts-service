.PHONY: build console run release

APPLICATION=accounts-service

GCR_IMAGE_URL=eu.gcr.io/paul-personal-306310/$(APPLICATION)

build:
	docker-compose build

check_credentials:
	docker run --rm \
	  -v $(shell pwd)/scripts:/scripts \
	  -v $(HOME)/.config/gcloud:/config \
	  python:3.9.0-buster bash -c "python /scripts/check_credentials.py"

console:
	docker-compose run --rm --service-ports app bash

mysql:
	docker-compose run --rm mysql_cli

run: check_credentials
	docker-compose up app

release:
	docker build -t $(GCR_IMAGE_URL):latest .
	docker push $(GCR_IMAGE_URL):latest

deploy: release #TODO remove password
	gcloud run deploy $(APPLICATION) \
	  --image $(GCR_IMAGE_URL):latest \
	  --platform managed \
	  --region europe-west2 \
	  --allow-unauthenticated \
	  --concurrency 4 \
	  --add-cloudsql-instances paul-personal-306310:europe-west2:notes \
	  --set-env-vars "FLASK_ENV=production" \
	  --set-env-vars "NOTES_ENV=production" \
	  --set-env-vars "MYSQL_USER=root" \
	  --set-env-vars "MYSQL_PASSWORD=Kudv45jlgf1rpBot" \
	  --set-env-vars "MYSQL_DATABASE=accounts" \
	  --set-env-vars "INSTANCE_CONNECTION_NAME=paul-personal-306310:europe-west2:notes"
