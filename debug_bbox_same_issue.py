#!/usr/bin/env python3

import sys
import os
sys.path.append('/workspace/project/simha--2/backend')

from core.annotation_transformer import update_annotations_for_transformations, BoundingBox

def debug_bbox_same_issue():
    """Test bounding boxes with your exact scenario"""
    
    print("🚨 TESTING BOUNDING BOXES - SAME COORDINATES BUG")
    print("=" * 60)
    
    # Test bounding box
    test_bbox = BoundingBox(
        x_min=100, y_min=100, x_max=200, y_max=200,
        class_name="test", class_id=1, confidence=1.0
    )
    
    print(f"📍 ORIGINAL: 640x640 image")
    print(f"📍 BBOX: [{test_bbox.x_min}, {test_bbox.y_min}, {test_bbox.x_max}, {test_bbox.y_max}]")
    print()
    
    # Test with same dimensions (your scenario)
    modes_to_test = ['stretch_to', 'fit_within', 'fill_center_crop', 'fit_reflect_edges', 'fit_black_edges', 'fit_white_edges']
    
    print("🧪 TESTING ALL 6 MODES (640x640 → 640x640):")
    for mode in modes_to_test:
        transformation_config = {
            'resize': {
                'resize_mode': mode,
                'width': 640,
                'height': 640,
                'enabled': True
            }
        }
        
        result = update_annotations_for_transformations(
            [test_bbox], 
            transformation_config, 
            original_dims=(640, 640),
            new_dims=(640, 640),
            debug_tracking=False
        )
        
        if result and len(result) > 0:
            bbox = [result[0].x_min, result[0].y_min, result[0].x_max, result[0].y_max]
            print(f"  {mode:18}: {bbox}")
        else:
            print(f"  {mode:18}: FAILED")
    
    print()
    print("🧪 TESTING WITH DIFFERENT DIMENSIONS (640x640 → 800x600):")
    for mode in modes_to_test:
        transformation_config = {
            'resize': {
                'resize_mode': mode,
                'width': 800,
                'height': 600,
                'enabled': True
            }
        }
        
        result = update_annotations_for_transformations(
            [test_bbox], 
            transformation_config, 
            original_dims=(640, 640),
            new_dims=(800, 600),
            debug_tracking=False
        )
        
        if result and len(result) > 0:
            bbox = [result[0].x_min, result[0].y_min, result[0].x_max, result[0].y_max]
            print(f"  {mode:18}: {bbox}")
        else:
            print(f"  {mode:18}: FAILED")
    
    print()
    print("🔍 ANALYSIS:")
    print("- Same dimensions: All modes should be IDENTICAL (expected)")
    print("- Different dimensions: Modes should be DIFFERENT")
    print("- If all modes identical in both cases → BUG CONFIRMED")

if __name__ == "__main__":
    debug_bbox_same_issue()