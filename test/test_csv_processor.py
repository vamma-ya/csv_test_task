import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from csv_processor import parse_condition, filter_data, aggregate_data

sample_data = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]

def test_parse_condition():
    assert parse_condition("price>100") == ("price", ">", "100")
    assert parse_condition("brand=apple") == ("brand", "=", "apple")
    assert parse_condition("rating<4.5") == ("rating", "<", "4.5")

def test_filter_data_equal():
    result = filter_data(sample_data, "brand=apple")
    assert len(result) == 1
    assert result[0]["name"] == "iphone 15 pro"

def test_filter_data_greater_than():
    result = filter_data(sample_data, "price>1000")
    assert len(result) == 1
    assert result[0]["brand"] == "samsung"

def test_filter_data_less_than():
    result = filter_data(sample_data, "rating<4.7")
    assert len(result) == 2
    assert result[0]["name"] == "redmi note 12"

def test_aggregate_avg():
    result = aggregate_data(sample_data, "rating=avg")
    assert result["avg"] == pytest.approx(4.675, 0.01)

def test_aggregate_min():
    result = aggregate_data(sample_data, "price=min")
    assert result["min"] == 199

def test_aggregate_max():
    result = aggregate_data(sample_data, "rating=max")
    assert result["max"] == 4.9

def test_aggregate_invalid_column():
    bad_data = [{"name": "test", "brand": "apple"}]
    with pytest.raises(ValueError):
        aggregate_data(bad_data, "brand=avg")
