#!/usr/bin/env python3

import sys
import os
sys.path.append('/workspace/project/simha--2/backend')

from core.annotation_transformer import update_annotations_for_transformations, BoundingBox, Polygon

def debug_different_dimensions():
    """Test with different target dimensions to see if that reveals the bug"""
    
    print("🚨 TESTING WITH DIFFERENT TARGET DIMENSIONS")
    print("=" * 60)
    
    # Simple test polygon (square)
    test_points = [(100, 100), (200, 100), (200, 200), (100, 200)]
    test_polygon = Polygon(points=test_points, class_name="test", class_id=1, confidence=1.0)
    
    print(f"📍 ORIGINAL: 300x300 image")
    print(f"📍 POLYGON: {test_points}")
    print()
    
    # Test different target dimensions
    test_cases = [
        ("Same size", 300, 300),
        ("Wider", 600, 300),
        ("Taller", 300, 600),
        ("Different aspect", 400, 200)
    ]
    
    modes_to_test = ['stretch_to', 'fit_within']
    
    for case_name, target_w, target_h in test_cases:
        print(f"🎯 TARGET: {case_name} ({target_w}x{target_h})")
        
        for mode in modes_to_test:
            transformation_config = {
                'resize': {
                    'resize_mode': mode,
                    'width': target_w,
                    'height': target_h,
                    'enabled': True
                }
            }
            
            result = update_annotations_for_transformations(
                [test_polygon], 
                transformation_config, 
                original_dims=(300, 300),
                new_dims=(target_w, target_h),
                debug_tracking=False
            )
            
            if result and len(result) > 0:
                first_point = result[0].points[0]
                print(f"  {mode:12}: {first_point}")
            else:
                print(f"  {mode:12}: FAILED")
        
        print()
    
    print("🔍 ANALYSIS:")
    print("- If stretch_to and fit_within show SAME results for all cases → BUG")
    print("- If they show DIFFERENT results → Working correctly")

if __name__ == "__main__":
    debug_different_dimensions()