import json

from app.core.config import settings

EVENT_LOGS_DUPLICATE_KEY = 'tid'


def handler(event, context):
    """
    :param event: AWS event data (SQS's data)
    :param context: AWS function's context
    :return:
    """
    key_store = []
    data_chunks = []
    for record in event['Records']:
        data = json.loads(record['body'])
        transaction_id = data[EVENT_LOGS_DUPLICATE_KEY]

        if transaction_id in key_store:
            continue

        data_chunks.append(data)
        key_store.append(transaction_id)

    # TODO Insert data into Bigquery
    return True
