from datetime import datetime, timezone
import pytz

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Convert epoch to a timezone-aware datetime (UTC)
    utc_time = datetime.fromtimestamp(data['dt'], tz=timezone.utc)

    # Convert to a specific time zone
    local_timezone = pytz.timezone(kwargs['TIMEZONE'])
    local_time = utc_time.astimezone(local_timezone)

    # Format datetime as an ISO 8601 string with timezone information
    formatted_time_with_tz = local_time.isoformat()

    return formatted_time_with_tz


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
