const fs = require("fs");
const path = require("path");
const uuid = require("uuid");

const { promisify } = require("node:util");
const exec = promisify(require("node:child_process").exec);

const ENV_FILE = "./config.env";
const TMP_FOLDER = "./tmp";

async function allowPort(port) {
  const command = `ufw allow ${port}`;
  const result = await exec(command);

  return result.stdout ? true : false;
}

async function denyPort(port) {
  const command = `ufw deny ${port}`;
  const result = await exec(command);

  return result.stdout ? true : false;
}

async function getContainerPort(container) {
  const command = `docker port ${container}-backend-1`;
  const result = await exec(command);

  const portReg = /:(\d+)/;
  const portNumber = result.stdout.match(portReg)[1];

  return portNumber;
}

async function createComposeFile(composePath) {
  // create file
  const fname = uuid.v1();
  const command = `docker compose --env-file ${ENV_FILE} -p ${fname} -f ${composePath}/docker-compose.yml config`;
  const result = await exec(command);

  const fpath = path.resolve(TMP_FOLDER, fname);
  fs.writeFileSync(fpath, result.stdout);

  return { fname, fpath };
}

async function runComposeFile({ fname, fpath }) {
  const command = `docker compose -f ${fpath} up -d`;
  const result = await exec(command);
  const port = await getContainerPort(fname);

  return {
    composerFile: fname,
    composerPath: fpath,
    port,
  };
}

async function removeComposerFile(composePath) {
  const command = `docker compose -f ${composePath} down`;
  const result = await exec(command);

  return result;
}

async function up(composePath) {
  const command = `docker compose -f ${composePath} up`;
  const result = exec(command);

  return result;
}

function down(composePath) {
  const command = `docker compose -f ${composePath} down`;
  const result = exec(command);

  return result;
}

module.exports = {
  removeComposerFile,
  runComposeFile,
  createComposeFile,
  up,
  down,
  allowPort,
  denyPort,
};
