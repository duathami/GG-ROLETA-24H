"""
Patch to handle imghdr removal in Python 3.13
"""
import sys
import os

# Add our custom imghdr to the path
sys.path.insert(0, os.path.dirname(__file__))

# Create fake imghdr module if needed
try:
    import imghdr
except ModuleNotFoundError:
    # Create a simple imghdr replacement
    class SimpleImghdr:
        @staticmethod
        def what(file, h=None):
            return None
    
    # Inject into modules
    sys.modules['imghdr'] = SimpleImghdr
