# Name: Airtime
# Description: A package for analyzing meeting transcripts to determine speaking time distribution among participants.

# Copyright 2023 Jana M. Perkins.
# See the LICENSE file at the top-level directory of this distribution and at
# https://github.com/jcontd/airtime/blob/main/LICENSE


import re
from collections import defaultdict

SPEECH_REGEX = r"\[(.*?)\] (\d{2}:\d{2}:\d{2})"
TIMESTAMP_REGEX = r"\[.*?\] \d{2}:\d{2}:\d{2}"


def read_transcript(file_name):
    """Reads a transcript file & returns a dictionary with speakers' texts."""
    speaker_texts = defaultdict(str)
    current_speaker = None
    timestamp = None

    try:
        with open(file_name, "r") as f:
            for line in f:
                match = re.match(SPEECH_REGEX, line)
                if match:
                    current_speaker = match.group(1)
                    timestamp = match.group(2)
                elif line.strip() != "" and current_speaker is not None:
                    speaker_texts[current_speaker] += \
                        f"\n[{current_speaker}] {timestamp}\n{line.strip()}"
    except (FileNotFoundError, IsADirectoryError):
        pass

    return speaker_texts


def calculate_word_totals(speaker_texts):
    """Calculates word totals both for each speaker and the overall meeting."""
    for key, value in speaker_texts.items():
        if not isinstance(key, str):
            raise TypeError("All keys in speaker_texts must be strings.")
        if not isinstance(value, str):
            raise TypeError("All values in speaker_texts must be strings.")

    word_totals = {}

    for speaker, text in speaker_texts.items():
        cleaned_text = re.sub(TIMESTAMP_REGEX, "", text)
        speaker_texts[speaker] = cleaned_text

        words = cleaned_text.split()
        word_totals[speaker] = len(words)

    overall_total = sum(word_totals.values())
    return word_totals, overall_total


def print_results(word_totals, overall_total):
    """Prints the results."""
    number_of_speakers = len(word_totals)

    print("MEETING TOTALS")
    print(f"- {overall_total:,} words")
    print(f"- {number_of_speakers} speaker(s)\n")
    print("SPEAKER TOTALS")

    for speaker, total in word_totals.items():
        percentage = (total / overall_total) * 100
        print(f"- {speaker}: {total:,} words ({percentage:.1f}% of meeting)")


def analyze_zoom_transcript(file_name):
    """Processes a Zoom transcript file."""
    if not isinstance(file_name, str):
        print("An error occurred: file_name must be a string.")
        return

    try:
        speaker_texts = read_transcript(file_name)
        if not speaker_texts:
            print(f"The file {file_name} could not be found.")
            return
        word_totals, overall_total = calculate_word_totals(speaker_texts)
        print_results(word_totals, overall_total)
    except Exception as e:
        print(f"""An unexpected error occurred while
              analyzing the transcript: {e}""")


if __name__ == "__main__":
    analyze_zoom_transcript("../../transcript.txt")
