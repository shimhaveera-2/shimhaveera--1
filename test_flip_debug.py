#!/usr/bin/env python3

"""
🔍 TEST FLIP DEBUG
Create a release with flip transformation to see debug output
"""

import requests
import json

def test_flip_release():
    print("🧮 TESTING FLIP RELEASE CREATION")
    
    # Release configuration with flip transformation
    release_config = {
        "project_id": 1,
        "version_name": "v1.0",
        "dataset_ids": ["1c62d270-2df3-4568-986d-0cff06cd7e7d"],
        "name": "flip-debug-test-2",
        "description": "Debug test for flip transformations",
        "train_split": 0.7,
        "val_split": 0.2,
        "test_split": 0.1,
        "output_format": "yolo",
        "task_type": "detection",
        "augmentation_config": {
            "enabled": True,
            "num_augmentations_per_image": 1,
            "transformations": {
                "flip": {
                    "enabled": True,
                    "vertical": True
                },
                "resize": {
                    "enabled": True,
                    "width": 500,
                    "height": 500
                }
            }
        }
    }
    
    print(f"📊 Release config:")
    print(f"   Transformations: {list(release_config['augmentation_config']['transformations'].keys())}")
    print(f"   Flip vertical: {release_config['augmentation_config']['transformations']['flip']['vertical']}")
    
    # Create release
    try:
        response = requests.post(
            "http://localhost:12000/api/v1/releases/create",
            json=release_config,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Release created successfully!")
            print(f"   Release ID: {result.get('release_id')}")
            print(f"   Status: {result.get('status')}")
            if 'download_url' in result:
                print(f"   Download URL: {result['download_url']}")
        else:
            print(f"❌ Release creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_flip_release()