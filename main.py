def refresh_translations(self):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.TRANSLATION_ACCESS_KEY_ID,
        aws_secret_access_key=settings.TRANSLATION_SECRET_ACCESS_KEY
    )

    session = Session(
        aws_access_key_id=settings.TRANSLATION_ACCESS_KEY_ID,
        aws_secret_access_key=settings.TRANSLATION_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')
    your_bucket = s3.Bucket(settings.TRANSLATION_BUCKET_NAME)
    for s3_file in your_bucket.objects.filter(Prefix=f"{CH_APP_LABEL}/{settings.FLASK_ENV}"):

        try:
            _, _, _, lang, file = s3_file.key.split('/')
        except ValueError:
            continue

        if not file.endswith(".po"):
            continue

        if not os.path.isdir(f'translations/po_files/{lang}'):
            os.mkdir(f'translations/po_files/{lang}')

        s3_client.download_file(settings.TRANSLATION_BUCKET_NAME, s3_file.key, f'translations/po_files/{lang}/{file}')

        self.convert_po_to_json(
            po_file=f'translations/po_files/{lang}/{file}',
            json_file=f'translations/json_files/{lang}.json',
            lang=lang
        )