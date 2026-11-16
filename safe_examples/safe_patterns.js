// Illustrative safer counterparts; validate in full application context.
const childProcess = require("child_process");
const fs = require("fs");
const path = require("path");

function createArchiveSafely(validatedName) {
  return childProcess.execFileSync("tar", ["-czf", "/tmp/archive.tgz", validatedName],
                                   { timeout: 10000 });
}
function renderTextSafely(container, profileText) {
  container.textContent = profileText;
}
function readExportSafely(exportDirectory, requestedFile) {
  const root = path.resolve(exportDirectory);
  const target = path.resolve(root, requestedFile);
  if (target !== root && !target.startsWith(root + path.sep)) {
    throw new Error("Path escapes export directory");
  }
  return fs.readFileSync(target, "utf8");
}
module.exports = { createArchiveSafely, renderTextSafely, readExportSafely };
