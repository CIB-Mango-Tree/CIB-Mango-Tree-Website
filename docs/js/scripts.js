/*customElements.define('test-summary',
  class extends HTMLElement {
    constructor() {
      super();
      const template = document
        .getElementById('test-summary-template')
        .content;
      const shadowRoot = this.attachShadow({mode: 'open'})
        .appendChild(template.cloneNode(true));
  }
});*/

customElements.define("test-summary", class extends HTMLElement {
    connectedCallback() {
      let template = document.getElementById(this.nodeName);
      this.innerHTML = template.innerHTML;
      this.append(template.content.cloneNode(true))
    }
  })
