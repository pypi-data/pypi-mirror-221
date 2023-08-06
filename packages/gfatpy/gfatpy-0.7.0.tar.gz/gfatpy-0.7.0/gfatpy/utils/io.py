from pdb import set_trace
import zipfile
import tempfile
import numpy as np
from typing import Any, Tuple
from pathlib import Path
from datetime import datetime

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import yaml


def read_yaml(path: Path | str) -> Any:
    """
    Reads a yaml file and returns the data as a dictionary.
    """
    with open(path, "r") as stream:
        return yaml.safe_load(stream)


def convert_pdf_to_txt(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(path, "rb")
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


from pathlib import Path
import numpy as np
from datetime import datetime


def find_nearest_filepath(
    dir: Path, wildcard_filename: str, date_location_in_filename: int, date: datetime
) -> Path:
    """Finds the nearest file path in the specified directory based on a wildcard filename pattern and a target date.

    Args:
        dir (Path): The directory to search for files.
        wildcard_filename (str): The wildcard filename pattern to match files.
        date_location_in_filename (int): The index of the date in the filename split by underscores.
        date (datetime): The target date to find the nearest file.

    Returns:
        Path: The path to the nearest file.

    Raises:
        ValueError: If no file is found in the directory.

    """
    # Get all candidate file paths
    candidates = [*dir.rglob(wildcard_filename)]

    # Raise an error if no candidate files are found
    if not candidates:
        raise ValueError("No file found.")

    # Extract the dates from candidate file names
    candidate_dates = np.array(
        [
            np.datetime64(p.name.split(".")[0].split("_")[date_location_in_filename])
            for p in candidates
        ]
    )

    # Calculate the differences between target date and candidate dates
    date_diffs = np.abs(candidate_dates - np.datetime64(date))

    # Find the index of the minimum date difference
    idx = np.argmin(date_diffs)

    # Get the path of the nearest file
    path = candidates[idx]

    # Raise an error if the path does not exist
    if not path.exists():
        raise ValueError("No file found.")

    return path

def unzip_file_to_temp(file: Path) -> Path:
    
    if file.suffix != ".zip":
        raise ValueError("The file is not a zip file.")
    
    filename = file.name.split(".")[0]

    # Create a temporary directory    
    temp_dir = Path(tempfile.mkdtemp(prefix="tmp_unzipped_", dir=Path.cwd().as_posix()))
    unzip_file = temp_dir / filename
    try:
        # Extract the zip file
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(unzip_file)
            
    except zipfile.BadZipFile:
        raise ValueError("The file is not a valid zip file.")        

    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")            
    return unzip_file            