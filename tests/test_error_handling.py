import pytest
from playwright.sync_api import sync_playwright
import subprocess
import time
import os

def test_frontend_error_handling():
    """Test that frontend shows error message when backend is not available"""
    
    # Start the server first to load the page
    server_process = subprocess.Popen(['python', 'app.py'], 
                                     cwd=os.path.dirname(os.path.dirname(__file__)))
    time.sleep(2)  # Give server time to start
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Navigate to the page while server is running
            page.goto('http://localhost:8002')
            
            # Check that button exists
            button = page.locator('#testButton')
            assert button.is_visible(), "Button should be visible"
            
            # Clear any previous result
            page.evaluate("document.getElementById('result').innerHTML = ''")
            
            # Stop the server
            server_process.terminate()
            server_process.wait()
            time.sleep(1)  # Wait for server to fully stop
            
            # Click the button (should now fail)
            button.click()
            
            # Wait for error message to appear
            try:
                page.wait_for_selector('#result:has-text("Error: Cannot connect")', timeout=5000)
                
                result_text = page.locator('#result').text_content()
                assert 'Error: Cannot connect to server' in result_text, \
                    f"Expected 'Error: Cannot connect to server' in result, got: {result_text}"
                
                print("✅ PASS: error handled")
                
            except Exception as e:
                result_text = page.locator('#result').text_content()
                pytest.fail(f"Frontend did not show expected error message. "
                          f"Result div contains: '{result_text}'. Error: {e}")
            
            browser.close()
            
    finally:
        # Clean up server if still running
        try:
            server_process.terminate()
            server_process.wait()
        except:
            pass

if __name__ == "__main__":
    test_frontend_error_handling()