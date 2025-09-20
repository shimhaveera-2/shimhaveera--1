#!/usr/bin/env python3
"""
Debug script to understand why 640x640 resize parameters are empty
"""

# Test different resize configurations
test_configs = [
    {"type": "resize", "params": {"width": 400, "height": 400}},
    {"type": "resize", "params": {"width": 640, "height": 640}},
    {"type": "resize", "params": {"width": 751, "height": 751}},
    {"type": "resize", "params": {"width": 640, "height": 500}},
    {"type": "resize", "params": {"width": 500, "height": 640}},
]

print("=== TESTING RESIZE CONFIGURATIONS ===")
for i, config in enumerate(test_configs, 1):
    params = config["params"]
    width = params.get("width")
    height = params.get("height")
    
    print(f"\nTest {i}: {width}x{height}")
    print(f"  Config: {config}")
    print(f"  Params empty: {params == {}}")
    print(f"  Width: {width}, Height: {height}")
    
    # Check if it matches defaults
    from backend.core.transformation_config import RESIZE_WIDTH_DEFAULT, RESIZE_HEIGHT_DEFAULT
    is_default = (width == RESIZE_WIDTH_DEFAULT and height == RESIZE_HEIGHT_DEFAULT)
    print(f"  Matches defaults: {is_default}")
    
    # Simulate the logic from releases.py
    if width and height:
        print(f"  ✅ Would resize to: {width}x{height}")
    else:
        print(f"  ❌ Would keep original (no resize dimensions)")

print(f"\n=== DEFAULTS ===")
print(f"RESIZE_WIDTH_DEFAULT = {RESIZE_WIDTH_DEFAULT}")
print(f"RESIZE_HEIGHT_DEFAULT = {RESIZE_HEIGHT_DEFAULT}")