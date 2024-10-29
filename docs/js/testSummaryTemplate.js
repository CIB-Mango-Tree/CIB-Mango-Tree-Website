customElements.define('test-summary',
  class extends HTMLElement {
    constructor() {
      super();
      const template = document
        .getElementById('test-summary-template')
        .content;
      const shadowRoot = this.attachShadow({mode: 'open'})
        .appendChild(template.cloneNode(true));
  }
});
