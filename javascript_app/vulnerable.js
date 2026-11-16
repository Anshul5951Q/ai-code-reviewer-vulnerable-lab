// INTENTIONALLY VULNERABLE STATIC-ANALYSIS FIXTURES. DO NOT DEPLOY OR RUN.
const childProcess = require("child_process");
const fs = require("fs");

function createArchive(userSuppliedName) {
  // JS-01 command injection: untrusted input passed to a shell.
  childProcess.exec("tar -czf /tmp/archive.tgz " + userSuppliedName);
}
function renderProfile(container, profileText) {
  // JS-02 DOM XSS: untrusted content assigned to innerHTML.
  container.innerHTML = profileText;
}
function calculateExpression(userExpression) {
  // JS-03 code injection: untrusted input evaluated as JavaScript.
  return eval(userExpression);
}
function readExport(exportDirectory, requestedFile) {
  // JS-04 path traversal: requestedFile is not constrained to exportDirectory.
  return fs.readFileSync(exportDirectory + "/" + requestedFile, "utf8");
}
module.exports = { createArchive, renderProfile, calculateExpression, readExport };
