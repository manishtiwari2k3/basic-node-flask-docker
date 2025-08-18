const express = require("express");
const axios = require("axios");
const path = require("path");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;
// When running with Docker Compose, set API_BASE_URL to "http://backend:5000"
const API_BASE_URL = process.env.API_BASE_URL || "http://localhost:5000";

app.use(express.urlencoded({ extended: true })); // parse form data
app.use(express.json()); // allow JSON body parsing
app.use(express.static(path.join(__dirname, "views"))); // serve static files (html)

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.post("/submit", async (req, res) => {
  try {
    // Forward the form data to the Flask backend
    const response = await axios.post(`${API_BASE_URL}/process`, req.body, {
      headers: { "Content-Type": "application/json" } // send as JSON
    });

    res.send(`
      <h2>Response from Flask:</h2>
      <p>${response.data.message}</p>
      <p><a href="/">Go back</a></p>
    `);
  } catch (err) {
    res.status(500).send(`
      <h2>Something went wrong</h2>
      <pre>${err.message}</pre>
      <p><a href="/">Go back</a></p>
    `);
  }
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});
// Export the app for testing or other purposes