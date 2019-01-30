from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
body {
    font-family: arial;
}

.slidecontainer {
    width: 100%;
}

.slider {
    -webkit-appearance: none;
    width: 500px;
    height: 10px;
    margin: 10px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
}

.slider:hover {
    opacity: 1;
}

.slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    cursor: pointer;
}
#red-slider::-webkit-slider-thumb {
    background: red;
}

#green-slider::-webkit-slider-thumb {
    background: green;
}

#blue-slider::-webkit-slider-thumb {
    background: blue;
}
.slider::-moz-range-thumb {
    width: 25px;
    height: 25px;
    background: #4CAF50;
    cursor: pointer;
}

#square {
    height: 50px;
    width: 50px;
    background-color: #555;
}
    </style>
    </head>
    <body>

        <h1>Custom Range Slider</h1>
        <p>Drag the slider to display the current value.</p>

        <div class="slidecontainer">
            <input type="range" min="1" max="255" value="121" class="slider" id="red-slider">
            <input type="range" min="1" max="255" value="210" class="slider" id="green-slider">
            <input type="range" min="1" max="255" value="166" class="slider" id="blue-slider">
            <div id="square"></div>
        </div>
        <script>

            let red = document.getElementById("red-slider");
            let green = document.getElementById("green-slider");
            let blue = document.getElementById("blue-slider");
            red.addEventListener("input", rgbize);
            green.addEventListener("input", rgbize);
            blue.addEventListener("input", rgbize);
            rgbize();
            function rgbize() {
                rgb = `rgb(${red.value}, ${green.value}, ${blue.value})`;
                document.getElementById("square").style.backgroundColor = rgb;
                xhttp = new XMLHttpRequest();
                xhttp.open("POST", "/rgb", true);
                xhttp.send(JSON.stringify(rgb));
            }
        </script>
    </body>
</html>
    """

@app.route('/rgb', methods=['POST'])
def rgb():
    print(request.data)
    return 'success'

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
