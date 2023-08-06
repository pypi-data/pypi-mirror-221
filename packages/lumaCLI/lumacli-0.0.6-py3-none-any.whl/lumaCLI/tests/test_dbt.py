from lumaCLI import app
from typer.testing import CliRunner
from lumaCLI.tests.utils import METADATA_DIR


runner = CliRunner()


def test_ingest(post_endpoint):
    result = runner.invoke(
        app,
        [
            "dbt",
            "ingest",
            METADATA_DIR,
            "--endpoint",
            post_endpoint,
        ],
    )

    assert result.exit_code == 0, result.output


def test_send_test_results(post_endpoint):
    result = runner.invoke(
        app,
        [
            "dbt",
            "send-test-results",
            METADATA_DIR,
            "--endpoint",
            post_endpoint,
        ],
    )
    assert result.exit_code == 0, result.output
