"""
Test for the md generation
"""
import os


def test_outputfile():
    """
    Test that the output file exists
    """
    assert os.path.exists("pyspark_output_data.md")
