/* DOM building helper function */
export function el(name, attrs = {}, ...children) {
  const element = document.createElement(name);
  for (const [key, value] of Object.entries(attrs)) {
    if (key === "onclick") element.onclick = value;
    else element.setAttribute(key, value);
  }
  children.forEach((c) => {
    if (typeof c === "string") {
      c = document.createTextNode(c);
    }
    element.appendChild(c);
  });
  return element;
}
