#!/usr/bin/env python3

"""
🔍 DEBUG FLIP TRANSFORMATION
Test vertical flip + resize transformation manually
"""

def test_flip_transformation():
    print("🧮 TESTING FLIP + RESIZE TRANSFORMATION")
    
    # Original cat.jpg annotation from database
    original_bbox = (107.5, 40.5, 760.5, 583.5)
    original_dims = (800, 600)
    target_dims = (500, 500)
    
    print(f"📐 Original: BBox{original_bbox} on {original_dims}")
    
    # Step 1: Vertical Flip
    x_min, y_min, x_max, y_max = original_bbox
    current_width, current_height = original_dims
    
    print(f"\n🔄 STEP 1: Vertical Flip")
    print(f"   Before: y_min={y_min}, y_max={y_max}")
    
    # Vertical flip logic from annotation_transformer.py line 503
    y_min_flipped = current_height - y_max
    y_max_flipped = current_height - y_min
    
    print(f"   After:  y_min={y_min_flipped}, y_max={y_max_flipped}")
    
    flipped_bbox = (x_min, y_min_flipped, x_max, y_max_flipped)
    print(f"   Result: BBox{flipped_bbox}")
    
    # Step 2: Resize (stretch_to)
    print(f"\n📏 STEP 2: Resize {original_dims} → {target_dims}")
    
    x_min, y_min, x_max, y_max = flipped_bbox
    source_w, source_h = float(current_width), float(current_height)
    tw, th = float(target_dims[0]), float(target_dims[1])
    
    sx = tw / source_w  # 500/800 = 0.625
    sy = th / source_h  # 500/600 = 0.833
    
    print(f"   Scale factors: sx={sx:.3f}, sy={sy:.3f}")
    
    x_min_final = x_min * sx
    x_max_final = x_max * sx
    y_min_final = y_min * sy
    y_max_final = y_max * sy
    
    final_bbox = (x_min_final, y_min_final, x_max_final, y_max_final)
    print(f"   Final: BBox{final_bbox}")
    
    # Check bounds
    print(f"\n✅ BOUNDS CHECK:")
    print(f"   Target canvas: {target_dims}")
    print(f"   x_min: {x_min_final:.1f} (valid: {0 <= x_min_final <= target_dims[0]})")
    print(f"   y_min: {y_min_final:.1f} (valid: {0 <= y_min_final <= target_dims[1]})")
    print(f"   x_max: {x_max_final:.1f} (valid: {0 <= x_max_final <= target_dims[0]})")
    print(f"   y_max: {y_max_final:.1f} (valid: {0 <= y_max_final <= target_dims[1]})")
    
    # Check if bbox is valid
    valid = (x_min_final < x_max_final and y_min_final < y_max_final and
             x_min_final >= 0 and y_min_final >= 0 and
             x_max_final <= target_dims[0] and y_max_final <= target_dims[1])
    
    print(f"   📊 BBOX VALID: {valid}")
    
    if not valid:
        print("   ❌ BBOX WOULD BE DROPPED!")
    else:
        print("   ✅ BBOX SHOULD BE KEPT!")

if __name__ == "__main__":
    test_flip_transformation()