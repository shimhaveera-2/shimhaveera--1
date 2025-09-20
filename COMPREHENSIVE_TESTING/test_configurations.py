#!/usr/bin/env python3
"""
🧪 COMPREHENSIVE TESTING CONFIGURATIONS
Test scenarios for transformation tools and resize modes
"""

# Test configurations for different scenarios
TEST_CONFIGURATIONS = {
    
    # ========================================
    # RESIZE MODE TESTING
    # ========================================
    "resize_mode_stretch": {
        "name": "Resize Mode: Stretch",
        "description": "Test stretch resize mode with simple resize",
        "transformations": {
            "resize": {
                "width": 1113,
                "height": 760,
                "mode": "stretch"
            }
        },
        "expected_result": "Different aspect ratio, coordinates should reflect stretching"
    },
    
    "resize_mode_fit_black": {
        "name": "Resize Mode: Fit with Black Edges", 
        "description": "Test fit_black_edges resize mode",
        "transformations": {
            "resize": {
                "width": 1113,
                "height": 760,
                "mode": "fit_black_edges"
            }
        },
        "expected_result": "Maintain aspect ratio with black padding, coordinates adjusted for padding"
    },
    
    "resize_mode_fill_crop": {
        "name": "Resize Mode: Fill Center Crop",
        "description": "Test fill_center_crop resize mode", 
        "transformations": {
            "resize": {
                "width": 1113,
                "height": 760,
                "mode": "fill_center_crop"
            }
        },
        "expected_result": "Fill dimensions by cropping, coordinates reflect cropped area"
    },
    
    # ========================================
    # SINGLE TRANSFORMATION TESTING
    # ========================================
    "rotation_90": {
        "name": "Rotation: 90 degrees",
        "description": "Test 90-degree clockwise rotation",
        "transformations": {
            "rotate": {
                "angle": 90,
                "expand": True
            }
        },
        "expected_result": "Image rotated 90° clockwise, coordinates transformed accordingly"
    },
    
    "rotation_180": {
        "name": "Rotation: 180 degrees", 
        "description": "Test 180-degree rotation",
        "transformations": {
            "rotate": {
                "angle": 180,
                "expand": True
            }
        },
        "expected_result": "Image upside down, coordinates flipped both axes"
    },
    
    "rotation_custom": {
        "name": "Rotation: Custom 45 degrees",
        "description": "Test custom 45-degree rotation",
        "transformations": {
            "rotate": {
                "angle": 45,
                "expand": True
            }
        },
        "expected_result": "Image rotated 45°, expanded canvas, coordinates transformed"
    },
    
    "flip_horizontal": {
        "name": "Flip: Horizontal",
        "description": "Test horizontal flip",
        "transformations": {
            "flip": {
                "direction": "horizontal"
            }
        },
        "expected_result": "Image mirrored horizontally, x-coordinates flipped"
    },
    
    "flip_vertical": {
        "name": "Flip: Vertical", 
        "description": "Test vertical flip",
        "transformations": {
            "flip": {
                "direction": "vertical"
            }
        },
        "expected_result": "Image mirrored vertically, y-coordinates flipped"
    },
    
    "crop_center": {
        "name": "Crop: Center Region",
        "description": "Test center crop",
        "transformations": {
            "crop": {
                "x": 200,
                "y": 150, 
                "width": 400,
                "height": 300
            }
        },
        "expected_result": "Center region extracted, coordinates adjusted to new origin"
    },
    
    "crop_corner": {
        "name": "Crop: Top-Left Corner",
        "description": "Test corner crop",
        "transformations": {
            "crop": {
                "x": 0,
                "y": 0,
                "width": 400, 
                "height": 300
            }
        },
        "expected_result": "Top-left corner extracted, some annotations may be outside crop area"
    },
    
    # ========================================
    # COMBINATION TESTING
    # ========================================
    "combo_resize_rotate": {
        "name": "Combo: Resize + Rotate",
        "description": "Test resize followed by rotation",
        "transformations": {
            "resize": {
                "width": 640,
                "height": 480,
                "mode": "stretch"
            },
            "rotate": {
                "angle": 90,
                "expand": True
            }
        },
        "expected_result": "First resized then rotated, coordinates undergo both transformations"
    },
    
    "combo_flip_crop": {
        "name": "Combo: Flip + Crop",
        "description": "Test flip followed by crop",
        "transformations": {
            "flip": {
                "direction": "horizontal"
            },
            "crop": {
                "x": 100,
                "y": 100,
                "width": 600,
                "height": 400
            }
        },
        "expected_result": "First flipped then cropped, coordinates transformed in sequence"
    },
    
    "combo_complex": {
        "name": "Combo: Complex Multi-Transform",
        "description": "Test multiple transformations in sequence",
        "transformations": {
            "resize": {
                "width": 1024,
                "height": 768,
                "mode": "fit_black_edges"
            },
            "rotate": {
                "angle": 45,
                "expand": True
            },
            "flip": {
                "direction": "horizontal"
            }
        },
        "expected_result": "Complex transformation sequence, coordinates undergo all transformations"
    },
    
    # ========================================
    # EDGE CASE TESTING
    # ========================================
    "edge_tiny_resize": {
        "name": "Edge Case: Tiny Resize",
        "description": "Test very small resize dimensions",
        "transformations": {
            "resize": {
                "width": 64,
                "height": 64,
                "mode": "stretch"
            }
        },
        "expected_result": "Very small image, coordinates scaled down significantly"
    },
    
    "edge_large_resize": {
        "name": "Edge Case: Large Resize", 
        "description": "Test very large resize dimensions",
        "transformations": {
            "resize": {
                "width": 2048,
                "height": 1536,
                "mode": "stretch"
            }
        },
        "expected_result": "Large image, coordinates scaled up significantly"
    },
    
    "edge_360_rotation": {
        "name": "Edge Case: 360° Rotation",
        "description": "Test full 360-degree rotation (should be identity)",
        "transformations": {
            "rotate": {
                "angle": 360,
                "expand": False
            }
        },
        "expected_result": "Should be identical to original (360° = 0°)"
    }
}

# Test images to use for each configuration
TEST_IMAGES = [
    "test_geometric_800x600.jpg",
    "test_grid_1024x768.jpg", 
    "test_small_400x300.jpg"
]

# Export formats to test
EXPORT_FORMATS = [
    "yolo_detection",
    "yolo_segmentation"
]

def get_test_matrix():
    """Generate complete test matrix"""
    test_matrix = []
    
    for config_name, config in TEST_CONFIGURATIONS.items():
        for image in TEST_IMAGES:
            for format_type in EXPORT_FORMATS:
                test_matrix.append({
                    "config_name": config_name,
                    "config": config,
                    "image": image,
                    "format": format_type,
                    "test_id": f"{config_name}_{image.split('.')[0]}_{format_type}"
                })
    
    return test_matrix

if __name__ == "__main__":
    matrix = get_test_matrix()
    print(f"🧪 Total test scenarios: {len(matrix)}")
    print(f"📊 Configurations: {len(TEST_CONFIGURATIONS)}")
    print(f"🖼️ Images: {len(TEST_IMAGES)}")
    print(f"📝 Formats: {len(EXPORT_FORMATS)}")