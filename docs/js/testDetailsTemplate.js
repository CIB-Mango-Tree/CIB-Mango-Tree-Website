let templateHTML = `<template id="test-details-template">
			<style>
				@import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css";
				@import url("./docs/css/styles.css");
	
				.fruit-img {
					width: 130px;
					display: block;
				}
	
				slot[name="reqs-boxes"]::slotted(*),
				slot[name="optional-reqs-boxes"]::slotted(*) {
					display: flex;
					flex-wrap: wrap;
				}
	
				slot[name="output-image"]::slotted(*) {
					width: 100%;
				}
			</style>
			<h1 class="display-3">
				<slot name="test-title"></slot>
			</h1>
	
			<div class="row row-cols-1 g-4">
				<div class="col">
					<span class="return"><a href="tests.html">&larr;Return to List of Tests</a></span>
					<img class="fruit-img" src="./docs/images/low-hanging-circle.png" />
					<div class="body">
						<span><b>Summary</b></span>
						<p>
							<slot name="test-summary"></slot>
						</p>
						<p>
							<slot name="code-link"></slot>
						</p>
	
						<span><b>Inspiration</b></span>
						<p>
							<slot name="reference-link"></slot>
						</p>
						<div class="req-fields"><em>Required Fields:</em></div>
	
						<div class="box-row">
							<slot name="reqs-boxes"></slot>
						</div>
	
						<div class="req-fields">
							<em>Optional Fields (for display in output):</em>
						</div>
	
						<div class="box-row">
							<slot name="optional-reqs-boxes"></slot>
						</div>
						<div class="body">
							<span><b>Test Process</b></span>
							<slot name="test-process"></slot>
						</div>
	
						<div class="body">
							<slot name="output-summary"></slot>
						</div>
	
						<slot name="output-image"></slot>
					</div>
				</div>
			</div>
		</template>`;

const templatePlaceholder = document.getElementById("template-placeholder");
templatePlaceholder.outerHTML = templateHTML;

customElements.define('test-details',
  class extends HTMLElement {
    constructor() {
      super();
      const template = document
        .getElementById('test-details-template')
        .content;
      const shadowRoot = this.attachShadow({mode: 'open'})
        .appendChild(template.cloneNode(true));
  }
});
