#!/usr/bin/env python3

# Quick test to verify resize math
def test_fit_black_edges_math():
    print("🧮 TESTING fit_black_edges MATH")
    
    # Test case from debug log: (800, 600) → (500, 500)
    source_w, source_h = 800, 600
    tw, th = 500, 500
    
    print(f"📐 Input: ({source_w}, {source_h}) → ({tw}, {th})")
    
    # Calculate scale factor
    s = min(tw / source_w, th / source_h)
    print(f"🔢 Scale factor: s = min({tw}/{source_w}, {th}/{source_h}) = min({tw/source_w:.3f}, {th/source_h:.3f}) = {s:.3f}")
    
    # Calculate scaled dimensions
    sw = source_w * s
    sh = source_h * s
    print(f"📏 Scaled size: ({sw:.1f}, {sh:.1f})")
    
    # Calculate padding
    pad_x = int(round((tw - sw) / 2.0))
    pad_y = int(round((th - sh) / 2.0))
    print(f"🎯 Padding: pad_x = {pad_x}, pad_y = {pad_y}")
    
    # Test with a sample bbox that should result in the debug output
    # We need to reverse-engineer what the original bbox was
    # From debug: BBox(107.50, 40.50, 760.50, 583.50)
    # This means: x_min * s + pad_x = 107.50, etc.
    
    result_x_min, result_y_min = 107.50, 40.50
    result_x_max, result_y_max = 760.50, 583.50
    
    # Reverse calculate original coordinates
    orig_x_min = (result_x_min - pad_x) / s
    orig_y_min = (result_y_min - pad_y) / s
    orig_x_max = (result_x_max - pad_x) / s
    orig_y_max = (result_y_max - pad_y) / s
    
    print(f"\n🔍 REVERSE CALCULATION:")
    print(f"   Result bbox: ({result_x_min}, {result_y_min}, {result_x_max}, {result_y_max})")
    print(f"   Original bbox should be: ({orig_x_min:.1f}, {orig_y_min:.1f}, {orig_x_max:.1f}, {orig_y_max:.1f})")
    
    # Forward calculate to verify
    calc_x_min = orig_x_min * s + pad_x
    calc_y_min = orig_y_min * s + pad_y
    calc_x_max = orig_x_max * s + pad_x
    calc_y_max = orig_y_max * s + pad_y
    
    print(f"\n✅ FORWARD VERIFICATION:")
    print(f"   Calculated: ({calc_x_min:.1f}, {calc_y_min:.1f}, {calc_x_max:.1f}, {calc_y_max:.1f})")
    print(f"   Expected:   ({result_x_min}, {result_y_min}, {result_x_max}, {result_y_max})")
    print(f"   Match: {abs(calc_x_min - result_x_min) < 0.1 and abs(calc_y_min - result_y_min) < 0.1}")

if __name__ == "__main__":
    test_fit_black_edges_math()