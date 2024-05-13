const { promisify } = require("node:util");

const fs = require("fs");
const readdir = promisify(fs.readdir);
const rmFile = promisify(fs.rm);
const writeFile = promisify(fs.writeFile);

const path = require("path");

const dockerAPI = require("./dockerAPI");
const COMPOSERS_FOLDER = "./composers";
const CONFIG_FILE = "./config.env";

const applications = [];

function getApplications() {
  return applications;
}

async function getAvailablesConfigs() {
  return await readdir(COMPOSERS_FOLDER);
}

async function runComposer({ conf, backend, database }) {
  const finfo = await dockerAPI.createComposeFile(
    path.join(COMPOSERS_FOLDER, conf)
  );

  const config = await createConfig(backend, database);
  const compose = await dockerAPI.runComposeFile(finfo);
  const newApp = { ...compose, backend, database, conf };

  applications.push(newApp);

  return newApp;
}

async function removeComposer({ composerFile }) {
  const application = applications.find(
    (app) => app.composerFile === composerFile
  );

  if (application) {
    const index = applications.indexOf(application);
    applications.splice(index, 1);

    await dockerAPI.removeComposerFile(application.composerPath);
    await rmFile(application.composerPath);

    return { result: "FILE REMOVED" };
  }

  return { result: "FILE NOT FOUND" };
}

async function createConfig(backend, database) {
  await writeFile(
    CONFIG_FILE,
    `
# CPUS can receive fractions (ex: 0.5)
# MEMORY receive value measure (ex: 4M)

BK_CPUS=${backend.cpu}
BK_MEMORY=${backend.ram}
DB_CPUS=${database.cpu}
DB_MEMORY=${database.ram}
`
  );
}

module.exports = {
  runComposer,
  getAvailablesConfigs,
  getApplications,
  removeComposer,
};
