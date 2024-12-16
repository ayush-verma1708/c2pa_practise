import subprocess
import json

def embed_c2pa_metadata(image_path, manifest_path, output_path):
    """
    Embed C2PA metadata into an image.

    Args:
        image_path (str): Path to the input image file.
        manifest_path (str): Path to the manifest JSON file containing metadata.
        output_path (str): Path where the output image will be saved.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Path to the `c2patool` executable
    c2pa_tool_path = "./c2patool.exe"  # Update with the correct path to `c2patool`

    # Validate the manifest JSON file
    try:
        with open(manifest_path, "r") as f:
            manifest_data = json.load(f)
            print("Manifest file loaded successfully:")
            print(json.dumps(manifest_data, indent=4))
    except Exception as e:
        print(f"Failed to load manifest.json: {e}")
        return False

    try:
        # Run the c2patool command to embed metadata
        result = subprocess.run(
            [
                c2pa_tool_path,
                image_path,
                "-m", manifest_path,
                "-o", output_path
            ],
            capture_output=True,
            text=True
        )

        # Check if the process succeeded
        if result.returncode == 0:
            print("C2PA metadata embedded successfully!")
            return True
        else:
            print(f"Error: {result.stderr}")
            return False

    except FileNotFoundError:
        print("Error: c2patool not found. Make sure it's installed and in your PATH.")
        return False

# Example usage
if __name__ == "__main__":
    # Path to the input image
    image_path = "example.jpg"
    # Path to the manifest JSON file
    manifest_path = "manifest.json"
    # Path for the output image
    output_path = "example_with_c2pa1.jpg"

    # Embed C2PA metadata
    success = embed_c2pa_metadata(image_path, manifest_path, output_path)

    if success:
        print(f"Output image saved to {output_path}")
    else:
        print("Failed to embed metadata.")
