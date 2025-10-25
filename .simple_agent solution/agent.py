import datetime
from zoneinfo import ZoneInfo
from google.adk.agents.llm_agent import Agent


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


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_time]
)
