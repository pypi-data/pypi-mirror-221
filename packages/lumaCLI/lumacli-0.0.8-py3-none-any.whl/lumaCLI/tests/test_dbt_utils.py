import json
from lumaCLI.tests.utils import MANIFEST_JSON, FILE_TXT, INVALID_JSON
from lumaCLI.utils import validate_json, json_to_dict, print_response
from unittest.mock import patch, MagicMock
from io import StringIO
from requests.models import Response


def test_validate_json():
    # Positive test case
    is_json = validate_json(json_path=MANIFEST_JSON)
    assert is_json

    # Positive test case with custom endswith
    is_json = validate_json(json_path=MANIFEST_JSON, endswith=".json")
    assert is_json

    # Negative test case with wrong endswith
    is_json = validate_json(json_path=MANIFEST_JSON, endswith=".txt")
    assert not is_json

    # Negative test case with non-existent file
    is_json = validate_json(json_path="non_existent_file.json")
    assert not is_json

    # Negative test case with a file that is not a .json file
    is_json = validate_json(json_path=FILE_TXT)
    assert not is_json


def test_validate_json_to_dict():
    # Positive test case with valid JSON file
    dict_data = json_to_dict(json_path=MANIFEST_JSON)
    assert isinstance(dict_data, dict)

    # Negative test case with non-existent file
    try:
        dict_data = json_to_dict(json_path="non_existent_file.json")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass

    # Negative test case with a file that is not a .json file
    try:
        dict_data = json_to_dict(json_path=FILE_TXT)
        assert False, "Expected json.decoder.JSONDecodeError"
    except json.decoder.JSONDecodeError:
        pass

    # Negative test case with a JSON file that contains invalid JSON
    try:
        dict_data = json_to_dict(json_path=INVALID_JSON)
        assert False, "Expected json.decoder.JSONDecodeError"
    except json.decoder.JSONDecodeError:
        pass


def test_print_response_success():
    response = MagicMock(spec=Response)
    response.ok = True
    response.json.return_value = {"some": "data"}

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        print_response(response)

        # Check the output
        stdout = mock_stdout.getvalue()
        assert "The dbt ingestion to luma was successful!" in stdout
        assert "Items ingested:" in stdout
        assert str(response.json()) in stdout


def test_print_response_error():
    response = MagicMock(spec=Response)
    response.ok = False
    response.status_code = 400
    response.text = "Bad Request"

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        print_response(response)

        # Check the output
        stdout = mock_stdout.getvalue()
        assert "An HTTP error occurred, response status code" in stdout
        assert str(response.status_code) in stdout
        assert (
            response.text not in stdout
        )  # It seems that 'response.text' is not being printed out, hence the assertion


def test_print_response_error_with_json():
    response = MagicMock(spec=Response)
    response.ok = False
    response.status_code = 400
    response.json.return_value = {"detail": "Bad Request"}

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        print_response(response)

        # Check the output
        stdout = mock_stdout.getvalue()
        assert "An HTTP error occurred, response status code" in stdout
        assert str(response.status_code) in stdout
        assert str(response.json()["detail"]) in stdout


def test_print_response_success_with_json_error():
    response = MagicMock(spec=Response)
    response.ok = True
    response.json.side_effect = Exception("Error at printing items ingested")

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        print_response(response)

        # Check the output
        stdout = mock_stdout.getvalue()
        assert "The dbt ingestion to luma was successful!" in stdout
        assert "Items ingested:" in stdout
        assert "Error at printing items ingested" in stdout
