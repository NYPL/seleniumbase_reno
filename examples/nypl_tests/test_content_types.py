"""
Content type regression tests - verify pages load successfully 
by ensuring no error page is displayed.

Basic implementation - loads content types from JSON and validates
they don't display error pages.
"""
import json
import os
import pytest
from seleniumbase import BaseCase


class ContentTypeTests(BaseCase):
    """Test suite for content type regression tests"""

    @classmethod
    def setUpClass(cls):
        """Load content types JSON once for all tests"""
        super().setUpClass()
        # Get the path to the JSON file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "resources", "content-types.json")
        
        with open(json_path, "r") as f:
            cls.content_types = json.load(f)

    def get_base_url(self):
        """Get base URL based on environment (--env=qa or production)"""
        base_url = "https://www.nypl.org"
        qa_base_url = "https://qa-www.nypl.org"
        
        if self.env == "qa":
            return qa_base_url
        else:
            return base_url

    def verify_not_error_page(self):
        """Verify we're not on an error page"""
        # Simple check for error heading
        error_heading_present = self.is_element_visible("h1:contains('we\\'re sorry')")
        if error_heading_present:
            raise AssertionError("Error page detected")

    @pytest.mark.regression
    def test_twig_content_types(self):
        """Test all Twig-rendered content types"""
        base_url = self.get_base_url()
        twig_types = self.content_types.get("twig", [])
        
        print(f"\nRunning on: {base_url}")
        
        for content_type in twig_types:
            name = content_type["name"]
            url = content_type["url"]
            
            print(f"\nTesting: {name}")
            self.open(f"{base_url}{url}")
            self.verify_not_error_page()

    @pytest.mark.regression
    def test_scout_content_types(self):
        """Test all Scout-rendered content types"""
        base_url = self.get_base_url()
        scout_types = self.content_types.get("scout", [])
        
        print(f"\nRunning on: {base_url}")
        
        for content_type in scout_types:
            name = content_type["name"]
            url = content_type["url"]
            
            print(f"\nTesting: {name}")
            self.open(f"{base_url}{url}")
            self.verify_not_error_page()
