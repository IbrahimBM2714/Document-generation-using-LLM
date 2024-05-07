from langchain_community.llms import CTransformers
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

import re
from docxtpl import DocxTemplate

template_dict = {"name": "", "age": "", "city": "", "occupation": "",
                 "country": "", "favorite_foods": "", "pet_name": ""}

# Document generation
def doc_gen(text: str):

    # Filling the values of template_dict using regular expressions.
    for key in template_dict:
        match = re.search(rf'{key}:\s*(.+)', text)
        template_dict[key] = match.group(1) if match else None

    context = {}

    for key in template_dict:
        context[key] = template_dict[key]

    print(context)

    doc = DocxTemplate("template.docx")
    doc.render(context)
    doc.save("generated_doc.docx")

# LLM
def llm(input: str, chat_history):

    llm = CTransformers(
        model='mistral-7b-instruct-v0.2.Q2_K.gguf', # Insert the path of the model you have downloaded here.
        model_type='mistral',
        config={'max_new_tokens': 600,
                'temperature': 0.1,
                'context_length': 1024})

    # Prompt tempplate to enable context memory
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Give very precise answers and if you don't know something, say I don't know"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", " I have a form with the fields: name, age, city, occupation, country, favorite_foods, and pet_name.Fill these fields from the following data."),
        ("human", "{input}"),
        ("human", "The output should provide the field followed by the answer, should only contain these fields and nothing else. If you don't know the answer of any field, make the answer blank"),

    ])

    llm_chain = prompt | llm

    output = llm_chain.invoke({"chat_history": chat_history, "input": input})

    doc_gen(output)

    return output


if __name__ == "__main__":

    chat_history = []

    # The text I gave to the model was:
    # In the bustling metropolis of Tokyo where skyscrapers towered over bustling streets and neon lights painted the night sky, there resided a woman of singular determination and grace. Known to all as Dr. Amelia Sinclair, she was a pioneer in the field of quantum physics, her groundbreaking research pushing the boundaries of human understanding. At the age of 35, Dr. Sinclair had already achieved more than most could dream of. Born and raised in the vibrant city of Japan she had inherited a love for innovation and technology from her parents, both esteemed engineers. From a young age, Amelia displayed an insatiable curiosity for the mysteries of the universe, spending countless hours poring over equations and conducting experiments in her makeshift laboratory. But Amelia's passions were not limited to the confines of academia. In her spare time, she found solace in the art of culinary experimentation, crafting gourmet dishes that delighted the senses and pushed the boundaries of flavor. Her favorite foods ranged from the delicate simplicity of sushi to the fiery complexity of Indian curry, each dish a testament to her adventurous palate and creative spirit. Despite her busy schedule, Amelia always made time for her faithful companion, a sleek black cat named Nebula. With his piercing green eyes and regal bearing, Nebula was more than just a pet; he was a confidant, a source of comfort in times of stress, and a reminder of the beauty of the natural world. As Amelia embarked on yet another daring experiment, her mind buzzing with possibilities, she knew that she was exactly where she was meant to be. For in the boundless expanse of the cosmos, amidst the chaos and the uncertainty, she found a sense of purpose that fueled her every endeavor.
    # You can use a similar text to check the code. Make sure the text has the answers to the fields: name, age, city, occupation, country, pet name and favorite foods.
    # Ofcourse, you can use your specifiy your own fields names and input too.

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = llm(user_input, chat_history)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response))
        print("Assistant: ", response)
