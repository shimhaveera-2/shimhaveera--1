#!/usr/bin/env python3

print("🔍 COORDINATE COMPARISON ANALYSIS")
print("=" * 50)

# What I'm getting in my tests
stretch_to_backend = [310.0, 140.0, 490.0, 460.0]
fit_within_backend = [210.0, 180.0, 390.0, 420.0]

# Convert to YOLO format (normalized)
def to_yolo(bbox, img_width, img_height):
    x_min, y_min, x_max, y_max = bbox
    center_x = (x_min + x_max) / 2 / img_width
    center_y = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height
    return [center_x, center_y, width, height]

stretch_to_yolo = to_yolo(stretch_to_backend, 800, 600)
fit_within_yolo = to_yolo(fit_within_backend, 800, 600)

print("🧪 MY TEST RESULTS:")
print(f"stretch_to: {stretch_to_yolo}")
print(f"fit_within:  {fit_within_yolo}")
print()

print("❓ WHAT ARE YOU SEEING IN YOUR label.txt?")
print("Please check your actual label.txt files and tell me:")
print("1. What coordinates do you see for stretch_to?")
print("2. What coordinates do you see for fit_within?")
print("3. Are they exactly the same or different?")
print()

print("🔍 POSSIBLE REASONS FOR MISMATCH:")
print("1. Different input annotation coordinates")
print("2. Different transformation parameters")
print("3. Bug in label.txt export process")
print("4. UI uses different transformation than backend")
print()

print("📋 TO DEBUG:")
print("1. Share your actual label.txt coordinates")
print("2. Tell me your original annotation coordinates")
print("3. Tell me your transformation parameters (width, height, angle)")