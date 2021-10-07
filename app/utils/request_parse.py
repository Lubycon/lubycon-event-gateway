from user_agents import parse


async def get_user_agent_data(user_agent: str) -> dict:
    data = parse(user_agent)
    return {
        'uabf': data.browser.family,
        'uabv': data.browser.version_string,
        'uaof': data.os.family,
        'uaov': data.os.version_string,
        'uadf': data.device.family,
        'uadb': data.device.brand,
        'uadm': data.device.model,
    }


async def dict_values_convert_string(data: dict) -> dict:
    return {k: str(v) for k, v in data.items()}
