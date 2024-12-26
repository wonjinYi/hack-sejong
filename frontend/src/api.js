import axios from "axios";
const BASE_URL = "https://0fd8-115-91-214-4.ngrok-free.app";

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

export async function getPowerData(start) {
  const res = await axios.get(`${BASE_URL}/power`, {
    params: {
      start: start,
    },
    headers: {
      "ngrok-skip-browser-warning": true,
    },
  });
  console.log("[api:getPowerData] res.data:", res.data);

  const data = res.data.data.map((el) => {
    const date = new Date(el.timestamp);
    const hours = String(date.getHours()).padStart(2, "0"); // 두 자리 숫자로 포맷
    const minutes = String(date.getMinutes()).padStart(2, "0"); // 두 자리 숫자로 포맷
    const time = `${hours}:${minutes}`; // 'hh:mm' 형식으로 조합

    return {
      timestamp: time,
      value: el.value,
    };
  });

  return {
    data: data,
    nextIndex: res.data.end,
  };
}

export async function getHistory() {}

// -------------------------------------------------
// user
// -------------------------------------------------
export async function postUser(id) {
  const res = await axios.post(
    `${BASE_URL}/user`,
    {
      id: id,
    },
    {
      headers: {
        "ngrok-skip-browser-warning": true,
      },
    }
  );
  console.log("[api:postUser] res:", res);
  return res;
}
