const { spawn } = require("child_process");
const path = require("path");

exports.runMLModel = (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ message: "Text input is required" });
  }

  // Log when the ML model starts
  console.log(`🚀 Running ML Model with input: "${text}"`);

  const pythonPath = path.join(__dirname, "../venv/Scripts/python.exe"); // Windows
  // const pythonPath = path.join(__dirname, "../venv/bin/python"); // Mac/Linux

  const pythonProcess = spawn(pythonPath, [
    path.join(__dirname, "../ml_model/model.py"),
  ]);

  let result = "";
  let errorMessage = "";

  // Send input safely via stdin
  pythonProcess.stdin.write(JSON.stringify({ input: text }) + "\n");
  pythonProcess.stdin.end();

  pythonProcess.stdout.on("data", (data) => {
    result += data.toString().trim();
    // console.log(`📤 Model Output: ${result}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    errorMessage += data.toString().trim();
    console.error(`❌ Model Error: ${errorMessage}`);
  });

  pythonProcess.on("close", (code) => {
    console.log(`🔚 ML Model process exited with code: ${code}`);

    if (code !== 0 || (errorMessage && !result)) {
      return res.status(500).json({
        message: "Error processing ML model",
        error: errorMessage || `Process exited with code ${code}`,
      });
    }

    console.log(`✅ Final Prediction: ${result}`);
    res.json({ prediction: result });
  });
};
