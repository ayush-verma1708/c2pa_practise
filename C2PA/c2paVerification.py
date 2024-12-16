import subprocess

def verify_c2pa_metadata(image_path):
    """
    Verify the C2PA metadata embedded in an image.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        bool: True if verification is successful, False otherwise.
    """
    # Path to the `c2patool` executable
    c2pa_tool_path = "c2patool"  # Adjust this if c2patool is not in your PATH

    try:
        # Run the c2patool command to check the C2PA metadata
        result = subprocess.run(
            [
                c2pa_tool_path,
                image_path,
                "--info"  # Option to display the metadata info
            ],
            capture_output=True,
            text=True
        )

        # Check if the process succeeded
        if result.returncode == 0:
            print("C2PA metadata verification successful!")
            print("Verification Info:")
            print(result.stdout)
            return True
        else:
            print(f"Error: {result.stderr}")
            return False

    except FileNotFoundError:
        print("Error: c2patool not found. Make sure it's installed and in your PATH.")
        return False

# Example usage
if __name__ == "__main__":
    # Path to the image with embedded C2PA metadata
    # image_path = "example.jpg"  # Path of original file without C2PA metadata
    # image_path = "example_with_c2pa1.jpg"  # Path of file with C2PA metadata
    image_path = "example_with_c2pa2.jpg"  # Path of image modified by Paint , this should reflect the changes made in the image

    # Verify C2PA metadata
    success = verify_c2pa_metadata(image_path)

    if success:
        print("Verification Completed.")
    else:
        print("Verification failed.")
