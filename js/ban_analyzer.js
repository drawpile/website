import { el } from "./el";

(function () {
  "use strict";
  const inputElement = document.querySelector("#ban-analyzer-input");
  const resultsElement = document.querySelector("#ban-analyzer-results");

  function extractUsername(line) {
    const matchWithIp = /\b[0-9]+;[0-9a-f:\.]+;(.+?):?\s+{/.exec(line);
    if (matchWithIp) {
      return matchWithIp[1];
    }

    const matchWithoutIp = /\b[0-9]+;(.+?):?\s+{/.exec(line);
    if (matchWithoutIp) {
      return matchWithoutIp[1];
    }

    return "";
  }

  function extractOs(os) {
    if (os === "android") {
      return "Android";
    } else if (os === "emscripten") {
      return "Browser";
    } else if (os === "linux") {
      return "Linux";
    } else if (os === "darwin") {
      return "macOS";
    } else if (os === "winnt") {
      return "Windows";
    } else if (os) {
      return `${os}`;
    } else {
      return "";
    }
  }

  function extractAddress(address) {
    return address ? `${address}`.replace(/^::ffff:/, "") : "";
  }

  function extractUserId(authId) {
    if (authId) {
      const match = /^drawpile.net:([0-9]+)$/.exec(`${authId}`);
      if (match) {
        return match[1];
      }
    }
    return "";
  }

  function analyzeLine(line) {
    // [2024-03-19T14:53:59] 1;askmeaboutloom: {"address":"::ffff:123.253.321","app_version":"2.2.1","auth_id":"drawpile.net:108094","os":"winnt","protocol_version":"dp:4.24.0","qt_version":"5","s":"0123456789abcdef0123456789abcdef"}
    const username = extractUsername(line);
    while (true) {
      const curlyIndex = line.indexOf("{");
      if (curlyIndex === -1) {
        return null;
      } else {
        line = line.substr(curlyIndex);
        try {
          const data = JSON.parse(line);
          return {
            os: extractOs(data.os),
            username,
            address: extractAddress(data.address),
            sid: data.s || "",
            userId: extractUserId(data.auth_id),
          };
        } catch (e) {
          console.error(line, e);
        }
        line = line.substr(1);
      }
    }
  }

  function isDuplicateResult(candidates, result) {
    for (const candidate of candidates) {
      if (
        result.os === candidate.os &&
        result.username === candidate.username &&
        result.address === candidate.address &&
        result.sid === candidate.sid &&
        result.userId === candidate.userId
      ) {
        return true;
      }
    }
    return false;
  }

  function analyze() {
    const results = [];
    for (const line of inputElement.value.split("\n")) {
      try {
        const result = analyzeLine(line.trim());
        if (result && !isDuplicateResult(results, result)) {
          results.push(result);
        }
      } catch (e) {
        console.error(line, e);
      }
    }

    resultsElement.innerHTML = "";
    if (results.length === 0) {
      resultsElement.appendChild(
        el(
          "tr",
          {},
          el(
            "td",
            { class: "is-italic", colspan: "4" },
            "Nothing here. Paste logs into the field above."
          )
        )
      );
    } else {
      for (const result of results) {
        resultsElement.appendChild(
          el(
            "tr",
            {},
            el("td", {}, result.os),
            el("td", {}, result.username),
            el("td", {}, result.address),
            el("td", {}, result.sid),
            el("td", {}, result.userId)
          )
        );
      }
    }
  }

  inputElement.addEventListener("input", analyze);
  analyze();
})();
