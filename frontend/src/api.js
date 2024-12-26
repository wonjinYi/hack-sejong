import axios from "axios";
const BASE_URL = "https://f1a0-115-91-214-4.ngrok-free.app/";

// -------------------------------------------------
// dashboard
// -------------------------------------------------
export async function helloWorld() {
  const res = await axios.get(`${BASE_URL}`, {
    headers: {
      "ngrok-skip-browser-warning": true,
    },
  });
  console.log("[api:helloWorld] res:", res);
  return res;
}

export async function getPowerData(start) {}

export async function getHistory() {}

// -------------------------------------------------
// user
// -------------------------------------------------
export async function postUser() {}
