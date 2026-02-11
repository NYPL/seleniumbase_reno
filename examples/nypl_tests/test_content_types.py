"""
Content type regression tests - verify pages load successfully 
by ensuring no error page is displayed.

Enhanced parametrized implementation - each content type runs as a separate test
for better isolation and reporting.
"""
import json
import os
import pytest
from seleniumbase import BaseCase


# Load content types once at module level
def load_content_types():
    """Load content types from JSON file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "resources", "content-types.json")
    
    with open(json_path, "r") as f:
        return json.load(f)


# Load data once
CONTENT_TYPES = load_content_types()


class ContentTypeTests(BaseCase):
    """Test suite for content type regression tests"""

    def get_base_url(self):
        """Get base URL based on environment (--env=qa or production)"""
        base_url = "https://www.nypl.org"
        qa_base_url = "https://qa-www.nypl.org"
        
        if self.env == "qa":
            return qa_base_url
        else:
            return base_url

    def verify_not_error_page(self):
        """Verify we're not on an error page with enhanced checks"""
        # Check multiple heading levels for better coverage
        error_selectors = [
            "h1:contains('we\\'re sorry')",
            "h2:contains('we\\'re sorry')",
            "h3:contains('we\\'re sorry')"
        ]
        
        for selector in error_selectors:
            if self.is_element_visible(selector):
                raise AssertionError(f"Error page detected: '{selector}' is visible")

    # Parametrized Twig content type tests - each runs as separate test
    @pytest.mark.regression
    @pytest.mark.parametrize("content_type", CONTENT_TYPES["twig"], ids=lambda x: x["name"])
    def test_twig_content_type(self, content_type):
        """Test individual Twig-rendered content type"""
        base_url = self.get_base_url()
        name = content_type["name"]
        url = content_type["url"]
        
        print(f"\nTesting {name} on {base_url}")
        self.open(f"{base_url}{url}")
        self.verify_not_error_page()

    # Parametrized Scout content type tests - each runs as separate test
    @pytest.mark.regression
    @pytest.mark.parametrize("content_type", CONTENT_TYPES["scout"], ids=lambda x: x["name"])
    def test_scout_content_type(self, content_type):
        """Test individual Scout-rendered content type"""
        base_url = self.get_base_url()
        name = content_type["name"]
        url = content_type["url"]
        
        print(f"\nTesting {name} on {base_url}")
        self.open(f"{base_url}{url}")
        self.verify_not_error_page()
