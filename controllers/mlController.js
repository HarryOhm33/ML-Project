require("dotenv").config(); // Load environment variables
const { spawn } = require("child_process");
const path = require("path");

// Determine Python executable dynamically
const pythonPath =
  process.platform === "win32"
    ? path.join(__dirname, "../venv/Scripts/python.exe") // Windows
    : path.join(__dirname, "../venv/bin/python"); // Mac/Linux

// Get Python script path from .env
const pythonScriptPath = path.resolve(process.env.PYTHON_SCRIPT_PATH);

exports.runMLModel = (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ message: "Text input is required" });
  }

  console.log(`🚀 Running ML Model with input: "${text}"`);

  const pythonProcess = spawn(pythonPath, [pythonScriptPath]);

  let result = "";
  let errorMessage = "";

  // Send input safely via stdin
  pythonProcess.stdin.write(JSON.stringify({ input: text }) + "\n");
  pythonProcess.stdin.end();

  pythonProcess.stdout.on("data", (data) => {
    result += data.toString().trim();
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
