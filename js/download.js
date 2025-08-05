import { UAParser } from "ua-parser-js";
import { el } from "./el";

document.addEventListener("DOMContentLoaded", function () {
  const getTabHash = (element) => {
    while (element) {
      const hash = element.hash;
      if (hash) {
        return hash;
      } else {
        element = element.parentElement;
      }
    }
    return null;
  };

  document.querySelectorAll(".tab-container").forEach((tabContainer) => {
    const tabbar = tabContainer.querySelector(".tabs>ul");
    const buttons = tabContainer.querySelector(".download-buttons>.buttons");
    const pages = tabContainer.querySelectorAll(".tab-page");
    tabbar.onclick = (event) => {
      event.preventDefault();

      const tabHash = getTabHash(event.srcElement);
      if (!tabHash) {
        return;
      }

      const pageId = tabHash.substring(1);

      pages.forEach((p) =>
        p.id === pageId
          ? p.classList.remove("is-hidden")
          : p.classList.add("is-hidden")
      );
      tabbar.childNodes.forEach((c) =>
        c.id === `tab-${pageId}`
          ? c.classList.add("is-active")
          : c.classList.remove("is-active")
      );
      buttons.childNodes.forEach((c) =>
        c.id === `button-${pageId}`
          ? c.classList.add("is-active", "is-light", "is-inverted")
          : c.classList.remove("is-active", "is-light", "is-inverted")
      );

      if (history.pushState && window.location.hash != tabHash) {
        if (!window.location.hash) {
          history.replaceState(null, null, tabHash);
        } else {
          history.pushState(null, null, tabHash);
        }
      }
    };

    pages.forEach((page) => {
      const header = page.querySelector("h1,h2,h3");
      header.classList.add("is-hidden");
      tabbar.appendChild(
        el(
          "li",
          { id: `tab-${page.id}` },
          el(
            "a",
            { href: `#${page.id}` },
            el(
              "span",
              { class: "icon" },
              el("i", { class: header.dataset.icon })
            ),
            el("span", {}, header.textContent)
          )
        )
      );
      buttons.appendChild(
        el(
          "a",
          { id: `button-${page.id}`, href: `#${page.id}`, class: "button" },
          el(
            "span",
            { class: "icon" },
            el("span", { class: header.dataset.icon })
          ),
          el("span", {}, header.textContent)
        )
      );
    });

    let initial = window.location.hash;
    if (!initial || !tabbar.querySelector(`#tab-${initial.substring(1)}>a`)) {
      const ua = new UAParser();
      const os = ua.getOS()?.name || "";
      const device = ua.getDevice()?.model || "";
      if (device.indexOf("iPad") !== -1 || device.indexOf("iPhone") !== -1) {
        initial = "#Browser";
      } else if (os.indexOf("Mac") !== -1) {
        initial = "#OSX";
      } else if (os.indexOf("Windows") !== -1) {
        initial = "#Windows";
      } else if (os.indexOf("Android") !== -1) {
        initial = "#Android";
      } else if (os.indexOf("Linux") !== -1) {
        initial = "#Linux";
      } else {
        initial = "#Source";
      }
    }
    const clickTab = (hash) => {
      const e = tabbar.querySelector(`#tab-${hash.substring(1)}>a`);
      if (e) e.click();
    };
    clickTab(initial);

    window.addEventListener("popstate", () => clickTab(window.location.hash));
  });
});
