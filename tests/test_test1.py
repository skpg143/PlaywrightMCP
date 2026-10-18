
from pathlib import Path

def test_read_text_file():
    # Get the folder containing this Python script
    folder_path = Path(__file__).resolve().parent

    # Build the full path to test.txt
    file_path = folder_path / "test.txt"

    # Check whether the file exists
    print(f"\nLooking for file: {file_path}")
    assert file_path.exists(), f"File not found: {file_path}"

    # Read the text file
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    print("\nText file data:")
    print(data)

    # Verify the content
    assert data.strip(), "The text file is empty!"

