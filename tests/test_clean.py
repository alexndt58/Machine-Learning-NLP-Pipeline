from src.preprocess import TextCleaner
def test_strip_urls():
    cleaner = TextCleaner({"lower": False, "regex_clean": "basic"})
    out = cleaner.transform(["Check link https://example.com"])
    assert "{{URL}}" in out[0]
