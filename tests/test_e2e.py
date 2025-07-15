import pytest
from playwright.sync_api import sync_playwright
import subprocess
import time
import os

def test_button_to_backend_flow():
    """Test that button triggers backend call and displays response on page"""
    
    # Start the server
    server_process = subprocess.Popen(['python', 'app.py'], 
                                     cwd=os.path.dirname(os.path.dirname(__file__)))
    time.sleep(2)  # Give server time to start
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Navigate to the page
            page.goto('http://localhost:8001')
            
            # Check that button exists and is clickable
            button = page.locator('#testButton')
            assert button.is_visible(), "Button should be visible"
            
            # Check initial state - result div should exist but be empty
            result_div = page.locator('#result')
            initial_text = result_div.text_content()
            assert initial_text == '', f"Result div should initially be empty, got: '{initial_text}'"
            
            # Click the button
            button.click()
            
            # Wait for the response and check that "Success:" appears within 5 seconds
            try:
                # Wait for the Success message to appear
                page.wait_for_selector('#result:has-text("Success:")', timeout=5000)
                
                # Verify the content contains the backend response
                result_text = result_div.text_content()
                assert 'Success:' in result_text, f"Expected 'Success:' in result, got: {result_text}"
                assert 'success' in result_text, f"Expected backend response in result, got: {result_text}"
                
            except Exception as e:
                # If timeout or other error, capture what's actually in the result div
                result_text = result_div.text_content()
                pytest.fail(f"Button click did not produce expected result within 5 seconds. "
                          f"Result div contains: '{result_text}'. Error: {e}")
            
            browser.close()
            
    finally:
        # Clean up server
        server_process.terminate()
        server_process.wait()