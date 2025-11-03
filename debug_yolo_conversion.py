#!/usr/bin/env python3

"""
🔍 DEBUG YOLO CONVERSION
Test YOLO conversion with transformed coordinates
"""

def test_yolo_conversion():
    print("🧮 TESTING YOLO CONVERSION")
    
    # Transformed coordinates from previous test
    x_min, y_min, x_max, y_max = 67.2, 13.8, 475.3, 466.2
    img_w, img_h = 500, 500
    
    print(f"📐 Input:")
    print(f"   BBox: ({x_min}, {y_min}, {x_max}, {y_max})")
    print(f"   Image: {img_w}x{img_h}")
    
    # YOLO conversion logic (from annotation_transformer.py)
    cx = (x_min + x_max) / 2.0 / img_w
    cy = (y_min + y_max) / 2.0 / img_h
    w  = (x_max - x_min) / img_w
    h  = (y_max - y_min) / img_h
    
    print(f"\n📊 YOLO Normalized:")
    print(f"   cx: {cx:.6f}")
    print(f"   cy: {cy:.6f}")
    print(f"   w:  {w:.6f}")
    print(f"   h:  {h:.6f}")
    
    # Check bounds (from annotation_transformer.py line 1304)
    valid = (0.0 <= cx <= 1.0 and 0.0 <= cy <= 1.0 and 0.0 < w <= 1.0 and 0.0 < h <= 1.0)
    
    print(f"\n✅ BOUNDS CHECK:")
    print(f"   cx in [0,1]: {0.0 <= cx <= 1.0} (cx={cx:.3f})")
    print(f"   cy in [0,1]: {0.0 <= cy <= 1.0} (cy={cy:.3f})")
    print(f"   w in (0,1]:  {0.0 < w <= 1.0} (w={w:.3f})")
    print(f"   h in (0,1]:  {0.0 < h <= 1.0} (h={h:.3f})")
    print(f"   📊 VALID: {valid}")
    
    if valid:
        yolo_line = f"12 {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}"
        print(f"   ✅ YOLO LINE: {yolo_line}")
    else:
        print(f"   ❌ WOULD BE DROPPED!")

if __name__ == "__main__":
    test_yolo_conversion()