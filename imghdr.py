"""
Replacement for imghdr module removed in Python 3.13
"""
import os

def what(file, h=None):
    if h is None:
        with open(file, 'rb') as f:
            h = f.read(32)
    if not h:
        return None
    
    # Simple image type detection
    if h.startswith(b'\xff\xd8\xff'):
        return 'jpeg'
    elif h.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    elif h.startswith(b'GIF87a') or h.startswith(b'GIF89a'):
        return 'gif'
    elif h.startswith(b'BM'):
        return 'bmp'
    elif h.startswith(b'RIFF') and h[8:12] == b'WEBP':
        return 'webp'
    return None
