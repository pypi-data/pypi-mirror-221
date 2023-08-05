# Name: Airtime
# Description: A package for analyzing meeting transcripts to determine speaking time distribution among participants.

# Copyright 2023 Jana M. Perkins.
# See the LICENSE file at the top-level directory of this distribution and at
# https://github.com/jcontd/airtime/blob/main/LICENSE


import os
import pytest
from ..teams_analyzer import (
    read_transcript, calculate_word_totals,
    print_results, analyze_teams_transcript
)


@pytest.fixture
def transcript_file(transcript_content):
    transcript_file = "temp_transcript.txt"
    with open(transcript_file, "w") as f:
        f.write(transcript_content)
    yield transcript_file
    os.remove(transcript_file)


@pytest.fixture
def transcript_content():
    return ("00:00:00.000 --> 00:00:00.200\n"
            "<v Speaker A>Hello, world!</v>\n"
            "\n"
            "00:00:04.480 --> 00:00:11.120\n"
            "<v Speaker B>Goodbye, world!</v>\n")


@pytest.fixture
def expected_output():
    return (
        "MEETING TOTALS\n"
        "- 4 words\n"
        "- 2 speaker(s)\n\n"
        "SPEAKER TOTALS\n"
        "- Speaker A: 2 words (50.0% of meeting)\n"
        "- Speaker B: 2 words (50.0% of meeting)\n"
    )


def test_read_transcript(transcript_file):
    try:
        read_transcript(transcript_file)
    except Exception:
        pytest.fail("""read_transcript raised an exception
                    unexpectedly when reading an existing file.""")

    result = read_transcript("nonexistent_file.txt")
    assert result == {}, """read_transcript did not return
     an empty dictionary for a nonexistent file."""

    result = read_transcript(".")
    assert result == {}, """read_transcript did not return
    an empty dictionary when a directory is passed as a file."""


def test_calculate_word_totals(transcript_file):
    speaker_texts = read_transcript(transcript_file)
    word_totals, overall_total = calculate_word_totals(speaker_texts)
    assert word_totals == {"Speaker A": 2, "Speaker B": 2}
    assert overall_total == 4

    speaker_texts = {}
    word_totals, overall_total = calculate_word_totals(speaker_texts)
    assert word_totals == {}
    assert overall_total == 0


def test_calculate_word_totals_with_invalid_input():
    with pytest.raises(TypeError):
        calculate_word_totals({1: "Hello, world!"})

    with pytest.raises(TypeError):
        calculate_word_totals({"Speaker A": 123})

    speaker_texts = {"Speaker A": ""}
    word_totals, overall_total = calculate_word_totals(speaker_texts)
    assert word_totals == {"Speaker A": 0}
    assert overall_total == 0


def test_print_results(capsys, expected_output):
    word_totals = {"Speaker A": 2, "Speaker B": 2}
    overall_total = 4

    print_results(word_totals, overall_total)

    captured = capsys.readouterr()

    assert captured.out == expected_output


def test_analyze_teams_transcript(capsys, transcript_file, expected_output):
    analyze_teams_transcript(transcript_file)

    captured = capsys.readouterr()

    assert captured.out.strip() == expected_output.strip()


def test_analyze_teams_transcript_with_invalid_input(capsys):
    analyze_teams_transcript("nonexistent_file.vtt")
    captured = capsys.readouterr()
    assert "The file nonexistent_file.vtt could not be found." in captured.out

    analyze_teams_transcript(123)
    captured = capsys.readouterr()
    assert "An error occurred: file_name must be a string." in captured.out
