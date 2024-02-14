import { UAParser } from "ua-parser-js";
import { el } from "./el";

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".tab-container").forEach((tabContainer) => {
    const tabbar = tabContainer.querySelector(".tabs>ul");
    const pages = tabContainer.querySelectorAll(".tab-page");
    tabbar.onclick = (event) => {
      event.preventDefault();

      const tabHash = event.srcElement.hash;
      if (!tabHash) return;

      const pageId = tabHash.substring(1);
      const tabId = "tab-" + tabHash.substring(1);

      pages.forEach((p) =>
        p.id === pageId
          ? p.classList.remove("is-hidden-tablet")
          : p.classList.add("is-hidden-tablet")
      );
      tabbar.childNodes.forEach((c) =>
        c.id === tabId
          ? c.classList.add("is-active")
          : c.classList.remove("is-active")
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
      header.classList.add("is-hidden-tablet");
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
            header.textContent
          )
        )
      );
    });

    let initial = window.location.hash;
    if (!initial || !tabbar.querySelector(`#tab-${initial.substring(1)}>a`)) {
      const os = new UAParser().getOS().name;
      if (os.indexOf("Mac") !== -1) {
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
