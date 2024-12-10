<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Image Encryption and Decryption Tool</h1>
    <h2>Overview</h2>
    <p>This tool provides a user-friendly way to encrypt and decrypt images using pixel-level manipulation. It employs mathematical operations and pixel swapping to ensure image data is protected. The project showcases how encryption techniques can be applied to image files, combining simplicity with robust functionality.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Image Encryption:</strong> Applies a mathematical operation (XOR) to modify pixel values for encrypting images.</li>
        <li><strong>Image Decryption:</strong> Reverses the encryption process to restore the original image.</li>
        <li><strong>Interactive Interface:</strong> A graphical interface allows users to easily select input images, specify encryption keys, and view the output.</li>
        <li><strong>Cross-Platform Support:</strong> Works seamlessly on various operating systems with Python and required libraries installed.</li>
    </ul>
    <h2>How It Works</h2>
    <ol>
        <li>The user selects an image file through a dialog window.</li>
        <li>A unique encryption key is provided by the user.</li>
        <li>The image undergoes XOR-based encryption and pixel swapping to produce an encrypted version.</li>
        <li>The encrypted image can be decrypted back using the same key, ensuring security and reversibility.</li>
    </ol>
    <h2>Technologies Used</h2>
    <ul>
        <li>Python (Pillow and NumPy libraries for image processing)</li>
        <li>PyQt5 (for GUI design)</li>
    </ul>
    <h2>Learning Outcomes</h2>
    <p>This task provided insights into:</p>
    <ul>
        <li>Implementing pixel-level data manipulation in images.</li>
        <li>Designing an interactive and functional GUI for user input.</li>
        <li>Applying mathematical operations to ensure data security.</li>
    </ul>
    <h2>Instructions to Run</h2>
    <ol>
        <li>Install required libraries:
            <pre><code>pip install pillow numpy pyqt5</code></pre>
        </li>
        <li>Run the main script:
            <pre><code>python task_02.py</code></pre>
        </li>
        <li>Follow the on-screen prompts to encrypt or decrypt an image.</li>
    </ol>
    <h2>Conclusion</h2>
    <p>This project demonstrates a practical implementation of encryption and decryption, blending mathematical operations with user interface design for real-world applications.</p>

</body>
</html>
