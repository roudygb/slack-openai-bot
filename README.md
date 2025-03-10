# slack-openai-bot

To deploy this bot on Google Cloud, first create an artifact registry to push it to. Then build the Docker image with a complete `.env` file.

```bash
docker build -t us-central1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$FOLDER/slack-bot .
```

You can test the image locally or push it to Artifact Registry.

```bash
docker push us-central1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$FOLDER/slack-bot
```

From there, you can click-button deploy it to Google Cloud Run.

![img](img/deploy-to-cloud-run.png)
