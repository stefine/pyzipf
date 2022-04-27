from collate import process_file
import numpy as np
import pytest
import plotcounts
from collections import Counter

from numpy import arange

import countwords


def test_word_count():
    """Test the counting of words.

    The example poem is Risk, by Anaïs Nin.
    """
    risk_poem_counts = {'the': 3, 'risk': 2, 'to': 2, 'and': 1,
                        'then': 1, 'day': 1, 'came': 1, 'when': 1, 'remain': 1,
                        'tight': 1, 'in': 1, 'a': 1, 'bud': 1, 'was': 1,
                        'more': 1, 'painful': 1, 'than': 1, 'it': 1, 'took': 1,
                        'blossom': 1}
    expected_results = Counter(risk_poem_counts)
    with open('test_data/risk.txt', 'r') as reader:
        actual_result = countwords.count_words(reader)
    assert actual_result == expected_results


def test_alpha():
    """Test the calculation of the alpha parameter.

    The test word counts satisfy the relationship,
      r = cf**(-1/alpha), where
      r is the rank,
      f the word count, and
      c is a constant of proportionality.

    To generate test word counts for an expected alpha
    assume alpha = 1, c = 600, r ranges from 1 to 600, 
    f = c/r 
    f ∝ word counts, so we use `floor(f)` denotes word counts
    """
    max_freq = 600
    counts = np.floor(max_freq / np.arange(1, max_freq+1))
    actural_alpha = plotcounts.get_power_law_params(counts)
    expected_alpha = pytest.approx(1.0, abs=0.01)
    assert actural_alpha == expected_alpha


def test_regression():
    """Regression test for Dracula"""
    with open('data/dracula.txt', 'r') as reader:
        word_counts_dict = countwords.count_words(reader)
    counts_array = np.array(list(word_counts_dict.values()))
    actural_alpha = plotcounts.get_power_law_params(counts_array)
    expected_alpha = pytest.approx(1.087, abs=0.01)
    assert actural_alpha == expected_alpha


def test_fileFormats():
    word_counts = Counter()
    fname = 'data/dracula.txt'
    with pytest.raises(OSError):
        process_file(fname, word_counts)


def test_fileExist():
    word_counts = Counter()
    fname = 'fake_file.csv'
    with pytest.raises(FileNotFoundError):
        process_file(fname, word_counts)
