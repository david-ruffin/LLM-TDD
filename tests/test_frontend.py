import pytest
from playwright.sync_api import sync_playwright
import subprocess
import time
import os

def test_button_click_handler():
    """Test that button has click handler with HTTP request capability"""
    
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
            
            # Set up console log monitoring
            console_messages = []
            page.on('console', lambda msg: console_messages.append(msg.text))
            
            # Set up network request monitoring
            network_requests = []
            page.on('request', lambda request: network_requests.append(request.url))
            
            # Click the button
            button.click()
            
            # Wait a moment for JavaScript to execute
            time.sleep(1)
            
            # Check that 'Request sent' was logged to console
            assert any('Request sent' in msg for msg in console_messages), \
                f"Expected 'Request sent' in console, got: {console_messages}"
            
            # Check that an HTTP request was made
            assert any('api' in url for url in network_requests), \
                f"Expected API request in network tab, got: {network_requests}"
            
            browser.close()
            
    finally:
        # Clean up server
        server_process.terminate()
        server_process.wait()