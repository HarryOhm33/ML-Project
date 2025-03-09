const express = require("express");
const { runMLModel } = require("../controllers/mlController");

const router = express.Router();

router.post("/predict", runMLModel);

module.exports = router;
