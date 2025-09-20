#!/usr/bin/env python3

import sys
import os
sys.path.append('/workspace/project/simha--2/backend')

from core.annotation_transformer import update_annotations_for_transformations, BoundingBox, Polygon

def debug_your_exact_data():
    """Test with your exact polygon data to see the bug"""
    
    print("🚨 TESTING WITH YOUR EXACT DATA")
    print("=" * 60)
    
    # Your exact polygon data (class 1 - car shape)
    car_points = [
        (0.169375*640, 0.997500*640), (0.165625*640, 0.944167*640), (0.168125*640, 0.880833*640),
        (0.188125*640, 0.767500*640), (0.218125*640, 0.680833*640), (0.244375*640, 0.615833*640),
        (0.258125*640, 0.574167*640), (0.256875*640, 0.532500*640), (0.283125*640, 0.499167*640),
        (0.315625*640, 0.464167*640), (0.343125*640, 0.420833*640), (0.364375*640, 0.387500*640),
        (0.376875*640, 0.372500*640), (0.390625*640, 0.357500*640), (0.406875*640, 0.287500*640),
        (0.428125*640, 0.237500*640), (0.439375*640, 0.220833*640), (0.466875*640, 0.215833*640),
        (0.515625*640, 0.270833*640), (0.549375*640, 0.347500*640), (0.566875*640, 0.345833*640),
        (0.580625*640, 0.329167*640), (0.590625*640, 0.297500*640), (0.596875*640, 0.272500*640),
        (0.611875*640, 0.232500*640), (0.644375*640, 0.184167*640), (0.683125*640, 0.180833*640),
        (0.681875*640, 0.235833*640), (0.680625*640, 0.315833*640), (0.670625*640, 0.369167*640),
        (0.676875*640, 0.392500*640), (0.706875*640, 0.425833*640), (0.726875*640, 0.482500*640),
        (0.725625*640, 0.530833*640), (0.739375*640, 0.572500*640), (0.743125*640, 0.652500*640),
        (0.714375*640, 0.677500*640), (0.664375*640, 0.680833*640), (0.629375*640, 0.680833*640),
        (0.606875*640, 0.685833*640), (0.559375*640, 0.715833*640), (0.573125*640, 0.764167*640),
        (0.579375*640, 0.789167*640), (0.583125*640, 0.820833*640), (0.583125*640, 0.850833*640),
        (0.598125*640, 0.907500*640), (0.604375*640, 0.939167*640), (0.606875*640, 0.972500*640),
        (0.601875*640, 0.995833*640)
    ]
    
    # Your small object (class 15)
    small_points = [
        (0.568125*640, 0.515833*640), (0.570625*640, 0.500833*640), (0.595625*640, 0.480833*640),
        (0.626875*640, 0.490833*640), (0.628125*640, 0.512500*640), (0.615625*640, 0.540833*640),
        (0.585625*640, 0.540833*640)
    ]
    
    # Create polygon annotations
    car_polygon = Polygon(points=car_points, class_name="car", class_id=1, confidence=1.0)
    small_polygon = Polygon(points=small_points, class_name="object", class_id=15, confidence=1.0)
    
    print(f"📍 ORIGINAL IMAGE: 640x640")
    print(f"📍 CAR POLYGON: {len(car_points)} points")
    print(f"📍 SMALL POLYGON: {len(small_points)} points")
    print()
    
    # Test the two modes that should be DIFFERENT
    modes_to_test = ['stretch_to', 'fit_within']
    
    for mode in modes_to_test:
        print(f"🧪 Testing {mode}:")
        
        transformation_config = {
            'resize': {
                'resize_mode': mode,
                'width': 640,  # Same size to isolate the bug
                'height': 640,
                'enabled': True
            }
            # No rotation to isolate resize bug
        }
        
        # Test car polygon
        car_result = update_annotations_for_transformations(
            [car_polygon], 
            transformation_config, 
            original_dims=(640, 640),
            new_dims=(640, 640),
            debug_tracking=False
        )
        
        if car_result and len(car_result) > 0:
            # Show first 3 points
            first_points = car_result[0].points[:3]
            print(f"  🚗 Car first 3 points: {first_points}")
        else:
            print(f"  🚗 Car: FAILED")
        
        # Test small polygon  
        small_result = update_annotations_for_transformations(
            [small_polygon], 
            transformation_config, 
            original_dims=(640, 640),
            new_dims=(640, 640),
            debug_tracking=False
        )
        
        if small_result and len(small_result) > 0:
            first_points = small_result[0].points[:3]
            print(f"  📦 Small first 3 points: {first_points}")
        else:
            print(f"  📦 Small: FAILED")
        
        print()
    
    print("🔍 EXPECTED:")
    print("- stretch_to and fit_within should show DIFFERENT coordinates")
    print("- If they're the same → BUG CONFIRMED in annotation transformer")

if __name__ == "__main__":
    debug_your_exact_data()