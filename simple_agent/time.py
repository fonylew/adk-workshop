import datetime
from zoneinfo import ZoneInfo

def get_current_time(tz_identifier: str="Asia/Bangkok") -> dict:
    """Returns the current time in a specified city.

    Args:
        tz_identifier (str): The Timezone identifier of the city for which to retrieve the current time. If user not specify, default is "Asia/Bangkok".

    Returns:
        dict: status and result or error msg.
    """

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {tz_identifier.split("/")[1]} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}