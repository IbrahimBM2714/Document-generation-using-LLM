<h1>Document generation using LLM and Langchain</h1>
<p>I have created a program that generates .docx document by utilizing the text provided from an LLM. This was achieved using the docxtpl package of python. This package helps in populating template variables in a document. E.g. in my template.docx file, there was a placeholder {{name}} and using docxtpl, I can dynamically populate a value in that placeholder variable</p>

The files and packages you will need to run this:
<ul>
  <li>Packages: Langchain, ctransformers and docxtpl</li>
  <li>Files: Any LLM from https://huggingface.co/models. </br> The one that I used is: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF</li>
</ul>

<p>Note: You might run into an error where you are unable to install the docxtpl package due to a failed build of lxml. If so, simply execute this command in the terminal: <code> set CFLAGS="-Wno-incompatible-function-pointer-types -Wno-implicit-function-declaration" </code></p>

<h3>How it works</h3>
<ul>
  <li>Using the prompt template from langchain, I specify which fields names I want from the given text and how I want them structures.</li>
  <li>I then provide a text that contains information about the fields</li>
  <li>After I get the values of the template variables using regular expression</li>
  <li>Finally, I use docxtpl to populate the template variables in the document with the values I get.</li>
</ul>

<h3>Provided below is an example scenario:</h3>
</br>

![Capture](https://github.com/IbrahimBM2714/Document-generation-using-LLM/assets/115867055/c344ca34-58ef-428f-938e-ae5874046ede)

</br>

![Capture3](https://github.com/IbrahimBM2714/Document-generation-using-LLM/assets/115867055/3e3dc39f-9638-4d62-8d8b-2e38460fb4e8)

