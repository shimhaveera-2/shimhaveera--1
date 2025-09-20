#!/usr/bin/env python3

import sys
import os
sys.path.append('/workspace/project/simha--2/backend')

from core.annotation_transformer import update_annotations_for_transformations, BoundingBox

def debug_coordinate_mismatch():
    """Debug why label.txt shows same coordinates but UI shows different"""
    
    print("🚨 DEBUGGING COORDINATE MISMATCH")
    print("=" * 60)
    
    # Test annotation - same as before
    test_annotation = BoundingBox(
        x_min=300, y_min=350, x_max=700, y_max=650,
        class_name="test", class_id=1, confidence=1.0
    )
    
    print(f"📍 ORIGINAL: [{test_annotation.x_min}, {test_annotation.y_min}, {test_annotation.x_max}, {test_annotation.y_max}]")
    print()
    
    # Test the two modes that should be DIFFERENT
    modes_to_compare = ['stretch_to', 'fit_within']
    
    for mode in modes_to_compare:
        print(f"🧪 Testing {mode}:")
        
        transformation_config = {
            'resize': {
                'resize_mode': mode,
                'width': 800,
                'height': 600,
                'enabled': True
            },
            'rotation': {
                'angle': 90,
                'enabled': True
            }
        }
        
        # Call annotation transformer (what gets saved to label.txt)
        result = update_annotations_for_transformations(
            [test_annotation], 
            transformation_config, 
            original_dims=(1000, 1000),
            new_dims=(800, 600),
            debug_tracking=False
        )
        
        if result and len(result) > 0:
            bbox = [result[0].x_min, result[0].y_min, result[0].x_max, result[0].y_max]
            print(f"  📝 Backend Result (label.txt): {bbox}")
            
            # Convert to YOLO format (what actually gets saved)
            center_x = (result[0].x_min + result[0].x_max) / 2 / 800  # Normalize by new width
            center_y = (result[0].y_min + result[0].y_max) / 2 / 600  # Normalize by new height  
            width = (result[0].x_max - result[0].x_min) / 800
            height = (result[0].y_max - result[0].y_min) / 600
            
            print(f"  📄 YOLO Format: [{center_x:.6f}, {center_y:.6f}, {width:.6f}, {height:.6f}]")
        else:
            print(f"  ❌ Backend Result: FAILED")
        
        print()
    
    print("🔍 ANALYSIS:")
    print("- If both modes show SAME coordinates → Backend annotation transformer is broken")
    print("- If UI shows DIFFERENT results → Frontend uses different transformation system")
    print("- Need to find where UI display transformations happen!")

if __name__ == "__main__":
    debug_coordinate_mismatch()