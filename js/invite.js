import { UAParser } from "ua-parser-js";

(function () {
  function flickerElement(elem) {
    elem.classList.add("is-invisible");
    window.setTimeout(() => elem.classList.remove("is-invisible"), 100);
  }

  const title = document.getElementById("invite-link-title");
  const input = document.getElementById("invite-link-input");
  const button = document.getElementById("invite-link-copy-button");
  const checked = document.getElementById("invite-link-checked");
  const openLink = document.getElementById("invite-link-open");
  const webLink = document.getElementById("invite-link-web");
  const needsPasswordMessage = document.getElementById("invite-needs-password");

  try {
    const ua = new UAParser();
    const os = ua.getOS()?.name || "";
    const show = os.indexOf("Windows") !== -1 || os.indexOf("Linux") !== -1;
    if (show) {
      document
        .getElementById("invite-section-open")
        .classList.remove("is-hidden");
    }
  } catch (e) {
    console.error(e);
  }

  let link = input.value;
  const hash = window.location.hash;
  const havePassword = hash && hash.length > 1;
  if (checked.value === "") {
    if (havePassword) {
      const separator = link.indexOf("?") === -1 ? "?" : "&";
      link += `${separator}p=${hash.substring(1)}`;
    }
    input.value = link;
    checked.value = "1";
  }

  if (needsPasswordMessage && !havePassword) {
    const article = document.createElement("article");
    article.className = "message is-info";

    const div = document.createElement("div");
    div.className = "message-body";
    article.appendChild(div);

    const span = document.createElement("span");
    span.className = "fas fa-lock";
    div.appendChild(span);

    div.appendChild(
      document.createTextNode(" This session requires a password to join."),
    );

    needsPasswordMessage.replaceWith(article);
  }

  button.addEventListener("click", () => {
    input.select();
    navigator.clipboard.writeText(input.value).then(
      () => {
        title.textContent = "Link copied! Paste it into Drawpile.";
        title.classList = "";
        flickerElement(title);
      },
      () => {
        title.textContent = "Copying failed, please do so manually.";
        title.classList = "has-text-danger";
        flickerElement(title);
      },
    );
  });

  openLink.href = link;
  if (webLink && hash && hash.length > 1) {
    webLink.href += window.location.hash;
  }
})();
