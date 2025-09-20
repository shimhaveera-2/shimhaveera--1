#!/usr/bin/env python3

"""
🔍 DEBUG ANNOTATION TRANSFORMER
Test the update_annotations_for_transformations function directly
"""

import sys
import os
sys.path.append('/workspace/project/shimhaveera--1')
sys.path.append('/workspace/project/shimhaveera--1/backend')

# Set up the environment
os.chdir('/workspace/project/shimhaveera--1')

from core.annotation_transformer import update_annotations_for_transformations, BoundingBox

def test_flip_resize_transformation():
    print("🧮 TESTING update_annotations_for_transformations")
    
    # Create test annotation (cat.jpg from database)
    test_bbox = BoundingBox(
        x_min=107.5,
        y_min=40.5, 
        x_max=760.5,
        y_max=583.5,
        class_name="cat",
        class_id=12
    )
    
    annotations = [test_bbox]
    
    # Test configuration (flip + resize)
    transformation_config = {
        'flip': {'enabled': True, 'vertical': True},
        'resize': {'enabled': True, 'width': 500, 'height': 500}
    }
    
    original_dims = (800, 600)
    new_dims = (500, 500)
    
    print(f"📐 Input:")
    print(f"   Annotation: BBox({test_bbox.x_min}, {test_bbox.y_min}, {test_bbox.x_max}, {test_bbox.y_max})")
    print(f"   Original dims: {original_dims}")
    print(f"   New dims: {new_dims}")
    print(f"   Transformations: {list(transformation_config.keys())}")
    
    # Call the function
    try:
        transformed_annotations, debug_info = update_annotations_for_transformations(
            annotations=annotations,
            transformation_config=transformation_config,
            original_dims=original_dims,
            new_dims=new_dims,
            affine_matrix=None,
            debug_tracking=True
        )
        
        print(f"\n✅ TRANSFORMATION RESULT:")
        print(f"   Input count: {len(annotations)}")
        print(f"   Output count: {len(transformed_annotations)}")
        
        if transformed_annotations:
            for i, ann in enumerate(transformed_annotations):
                print(f"   Ann {i+1}: BBox({ann.x_min:.1f}, {ann.y_min:.1f}, {ann.x_max:.1f}, {ann.y_max:.1f})")
        else:
            print("   ❌ NO ANNOTATIONS RETURNED!")
            
        print(f"\n🔍 DEBUG INFO:")
        if debug_info:
            print(f"   Keys: {list(debug_info.keys())}")
            if 'annotation_steps' in debug_info:
                print(f"   Annotation steps: {len(debug_info['annotation_steps'])}")
                for i, step in enumerate(debug_info['annotation_steps']):
                    print(f"     Step {i+1}: {step.get('transformation_method', 'unknown')}")
                    if 'transformation_steps' in step:
                        print(f"       Sub-steps: {len(step['transformation_steps'])}")
        
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_flip_resize_transformation()