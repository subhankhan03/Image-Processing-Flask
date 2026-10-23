from process_image import convert_to_grayscale, adjust_brightness
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    output_filename = None
    if request.method == "POST":
        image = request.files["image"]
        image.save("uploads/" + image.filename)
        print("Image saved successfully!")

        operation = request.form.get("operation", "grayscale")
        factor = float(request.form.get("factor", 1.5))

        if operation == "grayscale":
            output_filename = "grayscale_" + image.filename
            output_path = "processed/" + output_filename

            convert_to_grayscale(
            "uploads/" + image.filename,
            output_path
        )

        elif operation == "brightness":
            output_filename = "brightness_" + image.filename
            output_path = "processed/" + output_filename

            adjust_brightness(
                "uploads/" + image.filename,
                output_path,
                factor
            )

    return render_template(
    "index.html",
    output_filename=output_filename
    )
@app.route("/processed/<filename>")
def show_processed(filename):
    return send_from_directory("processed", filename)
if __name__ == "__main__":
    app.run(debug=True)