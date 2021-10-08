from app.core.config import settings


def handler(event, context):
    """
    :param event: AWS event data (SQS's data)
    :param context: AWS function's context
    :return:
    """
    print("reached handler")
    print(settings.PROJECT_NAME)
    print(settings.SERVER_STACK)
    print(event)
    return True
