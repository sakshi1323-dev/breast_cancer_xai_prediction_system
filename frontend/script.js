const features = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean",
    "concave points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",
    "radius_se",
    "texture_se",
    "perimeter_se",
    "area_se",
    "smoothness_se",
    "compactness_se",
    "concavity_se",
    "concave points_se",
    "symmetry_se",
    "fractal_dimension_se",
    "radius_worst",
    "texture_worst",
    "perimeter_worst",
    "area_worst",
    "smoothness_worst",
    "compactness_worst",
    "concavity_worst",
    "concave points_worst",
    "symmetry_worst",
    "fractal_dimension_worst"
];

const inputDiv = document.getElementById("inputs");

// create inputs
features.forEach(f => {
    inputDiv.innerHTML += `
        <label>${f}</label>
        <input type="number" id="${f}" value="0"><br><br>
    `;
});

async function predict() {
    let data = {};

    features.forEach(f => {
        data[f] = parseFloat(document.getElementById(f).value);
    });

    const response = await fetch("https://breast-cancer-xai-prediction-system.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        `Prediction: ${result.prediction}, Risk Score: ${result.risk_score}`;
}