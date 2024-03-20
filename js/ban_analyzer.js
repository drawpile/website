import { el } from "./el";

(function () {
  "use strict";
  const inputElement = document.querySelector("#ban-analyzer-input");
  const resultsElement = document.querySelector("#ban-analyzer-results");

  function extractUsername(line) {
    const matchWithIp = /\b[0-9]+;[0-9a-f:\.]+;(.+?):?\s+{/.exec(line);
    if(matchWithIp) {
      return matchWithIp[1];
    }

    const matchWithoutIp = /\b[0-9]+;(.+?):?\s+{/.exec(line);
    if(matchWithoutIp) {
      return matchWithoutIp[1];
    }

    return "";
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

  function analyze() {
    const results = [];
    for (const line of inputElement.value.split("\n")) {
      try {
        const result = analyzeLine(line.trim());
        if (result) {
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
