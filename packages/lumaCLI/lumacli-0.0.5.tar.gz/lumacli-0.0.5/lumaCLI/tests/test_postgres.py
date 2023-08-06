from lumaCLI import app
from typer.testing import CliRunner

runner = CliRunner()


def test_ingest(post_endpoint):
    result = runner.invoke(
        app,
        [
            "postgres",
            "ingest",
            post_endpoint,
        ],
    )
    assert result.exit_code == 0, result.output
