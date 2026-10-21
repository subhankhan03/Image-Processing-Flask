from process_image import convert_to_grayscale
from flask import Flask, render_template, request 
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        image = request.files["image"]
        image.save("uploads/" + image.filename)
        print("Image saved successfully!")
        output_path = "processed/grayscale_" + image.filename

        convert_to_grayscale(
        "uploads/" + image.filename,
        output_path
        )

        print("Grayscale image created:", output_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)