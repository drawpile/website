(function () {
  const { username, frameancestors } = document.querySelector("#auth").dataset;
  const allowedOrigins = (frameancestors || "").trim().split(/\s+/);

  function setMessage(message) {
    document.querySelector("#auth-message").textContent = message;
  }

  async function authenticate(payload, origin) {
    try {
      const response = await fetch("/api/ext-auth/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify(payload),
      });

      if (response.status !== 200) {
        throw new Error(`Server responded with status ${response.status}.`);
      }

      const result = await response.json();
      if (result.status === "badpass") {
        throw new Error("Not logged in.");
      } else if (result.status === "banned") {
        throw new Error("Banned.");
      } else if (result.status === "outgroup") {
        throw new Error("Not in the required group.");
      } else if (result.status !== "auth") {
        throw new Error(`Unknown status '${result.status}'.`);
      }

      if (!result.token || typeof result.token !== "string") {
        throw new Error(`Missing token.`);
      }

      window.parent.postMessage(
        { type: "auth-identified", token: result.token },
        origin
      );
    } catch (e) {
      console.error(e);
      setMessage(`Authentication failed: ${e.message}`);
    }
  }

  window.addEventListener("message", (e) => {
    if (allowedOrigins.includes(e.origin)) {
      const type = e.data?.type;
      if (type === "auth-authenticate") {
        const payload = { ...e.data.args, username, password: false };
        authenticate(payload, e.origin);
      } else {
        console.error("Unknown message type", e);
      }
    } else {
      console.warning("Origin not allowed", e);
    }
  });

  window.parent.postMessage({ type: "auth-username-selected", username }, "*");
})();
