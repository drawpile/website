import { el } from "./el";

document.addEventListener("DOMContentLoaded", function () {
  /* Navbar toggle (mobile) */
  document.querySelectorAll("#navbar-toggle").forEach((elem) => {
    elem.onclick = function () {
      this.classList.toggle("is-active");
      document.getElementById("navbar-menu").classList.toggle("is-active");
    };
  });

  /* Thumbnail modal links */
  const closeModal = () => modal.classList.remove("is-active");
  const modal = el(
    "div",
    { class: "modal" },
    el("div", { class: "modal-background", onclick: closeModal }),
    el("div", { class: "modal-content" }),
    el("button", { class: "modal-close", onclick: closeModal })
  );

  const showTumbnailModal = (e) => {
    e.preventDefault();
    const el = e.path.find((i) => i.localName === "a");
    modal.querySelector(
      ".modal-content"
    ).innerHTML = `<img src="${el.getAttribute("href")}">`;
    modal.classList.add("is-active");
  };
  document
    .querySelectorAll("a.thumbnail-link")
    .forEach((el) => (el.onclick = showTumbnailModal));
  document.body.appendChild(modal);

  /* Links that open in new windows */
  function openSmallNewWindow(e) {
    e.preventDefault();
    let target = e.target;
    while (target) {
      if (target.href) {
        window.open(target.href, "smallwindow", "width=500,height=600");
        break;
      }
      target = target.parentElement;
    }
  }
  document
    .querySelectorAll("a.smallNewWindow")
    .forEach((e) => (e.onclick = openSmallNewWindow));

  /* Some users double-click on submit buttons, prevent double-submissions */
  document.querySelectorAll("form.disable-button-on-submit").forEach((form) => {
    form.addEventListener("submit", (event) => {
      if (form.dataset.submitted) {
        event.preventDefault();
        event.target
          .querySelectorAll("button[type=submit], input[type=submit]")
          .forEach((button) => {
            button.disabled = true;
          });
      } else {
        form.dataset.submitted = "true";
      }
    });
    // Clear submitted flag whenever the page is loaded. Otherwise returning to
    // the form via the back button reloads it in an unusable state.
    window.addEventListener("pageshow", () => {
      delete form.dataset.submitted;
    });
  });
});

window.getCookie = function (name) {
  if (document.cookie) {
    const prefix = name + "=";
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(prefix)) {
        return decodeURIComponent(cookie.substring(prefix.length));
      }
    }
  }
  return null;
};
