import http from "k6/http";
import { sleep } from "k6";

// Stress
const stress = {
  stages: [
    { target: 100, duration: "5m" },
    { target: 250, duration: "10m" },
    { target: 100, duration: "5m" },
  ],
};

function makeRandomString(length) {
  let result = "";
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

const generateUser = (random) => {
  return {
    name: random ? makeRandomString(5) : "defualt_value",
    username: random ? makeRandomString(5) : "defualt_value",
    email: random ? makeRandomString(5) : "defualt_value",
    date: random ? makeRandomString(5) : "defualt_value",
    dateOfBirth: random ? makeRandomString(5) : "defualt_value",
    location: random ? makeRandomString(5) : "defualt_value",
    gender: random ? makeRandomString(5) : "defualt_value",
  };
};

const baseUrl = `${__ENV.HOSTNAME}`;

export const options = stress;

export default function () {
  // Consulta
  const ENDPOINT = `${baseUrl}/users`;
  http.get(ENDPOINT);

  const params = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  // Criacao
  const resPost = http.post(
    `${ENDPOINT}`,
    JSON.stringify(generateUser()),
    params
  );
  const userId = JSON.parse(resPost.body).id;

  // Edição
  const resPut = http.put(
    `${ENDPOINT}/${userId}`,
    JSON.stringify(generateUser(true)),
    params
  );

  // Remocao
  http.del(`${ENDPOINT}/${userId}`);

  sleep(1);
}
